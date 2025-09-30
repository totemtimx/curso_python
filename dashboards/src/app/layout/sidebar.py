from dash import html, dcc
from src.auth.user_manager import UserRole

def create_sidebar():
    """Crear el menú lateral vertical responsivo"""
    return html.Div([
        html.Div([
            html.Div([
                
                # Enlaces basados en roles
                html.Div([
                    # Enlaces básicos (todos los usuarios)
                    dcc.Link([
                        html.Span('🏠', className='sidebar-link-icon'),
                        html.Span('Inicio', className='sidebar-link-text')
                    ], href='/', id='nav-home', className='sidebar-link'),

                    # Dashboard Financiero (Manager, Admin, Analyst)
                    dcc.Link([
                        html.Span('📈', className='sidebar-link-icon'),
                        html.Span('Dashboard Financiero', className='sidebar-link-text')
                    ], href='/dashboard1', id='nav-financial', className='sidebar-link'),
                    
                    # Dashboard Operacional (Manager, Admin, Analyst)
                    dcc.Link([
                        html.Span('📊', className='sidebar-link-icon'),
                        html.Span('Dashboard Operacional', className='sidebar-link-text')
                    ], href='/dashboard2', id='nav-operational', className='sidebar-link'),
                    
                    # Gestión de usuarios (solo Admin)
                    dcc.Link([
                        html.Span('👥', className='sidebar-link-icon'),
                        html.Span('Gestión de Usuarios', className='sidebar-link-text')
                    ], href='/users', id='nav-users', className='sidebar-link'),
                    
                    # Reportes avanzados (solo Manager y Admin)
                    dcc.Link([
                        html.Span('📋', className='sidebar-link-icon'),
                        html.Span('Reportes Avanzados', className='sidebar-link-text')
                    ], href='/reports', id='nav-reports', className='sidebar-link')
                ], className='sidebar-nav')
            ], className='sidebar-nav')
        ], className='sidebar-content')
    ], id='sidebar', className='sidebar')
