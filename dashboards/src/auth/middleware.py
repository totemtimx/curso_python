"""
Middleware de autenticación con JWT
"""
from dash import html, dcc
from src.auth.jwt_manager import jwt_manager
from src.auth.user_manager import UserRole
from typing import Optional, Dict, Any

def require_auth(session_data: Optional[Dict], user_data: Optional[Dict]) -> bool:
    """Verificar si el usuario está autenticado usando JWT"""
    # Si no hay datos de sesión, no está autenticado
    if not session_data:
        return False
    
    # Obtener token de acceso
    access_token = session_data.get('access_token')
    if not access_token:
        return False
    
    # Verificar token JWT
    payload = jwt_manager.verify_token(access_token)
    if not payload:
        return False
    
    # Si tenemos user_data, verificar que coincida
    if user_data:
        user_id_from_data = user_data.get('id')
        if user_id_from_data and user_id_from_data != payload.get('user_id'):
            return False
    
    return True

def require_role(session_data: Optional[Dict], user_data: Optional[Dict], required_role: UserRole) -> bool:
    """Verificar si el usuario tiene el rol requerido"""
    if not require_auth(session_data, user_data):
        return False
    
    # Obtener rol del token JWT
    access_token = session_data.get('access_token')
    if not access_token:
        return False
    
    payload = jwt_manager.verify_token(access_token)
    if not payload:
        return False
    
    user_role = payload.get('role')
    if not user_role:
        return False
    
    # Verificar jerarquía de roles
    role_hierarchy = {
        'viewer': 1,
        'analyst': 2,
        'manager': 3,
        'admin': 4
    }
    
    user_level = role_hierarchy.get(user_role, 0)
    required_level = role_hierarchy.get(required_role.value, 0)
    
    return user_level >= required_level

def create_auth_guard():
    """Crear componente de protección de autenticación"""
    return html.Div([
        dcc.Store(id='auth-session-store', storage_type='session'),
        dcc.Store(id='auth-user-store', storage_type='session'),
        html.Div(id='auth-content')
    ])

def get_user_role_from_data(user_data: Optional[Dict]) -> Optional[UserRole]:
    """Obtener rol de usuario desde los datos"""
    if not user_data:
        return None
    
    role_str = user_data.get('role')
    if not role_str:
        return None
    
    try:
        return UserRole(role_str)
    except ValueError:
        return None

def get_user_from_token(session_data: Optional[Dict]) -> Optional[Dict]:
    """Obtener información del usuario desde el token JWT"""
    if not session_data:
        return None
    
    access_token = session_data.get('access_token')
    if not access_token:
        return None
    
    payload = jwt_manager.verify_token(access_token)
    if not payload:
        return None
    
    return {
        'id': payload.get('user_id'),
        'username': payload.get('username'),
        'email': payload.get('email'),
        'role': payload.get('role'),
        'full_name': payload.get('full_name')
    }
