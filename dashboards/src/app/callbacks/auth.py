"""
Callbacks para autenticación - Estrategia simplificada
"""
from dash import html, dcc, Input, Output, State, no_update
from src.app.layout.header import create_header
from src.app.layout.sidebar import create_sidebar
from src.app.pages.login import create_login_page
from src.app.pages.logout import create_logout_page
from src.app.dashboards.home import create_home_page
from src.app.dashboards.financial import create_financial_dashboard
from src.app.dashboards.operational import create_operational_dashboard
from src.auth.middleware import require_auth, require_role, get_user_from_token
from src.auth.jwt_manager import jwt_manager
from src.auth.user_manager import UserRole

def register_auth_callbacks(app):
    """Registrar callbacks de autenticación con estrategia simplificada"""
    
    @app.callback(
        [Output('main-content', 'children'),
         Output('header-container', 'children'),
         Output('sidebar-container', 'children'),
         Output('session-store', 'data'),
         Output('user-store', 'data'),
         Output('url', 'pathname')],
        [Input('url', 'pathname')],
        [State('session-store', 'data'),
         State('user-store', 'data')],
        prevent_initial_call='initial_duplicate'
    )
    def handle_page_display(pathname, session_data, user_data):
        """Manejar la visualización de páginas basada en la URL y autenticación"""
        
        # Páginas públicas
        if pathname == '/login':
            return create_login_page(), "", "", session_data, user_data, '/login'
        elif pathname == '/logout':
            return create_logout_page(), "", "", session_data, user_data, '/logout'
        
        # Reconstruir datos de usuario si es necesario
        if session_data and not user_data:
            user_data = get_user_from_token(session_data)
        
        # Limpiar datos de usuario si no hay sesión válida
        if not session_data and user_data:
            user_data = None
        
        # Verificar autenticación
        if not require_auth(session_data, user_data):
            return create_login_page(), "", "", None, None, '/login'
        
        # Usuario autenticado - mostrar interfaz completa
        header = create_header()
        sidebar = create_sidebar()
        
        if pathname == '/':
            return create_home_page(), header, sidebar, session_data, user_data, '/'
        elif pathname == '/dashboard1':
            if require_role(session_data, user_data, UserRole.ANALYST):
                return create_financial_dashboard(), header, sidebar, session_data, user_data, '/dashboard1'
            else:
                return create_access_denied_page(), header, sidebar, session_data, user_data, '/dashboard1'
        elif pathname == '/dashboard2':
            if require_role(session_data, user_data, UserRole.ANALYST):
                return create_operational_dashboard(), header, sidebar, session_data, user_data, '/dashboard2'
            else:
                return create_access_denied_page(), header, sidebar, session_data, user_data, '/dashboard2'
        elif pathname == '/users':
            if require_role(session_data, user_data, UserRole.ADMIN):
                return create_users_management_page(), header, sidebar, session_data, user_data, '/users'
            else:
                return create_access_denied_page(), header, sidebar, session_data, user_data, '/users'
        elif pathname == '/reports':
            if require_role(session_data, user_data, UserRole.MANAGER):
                return create_reports_page(), header, sidebar, session_data, user_data, '/reports'
            else:
                return create_access_denied_page(), header, sidebar, session_data, user_data, '/reports'
        else:
            return create_home_page(), header, sidebar, session_data, user_data, '/'
    
    @app.callback(
        [Output('session-store', 'data', allow_duplicate=True),
         Output('user-store', 'data', allow_duplicate=True),
         Output('url', 'pathname', allow_duplicate=True)],
        [Input('login-button', 'n_clicks')],
        [State('username-input', 'value'),
         State('password-input', 'value')],
        prevent_initial_call=True
    )
    def handle_login(n_clicks, username, password):
        """Manejar login"""
        if not n_clicks:
            return no_update, no_update, no_update
        
        if not username or not password:
            return no_update, no_update, no_update
        
        # Autenticar usuario
        from src.auth.user_manager import user_manager
        user = user_manager.authenticate_user(username, password)
        
        if not user:
            return no_update, no_update, no_update
        
        # Crear tokens JWT
        token_pair = jwt_manager.create_token_pair(user)
        
        # Preparar datos de sesión
        session_data = {
            'access_token': token_pair.access_token,
            'refresh_token': token_pair.refresh_token,
            'expires_at': token_pair.expires_at.isoformat()
        }
        
        # Preparar datos de usuario
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role.value,
            'full_name': user.full_name
        }
        
        return session_data, user_data, '/'
    
    @app.callback(
        [Output('session-store', 'data', allow_duplicate=True),
         Output('user-store', 'data', allow_duplicate=True),
         Output('url', 'pathname', allow_duplicate=True)],
        [Input('logout-button', 'n_clicks')],
        [State('session-store', 'data')],
        prevent_initial_call=True
    )
    def handle_logout(n_clicks, session_data):
        """Manejar logout"""
        if not n_clicks:
            return no_update, no_update, no_update
        
        # Invalidar tokens JWT si existen
        if session_data:
            access_token = session_data.get('access_token')
            if access_token:
                jwt_manager.blacklist_token(access_token)
            
            refresh_token = session_data.get('refresh_token')
            if refresh_token:
                jwt_manager.blacklist_token(refresh_token)
        
        return None, None, '/login'
    
    @app.callback(
        Output('login-error', 'children'),
        [Input('login-button', 'n_clicks')],
        [State('username-input', 'value'),
         State('password-input', 'value')],
        prevent_initial_call=True
    )
    def handle_login_error(n_clicks, username, password):
        """Manejar errores de login"""
        if not n_clicks:
            return ""
        
        if not username or not password:
            return html.Div("Usuario y contraseña son requeridos", className="alert alert-danger")
        
        # Autenticar usuario
        from src.auth.user_manager import user_manager
        user = user_manager.authenticate_user(username, password)
        
        if not user:
            return html.Div("Credenciales inválidas", className="alert alert-danger")
        
        return ""
    
    @app.callback(
        Output('user-info', 'children'),
        [Input('user-store', 'data')]
    )
    def update_user_info(user_data):
        """Actualizar información del usuario en el header"""
        if user_data:
            role_display = {
                'admin': 'Administrador',
                'manager': 'Gerente', 
                'analyst': 'Analista',
                'viewer': 'Visualizador'
            }
            role = role_display.get(user_data.get('role', ''), 'Usuario')
            return f"{user_data.get('full_name', user_data.get('username', ''))} ({role})"
        return ""
    
    @app.callback(
        [Output('session-store', 'data', allow_duplicate=True),
         Output('user-store', 'data', allow_duplicate=True)],
        [Input('refresh-token-timer', 'n_intervals')],
        [State('session-store', 'data')],
        prevent_initial_call=True
    )
    def handle_token_refresh(n_intervals, session_data):
        """Manejar renovación automática de tokens"""
        if not session_data:
            return None, None
        
        refresh_token = session_data.get('refresh_token')
        if not refresh_token:
            return None, None
        
        # Intentar renovar tokens
        new_token_pair = jwt_manager.refresh_access_token(refresh_token)
        if new_token_pair:
            # Actualizar datos de sesión
            new_session_data = {
                'access_token': new_token_pair.access_token,
                'refresh_token': new_token_pair.refresh_token,
                'expires_at': new_token_pair.expires_at.isoformat()
            }
            
            # Obtener datos de usuario desde el nuevo token
            user_data = get_user_from_token(new_session_data)
            
            return new_session_data, user_data
        
        # Si no se puede renovar, limpiar sesión
        return None, None

def create_access_denied_page():
    """Crear página de acceso denegado"""
    return html.Div([
        html.Div([
            html.H2("Acceso Denegado", className="text-center text-danger"),
            html.P("No tienes permisos para acceder a esta página", className="text-center"),
            html.Div([
                html.A("Volver al inicio", href="/", className="btn btn-primary")
            ], className="text-center mt-3")
        ], className="access-denied-container")
    ], className="access-denied-page")

def create_users_management_page():
    """Crear página de gestión de usuarios"""
    return html.Div([
        html.H2("Gestión de Usuarios"),
        html.P("Aquí puedes gestionar los usuarios del sistema (solo administradores)"),
    ])

def create_reports_page():
    """Crear página de reportes avanzados"""
    return html.Div([
        html.H2("Reportes Avanzados"),
        html.P("Aquí puedes generar reportes avanzados (solo gerentes y administradores)"),
    ])