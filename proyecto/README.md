
# Proyecto Dashboards

## Descripción

Este proyecto contiene un conjunto de dashboards desarrollados en Python para la visualización y análisis de datos. El proyecto está diseñado para proporcionar herramientas de visualización modernas y dinámicas que permiten explorar datos de manera intuitiva y efectiva.

## Estructura del Proyecto

```
dashboards/
├── data/                    # Datasets y archivos de datos
├── docs/                    # Documentación del proyecto
├── src/                     # Código fuente de la aplicación
├── main.py                  # Punto de entrada de la aplicación
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Este archivo
```

## Instalación

1. Clona el repositorio
2. Instala las dependencias: `pip install -r requirements.txt`

## Ejecución

```bash

python3 -m venv venv

# Activar entorno virtual
source venv/bin/activate
# o en windows
venv\Scripts\activate.bat

# Copiar archivo de configuracion
cp .env_example .env

# Adaptar datos de .env

# Ejecutar la aplicación
python main.py
```

La aplicación estará disponible en: **http://127.0.0.1:8051**
