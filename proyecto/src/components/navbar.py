import dash_bootstrap_components as dbc

def create_navbar():
    """Crea la barra de navegación"""
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Inicio", href="/")),
            dbc.NavItem(dbc.NavLink("Dashboard", href="/dashboard")),
        ],
        brand="Mi Aplicación",
        brand_href="/",
        color="primary",
        dark=True,
        className="mb-4"
    )
    return navbar