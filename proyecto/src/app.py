import dash
import dash_bootstrap_components as dbc

# Inicializar la aplicación
app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True
)

server = app.server  # Para deployment