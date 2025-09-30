from dash import html

def create_home_page():
    """Crear la página de inicio"""
    return html.Div([
        html.Div([
            html.H2("🏢 Bienvenido al Sistema BI", className='dashboard-title'),
            html.P("Sistema de Business Intelligence para análisis empresarial", className='dashboard-subtitle'),
            html.Div([
                html.Div([
                    html.H3("📈 Financiero", className='card-title'),
                    html.P("Análisis de métricas financieras y KPIs", className='card-text')
                ], className='card dashboard-card'),
                html.Div([
                    html.H3("📊 Operacional", className='card-title'),
                    html.P("Monitoreo de operaciones y eficiencia", className='card-text')
                ], className='card dashboard-card')
            ], className='dashboard-grid')
        ], className='dashboard-container')
    ])
