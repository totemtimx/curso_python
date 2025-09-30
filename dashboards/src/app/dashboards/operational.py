from dash import html

def create_operational_dashboard():
    """Crear el dashboard operacional"""
    return html.Div([
        html.Div([
            html.H2("📊 Dashboard Operacional", className='dashboard-title'),
            html.P("Monitoreo de operaciones y eficiencia empresarial", className='dashboard-subtitle'),
            html.Div([
                html.Div([
                    html.H3("⚡ Eficiencia", className='metric-title'),
                    html.P("94.5%", className='metric-value')
                ], className='card metric-card'),
                html.Div([
                    html.H3("👥 Productividad", className='metric-title'),
                    html.P("87.3%", className='metric-value')
                ], className='card metric-card')
            ], className='metrics-grid')
        ], className='dashboard-container')
    ])
