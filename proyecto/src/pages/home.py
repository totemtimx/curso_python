from dash import html
import dash_bootstrap_components as dbc

def layout():
    """Layout de la página de inicio"""
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Bienvenido", className="text-center mt-4"),
                html.Hr(),
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Página de Inicio", className="card-title"),
                        html.P(
                            "Esta es una aplicación de ejemplo con múltiples páginas "
                            "usando Dash y Bootstrap Components.",
                            className="card-text"
                        ),
                        html.P(
                            "Utiliza el menú de navegación superior para moverte "
                            "entre las diferentes páginas.",
                            className="card-text"
                        ),
                        dbc.Button("Ir al Dashboard", href="/dashboard", color="primary")
                    ])
                ], className="mt-4")
            ], width=12, lg=8, className="mx-auto")
        ])
    ], fluid=True)