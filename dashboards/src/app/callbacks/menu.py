from dash import callback, Input, Output

def register_menu_callbacks(app):
    """Registrar callbacks del menú"""
    
    @app.callback(
        [Output('sidebar', 'className'),
         Output('main-content', 'className')],
        Input('menu-toggle', 'n_clicks')
    )
    def toggle_menu(n_clicks):
        if n_clicks is None:
            n_clicks = 0
        
        # Toggle del menú: par = visible, impar = oculto
        if n_clicks % 2 == 0:  # Menú visible
            sidebar_class = 'sidebar'
            content_class = 'main-content'
        else:  # Menú oculto
            sidebar_class = 'sidebar mobile-hidden'
            content_class = 'main-content mobile-full'
        
        return sidebar_class, content_class
