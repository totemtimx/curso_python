# Archivos Estáticos - Dashboard

Esta carpeta contiene todos los archivos estáticos (CSS, JavaScript, imágenes, fuentes) del dashboard.

## Estructura de Archivos

```
static/
├── css/
│   ├── themes.css        # Variables CSS y colores corporativos
│   ├── main.css          # Estilos base y reset
│   ├── components.css    # Estilos de componentes específicos
│   └── responsive.css    # Media queries y responsividad
├── js/
│   └── custom.js         # JavaScript personalizado
└── assets/
    ├── images/          # Imágenes del dashboard
    └── fonts/           # Fuentes personalizadas
```

## Descripción de Archivos

### CSS

#### `themes.css`
- Variables CSS para colores corporativos
- Configuración de espaciado, bordes y sombras
- Soporte para temas (claro/oscuro)
- Variables para tipografía y z-index

#### `main.css`
- Reset CSS y estilos base
- Estilos del header
- Utilidades generales
- Animaciones básicas

#### `components.css`
- Estilos del sidebar
- Componentes de navegación
- Cards y contenedores
- Botones y alertas
- Overlay para móviles

#### `responsive.css`
- Media queries para diferentes tamaños de pantalla
- Estilos específicos para móviles, tablets y desktop
- Soporte para orientación landscape
- Estilos de impresión
- Accesibilidad (alto contraste, movimiento reducido)

### JavaScript

#### `custom.js`
- Funcionalidad del menú móvil
- Manejo de navegación activa
- Animaciones suaves
- Atajos de teclado
- Mejoras de accesibilidad
- Manejo de errores

## Mejores Prácticas Implementadas

### 1. **Separación de Responsabilidades**
- CSS: Solo estilos y diseño
- JavaScript: Solo funcionalidad interactiva
- Python: Solo lógica de negocio

### 2. **Organización Modular**
- Archivos CSS separados por funcionalidad
- Variables CSS centralizadas
- Componentes reutilizables

### 3. **Responsividad**
- Mobile-first approach
- Breakpoints bien definidos
- Soporte para diferentes dispositivos

### 4. **Accesibilidad**
- Atributos ARIA
- Soporte para teclado
- Alto contraste
- Movimiento reducido

### 5. **Performance**
- CSS optimizado
- JavaScript con defer
- Precarga de recursos críticos

## Uso

Los archivos se cargan automáticamente en el template HTML de Dash. No es necesario modificar el código Python para usar estos estilos.

### Agregar Nuevos Estilos

1. **Para estilos globales**: Editar `main.css`
2. **Para componentes**: Editar `components.css`
3. **Para responsividad**: Editar `responsive.css`
4. **Para variables**: Editar `themes.css`

### Agregar Nueva Funcionalidad JavaScript

1. Editar `custom.js`
2. Agregar la funcionalidad en la función `init()`
3. Exportar funciones globales si es necesario

## Variables CSS Disponibles

### Colores
```css
--primary-color: #1e3a8a
--secondary-color: #64748b
--accent-color: #0ea5e9
--background-color: #f8fafc
--white: #ffffff
--text-dark: #1e293b
--text-light: #64748b
```

### Espaciado
```css
--spacing-xs: 8px
--spacing-sm: 12px
--spacing-md: 16px
--spacing-lg: 20px
--spacing-xl: 24px
```

### Transiciones
```css
--transition-fast: 0.15s ease
--transition-normal: 0.3s ease
--transition-slow: 0.5s ease
```

## Clases CSS Disponibles

### Layout
- `.app-container` - Contenedor principal
- `.page-content` - Contenido de la página
- `.sidebar` - Menú lateral
- `.header` - Encabezado

### Componentes
- `.card` - Tarjetas de contenido
- `.btn` - Botones
- `.alert` - Alertas
- `.sidebar-link` - Enlaces del menú

### Utilidades
- `.hidden` - Ocultar elemento
- `.visible` - Mostrar elemento
- `.fade-in` - Animación de entrada
- `.slide-in` - Animación de deslizamiento
