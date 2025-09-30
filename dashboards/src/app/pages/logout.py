"""
Página de logout - Ocupa todo el espacio disponible
"""
from dash import html

def create_logout_page():
    """Crear la página de logout que ocupa todo el espacio"""
    return html.Div([
        html.Div([
            html.H2("Cerrando sesión...", className="text-center"),
            html.P("Has cerrado sesión exitosamente", className="text-center text-muted"),
            html.Div([
                html.A("Volver al login", href="/login", className="btn btn-primary")
            ], className="text-center mt-3")
        ], className="logout-container")
    ], className="logout-page", style={
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