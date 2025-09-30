from dash import html

def create_financial_dashboard():
    """Crear el dashboard financiero"""
    return html.Div([
        html.Div([
            html.H2("📈 Dashboard Financiero", className='dashboard-title'),
            html.P("Análisis de métricas financieras y KPIs empresariales", className='dashboard-subtitle'),
            html.Div([
                html.Div([
                    html.H3("💰 Ingresos", className='metric-title'),
                    html.P("$2.5M", className='metric-value')
                ], className='card metric-card'),
                html.Div([
                    html.H3("📊 KPIs", className='metric-title'),
                    html.P("15.2%", className='metric-value')
                ], className='card metric-card')
            ], className='metrics-grid')
        ], className='dashboard-container')
    ])
