from dash import html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

def layout():
    """Layout de la página dashboard"""
    
    # Datos de ejemplo
    df = pd.DataFrame({
        'Mes': ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun'],
        'Ventas': [4500, 5200, 4800, 6100, 5900, 6800],
        'Gastos': [3200, 3400, 3100, 3800, 3600, 4000]
    })
    
    fig = px.bar(df, x='Mes', y=['Ventas', 'Gastos'], 
                 title='Ventas vs Gastos Mensuales',
                 barmode='group')
    
    return dbc.Container([
        dbc.Row([
            dbc.Col([
                html.H1("Dashboard", className="text-center mt-4"),
                html.Hr(),
            ], width=12)
        ]),
        
        # Tarjetas con métricas
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Ventas Totales", className="card-title"),
                        html.H2("$33,300", className="text-primary"),
                        html.P("↑ 12% vs mes anterior", className="text-success")
                    ])
                ])
            ], width=12, md=4),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Gastos Totales", className="card-title"),
                        html.H2("$21,100", className="text-primary"),
                        html.P("↑ 8% vs mes anterior", className="text-warning")
                    ])
                ])
            ], width=12, md=4),
            
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H4("Ganancia", className="card-title"),
                        html.H2("$12,200", className="text-primary"),
                        html.P("↑ 15% vs mes anterior", className="text-success")
                    ])
                ])
            ], width=12, md=4),
        ], className="mb-4"),
        
        # Gráfica
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        dcc.Graph(figure=fig)
                    ])
                ])
            ], width=12)
        ])
    ], fluid=True)