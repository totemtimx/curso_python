import dash
import dash_bootstrap_components as dbc
from src.app.layout.layout import create_app_layout
from src.app.callbacks.menu import register_menu_callbacks
from src.app.callbacks.navigation import register_navigation_callbacks
from src.app.callbacks.auth import register_auth_callbacks
# Los callbacks de login y logout ahora están en register_auth_callbacks

# Crear la aplicación Dash con Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

# Configurar archivos estáticos
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True

# Configurar el template HTML con archivos CSS externos
app.index_string = '''
<!DOCTYPE html>
<html lang="es">
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <!-- Archivos CSS externos -->
        <link rel="stylesheet" href="/static/css/themes.css">
        <link rel="stylesheet" href="/static/css/main.css">
        <link rel="stylesheet" href="/static/css/components.css">
        <link rel="stylesheet" href="/static/css/responsive.css">
        <!-- JavaScript personalizado -->
        <script src="/static/js/custom.js" defer></script>
        <!-- Meta tags para responsividad -->
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="Dashboard empresarial con Dash y Python">
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# Configurar el layout de la aplicación
app.layout = create_app_layout()

# Registrar callbacks
register_menu_callbacks(app)
register_navigation_callbacks(app)
register_auth_callbacks(app)  # Incluye callbacks de login y logout

if __name__ == '__main__':
    app.run(debug=True, port=8051)
