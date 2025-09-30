"""
Configuración para servir archivos estáticos en Dash
"""
import os
from pathlib import Path

# Obtener la ruta del directorio del proyecto
PROJECT_ROOT = Path(__file__).parent
STATIC_FOLDER = PROJECT_ROOT / 'static'

def configure_static_files(app):
    """
    Configurar archivos estáticos para la aplicación Dash
    
    Args:
        app: Instancia de la aplicación Dash
    """
    # Configurar carpeta de archivos estáticos
    app.css.config.serve_locally = True
    app.scripts.config.serve_locally = True
    
    # Agregar archivos CSS externos
    external_stylesheets = [
        '/static/css/themes.css',
        '/static/css/main.css', 
        '/static/css/components.css',
        '/static/css/responsive.css'
    ]
    
    # Agregar archivos JavaScript externos
    external_scripts = [
        '/static/js/custom.js'
    ]
    
    return external_stylesheets, external_scripts

def get_static_url(path):
    """
    Obtener URL para archivo estático
    
    Args:
        path: Ruta relativa del archivo estático
        
    Returns:
        str: URL completa del archivo estático
    """
    return f'/static/{path}'

# Configuración de rutas estáticas
STATIC_ROUTES = {
    'css': '/static/css/',
    'js': '/static/js/',
    'images': '/static/assets/images/',
    'fonts': '/static/assets/fonts/'
}
