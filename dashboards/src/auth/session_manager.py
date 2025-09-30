"""
Gestión de sesiones de usuario
"""
import uuid
import time
from typing import Dict, Optional
from dataclasses import dataclass
from src.auth.user_manager import User, user_manager

@dataclass
class Session:
    """Modelo de sesión"""
    session_id: str
    user_id: str
    username: str
    role: str
    created_at: float
    last_activity: float
    is_active: bool = True

class SessionManager:
    """Gestor de sesiones en memoria"""
    
    def __init__(self, session_timeout: int = 86400):  # 24 horas por defecto
        self.sessions: Dict[str, Session] = {}
        self.session_timeout = session_timeout
    
    def create_session(self, user: User) -> str:
        """Crear nueva sesión para un usuario"""
        session_id = str(uuid.uuid4())
        current_time = time.time()
        
        session = Session(
            session_id=session_id,
            user_id=user.id,
            username=user.username,
            role=user.role.value,
            created_at=current_time,
            last_activity=current_time
        )
        
        self.sessions[session_id] = session
        return session_id
    
    def get_session(self, session_id: str) -> Optional[Session]:
        """Obtener sesión por ID"""
        session = self.sessions.get(session_id)
        
        if session and session.is_active:
            # Verificar si la sesión ha expirado
            if time.time() - session.last_activity > self.session_timeout:
                self.invalidate_session(session_id)
                return None
            
            # Actualizar última actividad
            session.last_activity = time.time()
            return session
        
        return None
    
    def invalidate_session(self, session_id: str) -> bool:
        """Invalidar sesión"""
        if session_id in self.sessions:
            self.sessions[session_id].is_active = False
            del self.sessions[session_id]
            return True
        return False
    
    def get_user_from_session(self, session_id: str) -> Optional[User]:
        """Obtener usuario desde sesión"""
        session = self.get_session(session_id)
        if session:
            return user_manager.get_user_by_id(session.user_id)
        return None
    
    def cleanup_expired_sessions(self):
        """Limpiar sesiones expiradas"""
        current_time = time.time()
        expired_sessions = []
        
        for session_id, session in self.sessions.items():
            if current_time - session.last_activity > self.session_timeout:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            self.invalidate_session(session_id)
    
    def get_active_sessions_count(self) -> int:
        """Obtener número de sesiones activas"""
        return len([s for s in self.sessions.values() if s.is_active])

# Instancia global del gestor de sesiones
session_manager = SessionManager()
