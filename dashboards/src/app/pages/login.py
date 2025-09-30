"""
Página de login - Ocupa todo el espacio disponible
"""
from dash import html, dcc, Input, Output, State, callback_context
import dash_bootstrap_components as dbc

def create_login_page():
    """Crear la página de login que ocupa todo el espacio"""
    return html.Div([
        # Contenedor principal del login que ocupa toda la pantalla
        html.Div([
            # Logo o título
            html.Div([
                html.H1("Dashboard Empresarial", className="login-title"),
                html.P("Inicia sesión para acceder al sistema", className="login-subtitle")
            ], className="login-header"),
            
            # Formulario de login
            dbc.Card([
                dbc.CardBody([
                    html.H4("Iniciar Sesión", className="card-title mb-4"),
                    
                    # Formulario
                    dbc.Form([
                        # Campo de usuario
                        dbc.Row([
                            dbc.Label("Usuario", html_for="username-input", className="form-label"),
                            dbc.Input(
                                id="username-input",
                                type="text",
                                placeholder="Ingresa tu usuario",
                                className="form-control"
                            )
                        ], className="mb-3"),
                        
                        # Campo de contraseña
                        dbc.Row([
                            dbc.Label("Contraseña", html_for="password-input", className="form-label"),
                            dbc.Input(
                                id="password-input",
                                type="password",
                                placeholder="Ingresa tu contraseña",
                                className="form-control"
                            )
                        ], className="mb-3"),
                        
                        # Botón de login
                        dbc.Row([
                            dbc.Button(
                                "Iniciar Sesión",
                                id="login-button",
                                color="primary",
                                className="w-100",
                                type="submit"
                            )
                        ]),
                        
                        # Mensaje de error
                        html.Div(id="login-error", className="mt-3")
                        
                    ], id="login-form")
                ])
            ], className="login-card"),
            
            # Información de usuarios de prueba
            html.Div([
                html.H5("Usuarios de Prueba", className="mb-3"),
                html.Div([
                    html.Div([
                        html.Strong("Admin: "),
                        html.Span("admin / admin123", className="text-muted")
                    ], className="mb-2"),
                    html.Div([
                        html.Strong("Manager: "),
                        html.Span("manager / manager123", className="text-muted")
                    ], className="mb-2"),
                    html.Div([
                        html.Strong("Analyst: "),
                        html.Span("analyst / analyst123", className="text-muted")
                    ], className="mb-2"),
                    html.Div([
                        html.Strong("Viewer: "),
                        html.Span("viewer / viewer123", className="text-muted")
                    ])
                ], className="user-info")
            ], className="login-info mt-4")
            
        ], className="login-container")
    ], className="login-page", style={
        'position': 'fixed',
        'top': 0,
        'left': 0,
        'width': '100%',
        'height': '100%',
        'background': 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
        'display': 'flex',
        'align-items': 'center',
        'justify-content': 'center',
        'z-index': 9999
    })