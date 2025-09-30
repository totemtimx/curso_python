
# Proyecto Dashboards

## Descripción

Este proyecto contiene un conjunto de dashboards desarrollados en Python para la visualización y análisis de datos. El proyecto está diseñado para proporcionar herramientas de visualización modernas y dinámicas que permiten explorar datos de manera intuitiva y efectiva.

## Estructura del Proyecto

```
dashboards/
├── data/                    # Datasets y archivos de datos
├── docs/                    # Documentación del proyecto
├── static/                  # Archivos estáticos (CSS, JS, assets)
│   ├── css/                 # Hojas de estilo
│   │   ├── themes.css       # Variables y colores corporativos
│   │   ├── main.css         # Estilos base y reset
│   │   ├── components.css   # Componentes específicos
│   │   ├── responsive.css   # Media queries y responsividad
│   │   └── examples.css     # Ejemplos de uso
│   ├── js/                  # JavaScript personalizado
│   │   └── custom.js        # Funcionalidad del dashboard
│   └── assets/              # Recursos multimedia
│       ├── images/          # Imágenes del dashboard
│       └── fonts/           # Fuentes personalizadas
├── src/                     # Código fuente de la aplicación
│   └── app/
│       ├── layout/          # Componentes de layout
│       │   ├── header.py    # Header de la aplicación
│       │   ├── sidebar.py   # Menú lateral
│       │   └── layout.py     # Layout principal
│       ├── dashboards/      # Páginas de dashboards
│       │   ├── home.py      # Página de inicio
│       │   ├── financial.py # Dashboard financiero
│       │   └── operational.py # Dashboard operacional
│       └── callbacks/       # Callbacks de Dash
│           ├── menu.py      # Callbacks del menú
│           └── navigation.py # Callbacks de navegación
├── main.py                  # Punto de entrada de la aplicación
├── static_config.py         # Configuración de archivos estáticos
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

## Arquitectura del Proyecto

### Separación de Responsabilidades
- **CSS**: Estilos y diseño en archivos separados (`static/css/`)
- **JavaScript**: Funcionalidad interactiva (`static/js/`)
- **Python**: Lógica de negocio y estructura de datos

### Organización Modular
- **Layout**: Componentes reutilizables de interfaz
- **Dashboards**: Páginas específicas de visualización
- **Callbacks**: Lógica de interacción de Dash
- **Estáticos**: Recursos multimedia y estilos

## Tecnologías Utilizadas

- **Python**: Lenguaje principal de desarrollo
- **Dash**: Framework para aplicaciones web interactivas
- **Plotly**: Para visualizaciones interactivas
- **Pandas**: Para manipulación y análisis de datos
- **CSS3**: Estilos modernos con variables CSS
- **JavaScript**: Funcionalidad interactiva del frontend

## Instalación

1. Clona el repositorio
2. Instala las dependencias: `pip install -r requirements.txt`

## Ejecución

```bash
# Activar entorno virtual
source venv/bin/activate

# Ejecutar la aplicación
python main.py
```

La aplicación estará disponible en: **http://127.0.0.1:8051**

## Características

- **Responsivo**: Adaptable a móviles, tablets y desktop
- **Modular**: Arquitectura separada por responsabilidades
- **Accesible**: Navegación por teclado y atributos ARIA
- **Moderno**: CSS3 con variables y JavaScript ES6
