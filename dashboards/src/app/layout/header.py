from dash import html, dcc

def create_header():
    """Crear el header empresarial responsivo"""
    return html.Header([
        html.Div([
            # Lado izquierdo: Botón menú y título
            html.Div([
                # Botón para ocultar/mostrar menú
                html.Button([
                    html.Span('☰', style={'fontSize': '20px'})
                ], id='menu-toggle', n_clicks=0, className='menu-toggle'),
                
                # Título
                html.H1("Dashboards", className='header-title')
            ], className='header-left'),
            
            # Lado derecho: Menú de usuario
            html.Div([
                # Menú desplegable de usuario
                html.Div([
                    # Botón del menú de usuario
                    html.Button([
                        html.Span('👤', className='user-icon'),
                        html.Span(id='user-info', className='user-name'),
                        html.Span('▼', className='dropdown-arrow')
                    ], id='user-menu-toggle', className='user-menu-button'),
                    
                    # Menú desplegable
                    html.Div([
                        html.Div([
                            html.Span('👤', className='menu-icon'),
                            html.Span('Perfil', className='menu-text')
                        ], className='user-menu-item'),
                        
                        html.Div([
                            html.Span('⚙️', className='menu-icon'),
                            html.Span('Configuración', className='menu-text')
                        ], className='user-menu-item'),
                        
                        html.Div([
                            html.Span('❓', className='menu-icon'),
                            html.Span('Ayuda', className='menu-text')
                        ], className='user-menu-item'),
                        
                        html.Div([
                            html.Span('', className='menu-divider')
                        ]),
                        
                        html.Button([
                            html.Span('🚪', className='menu-icon'),
                            html.Span('Cerrar Sesión', className='menu-text')
                        ], id='logout-button', className='user-menu-item logout-item')
                    ], id='user-menu-dropdown', className='user-menu-dropdown')
                ], className='user-menu-container')
            ], className='header-right')
        ], className='header-content')
    ], className='header')
