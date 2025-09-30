"""
Gestor de tokens JWT para autenticación stateless
"""
import jwt
import time
import uuid
from datetime import datetime, timedelta
from typing import Dict, Optional, Tuple
from dataclasses import dataclass
import os
from src.auth.user_manager import User, UserRole

@dataclass
class TokenPair:
    """Par de tokens (access + refresh)"""
    access_token: str
    refresh_token: str
    expires_at: datetime

class JWTManager:
    """Gestor de tokens JWT"""
    
    def __init__(self):
        from config import config
        
        # Clave secreta para firmar tokens
        self.secret_key = config.JWT_SECRET_KEY
        self.algorithm = config.JWT_ALGORITHM
        
        # Tiempos de expiración
        self.access_token_expiry = config.JWT_ACCESS_TOKEN_EXPIRY
        self.refresh_token_expiry = config.JWT_REFRESH_TOKEN_EXPIRY
        
        # Blacklist para tokens invalidados (en producción usar Redis)
        self.token_blacklist = set()
    
    def create_token_pair(self, user: User) -> TokenPair:
        """Crear par de tokens (access + refresh) para un usuario"""
        current_time = datetime.utcnow()
        access_expiry = current_time + timedelta(seconds=self.access_token_expiry)
        refresh_expiry = current_time + timedelta(seconds=self.refresh_token_expiry)
        
        # Payload del access token
        access_payload = {
            'user_id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role.value,
            'full_name': user.full_name,
            'token_type': 'access',
            'iat': current_time,
            'exp': access_expiry,
            'jti': str(uuid.uuid4())  # JWT ID único
        }
        
        # Payload del refresh token
        refresh_payload = {
            'user_id': user.id,
            'token_type': 'refresh',
            'iat': current_time,
            'exp': refresh_expiry,
            'jti': str(uuid.uuid4())
        }
        
        # Crear tokens
        access_token = jwt.encode(access_payload, self.secret_key, algorithm=self.algorithm)
        refresh_token = jwt.encode(refresh_payload, self.secret_key, algorithm=self.algorithm)
        
        return TokenPair(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_at=access_expiry
        )
    
    def verify_token(self, token: str) -> Optional[Dict]:
        """Verificar y decodificar token"""
        try:
            # Verificar si el token está en la blacklist
            if token in self.token_blacklist:
                return None
            
            # Decodificar y verificar token
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            
            # Verificar tipo de token
            if payload.get('token_type') != 'access':
                return None
            
            return payload
            
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def verify_refresh_token(self, token: str) -> Optional[Dict]:
        """Verificar refresh token"""
        try:
            if token in self.token_blacklist:
                return None
            
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            
            if payload.get('token_type') != 'refresh':
                return None
            
            return payload
            
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
    
    def refresh_access_token(self, refresh_token: str) -> Optional[TokenPair]:
        """Renovar access token usando refresh token"""
        payload = self.verify_refresh_token(refresh_token)
        if not payload:
            return None
        
        # Obtener usuario
        from src.auth.user_manager import user_manager
        user = user_manager.get_user_by_id(payload['user_id'])
        if not user or not user.is_active:
            return None
        
        # Crear nuevo par de tokens
        return self.create_token_pair(user)
    
    def blacklist_token(self, token: str) -> bool:
        """Agregar token a la blacklist"""
        try:
            # Decodificar token para obtener expiración
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm], options={"verify_exp": False})
            
            # Solo agregar a blacklist si no ha expirado
            if payload.get('exp', 0) > time.time():
                self.token_blacklist.add(token)
                return True
            return False
        except jwt.InvalidTokenError:
            return False
    
    def blacklist_user_tokens(self, user_id: str) -> int:
        """Invalidar todos los tokens de un usuario (requiere implementación con Redis)"""
        # En una implementación completa, esto requeriría Redis para trackear tokens por usuario
        # Por ahora, solo limpiamos la blacklist periódicamente
        return 0
    
    def cleanup_expired_tokens(self):
        """Limpiar tokens expirados de la blacklist"""
        current_time = time.time()
        expired_tokens = []
        
        for token in self.token_blacklist:
            try:
                payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm], options={"verify_exp": False})
                if payload.get('exp', 0) <= current_time:
                    expired_tokens.append(token)
            except jwt.InvalidTokenError:
                expired_tokens.append(token)
        
        for token in expired_tokens:
            self.token_blacklist.discard(token)
    
    def get_user_from_token(self, token: str) -> Optional[User]:
        """Obtener usuario desde token"""
        payload = self.verify_token(token)
        if not payload:
            return None
        
        from src.auth.user_manager import user_manager
        return user_manager.get_user_by_id(payload['user_id'])
    
    def is_token_blacklisted(self, token: str) -> bool:
        """Verificar si un token está en la blacklist"""
        return token in self.token_blacklist

# Instancia global del gestor JWT
jwt_manager = JWTManager()
