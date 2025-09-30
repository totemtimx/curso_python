from dash import html, dcc

def create_app_layout():
    """Crear el layout principal de la aplicación - Estrategia simplificada"""
    return html.Div([
        dcc.Location(id='url', refresh=False),
        
        # Almacenamiento de sesión y usuario
        dcc.Store(id='session-store', storage_type='session'),
        dcc.Store(id='user-store', storage_type='local'),
        
        # Timer para renovación automática de tokens (cada 10 minutos)
        dcc.Interval(
            id='refresh-token-timer',
            interval=10*60*1000,  # 10 minutos en milisegundos
            n_intervals=0
        ),
        
        # Contenedor principal que se llenará dinámicamente
        html.Div(id='main-content'),
        html.Div(id='header-container'),
        html.Div(id='sidebar-container')
    ], className='app-container', id='app-container')