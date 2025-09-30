"""
Gestión de usuarios y autenticación
"""
import bcrypt
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum

class UserRole(Enum):
    """Roles de usuario disponibles"""
    ADMIN = "admin"
    MANAGER = "manager"
    ANALYST = "analyst"
    VIEWER = "viewer"

@dataclass
class User:
    """Modelo de usuario"""
    id: str
    username: str
    email: str
    password_hash: str
    role: UserRole
    is_active: bool = True
    full_name: str = ""

class UserManager:
    """Gestor de usuarios en memoria (para desarrollo)"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self._create_default_users()
    
    def _create_default_users(self):
        """Crear usuarios por defecto para desarrollo"""
        default_users = [
            {
                "id": "1",
                "username": "admin",
                "email": "admin@empresa.com",
                "password": "admin123",
                "role": UserRole.ADMIN,
                "full_name": "Administrador"
            },
            {
                "id": "2", 
                "username": "manager",
                "email": "manager@empresa.com",
                "password": "manager123",
                "role": UserRole.MANAGER,
                "full_name": "Gerente"
            },
            {
                "id": "3",
                "username": "analyst",
                "email": "analyst@empresa.com", 
                "password": "analyst123",
                "role": UserRole.ANALYST,
                "full_name": "Analista"
            },
            {
                "id": "4",
                "username": "viewer",
                "email": "viewer@empresa.com",
                "password": "viewer123", 
                "role": UserRole.VIEWER,
                "full_name": "Visualizador"
            }
        ]
        
        for user_data in default_users:
            password_hash = self._hash_password(user_data["password"])
            user = User(
                id=user_data["id"],
                username=user_data["username"],
                email=user_data["email"],
                password_hash=password_hash,
                role=user_data["role"],
                full_name=user_data["full_name"]
            )
            self.users[user_data["username"]] = user
    
    def _hash_password(self, password: str) -> str:
        """Encriptar contraseña"""
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')
    
    def verify_password(self, password: str, password_hash: str) -> bool:
        """Verificar contraseña"""
        return bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))
    
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Autenticar usuario"""
        user = self.users.get(username)
        if user and user.is_active and self.verify_password(password, user.password_hash):
            return user
        return None
    
    def get_user_by_username(self, username: str) -> Optional[User]:
        """Obtener usuario por nombre de usuario"""
        return self.users.get(username)
    
    def get_user_by_id(self, user_id: str) -> Optional[User]:
        """Obtener usuario por ID"""
        for user in self.users.values():
            if user.id == user_id:
                return user
        return None
    
    def get_users_by_role(self, role: UserRole) -> List[User]:
        """Obtener usuarios por rol"""
        return [user for user in self.users.values() if user.role == role]
    
    def has_permission(self, user: User, required_role: UserRole) -> bool:
        """Verificar si el usuario tiene permisos para un rol específico"""
        role_hierarchy = {
            UserRole.VIEWER: 1,
            UserRole.ANALYST: 2, 
            UserRole.MANAGER: 3,
            UserRole.ADMIN: 4
        }
        
        user_level = role_hierarchy.get(user.role, 0)
        required_level = role_hierarchy.get(required_role, 0)
        
        return user_level >= required_level

# Instancia global del gestor de usuarios
user_manager = UserManager()
