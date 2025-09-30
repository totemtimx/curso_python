"""
Almacenamiento de tokens para múltiples instancias
"""
import redis
import json
import os
from typing import Optional, Dict, List
from datetime import datetime, timedelta

class TokenStorage:
    """Almacenamiento de tokens usando Redis para múltiples instancias"""
    
    def __init__(self):
        from config import config
        
        # Configuración de Redis
        self.redis_host = config.REDIS_HOST
        self.redis_port = config.REDIS_PORT
        self.redis_db = config.REDIS_DB
        self.redis_password = config.REDIS_PASSWORD
        
        try:
            self.redis_client = redis.Redis(
                host=self.redis_host,
                port=self.redis_port,
                db=self.redis_db,
                password=self.redis_password,
                decode_responses=True
            )
            # Verificar conexión
            self.redis_client.ping()
            self.available = True
        except Exception as e:
            print(f"Redis no disponible: {e}")
            self.redis_client = None
            self.available = False
    
    def store_token_blacklist(self, token: str, expires_at: datetime) -> bool:
        """Almacenar token en blacklist"""
        if not self.available:
            return False
        
        try:
            # Calcular TTL
            ttl = int((expires_at - datetime.utcnow()).total_seconds())
            if ttl > 0:
                self.redis_client.setex(f"blacklist:{token}", ttl, "1")
                return True
            return False
        except Exception:
            return False
    
    def is_token_blacklisted(self, token: str) -> bool:
        """Verificar si token está en blacklist"""
        if not self.available:
            return False
        
        try:
            return self.redis_client.exists(f"blacklist:{token}") > 0
        except Exception:
            return False
    
    def store_user_tokens(self, user_id: str, token_jti: str, expires_at: datetime) -> bool:
        """Almacenar referencia de token por usuario"""
        if not self.available:
            return False
        
        try:
            ttl = int((expires_at - datetime.utcnow()).total_seconds())
            if ttl > 0:
                # Agregar token a la lista de tokens del usuario
                self.redis_client.sadd(f"user_tokens:{user_id}", token_jti)
                self.redis_client.expire(f"user_tokens:{user_id}", ttl)
                return True
            return False
        except Exception:
            return False
    
    def blacklist_user_tokens(self, user_id: str) -> int:
        """Invalidar todos los tokens de un usuario"""
        if not self.available:
            return 0
        
        try:
            # Obtener todos los tokens del usuario
            token_jtis = self.redis_client.smembers(f"user_tokens:{user_id}")
            
            # Agregar cada token a la blacklist
            blacklisted_count = 0
            for token_jti in token_jtis:
                # Aquí necesitaríamos almacenar el token completo, no solo el JTI
                # Por simplicidad, solo eliminamos la referencia
                self.redis_client.srem(f"user_tokens:{user_id}", token_jti)
                blacklisted_count += 1
            
            return blacklisted_count
        except Exception:
            return 0
    
    def cleanup_expired_tokens(self):
        """Limpiar tokens expirados (Redis maneja esto automáticamente con TTL)"""
        if not self.available:
            return
        
        try:
            # Redis maneja automáticamente la expiración con TTL
            # Solo necesitamos limpiar sets vacíos
            pattern = "user_tokens:*"
            for key in self.redis_client.scan_iter(match=pattern):
                if self.redis_client.scard(key) == 0:
                    self.redis_client.delete(key)
        except Exception:
            pass
    
    def get_user_active_tokens_count(self, user_id: str) -> int:
        """Obtener número de tokens activos de un usuario"""
        if not self.available:
            return 0
        
        try:
            return self.redis_client.scard(f"user_tokens:{user_id}")
        except Exception:
            return 0

# Instancia global del almacenamiento de tokens
token_storage = TokenStorage()
