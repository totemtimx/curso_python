from dash import html, dcc, Input, Output
from src.app import app
from src.components.navbar import create_navbar
from src.pages import home, dashboard

# Layout principal
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    create_navbar(),
    html.Div(id='page-content')
])

# Callback para navegación
@app.callback(
    Output('page-content', 'children'),
    Input('url', 'pathname')
)
def display_page(pathname):
    if pathname == '/dashboard':
        return dashboard.layout()
    else:
        return home.layout()

# Ejecutar servidor
if __name__ == '__main__':
    app.run(debug=True)