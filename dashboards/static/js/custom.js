// JavaScript personalizado para funcionalidad del dashboard
document.addEventListener('DOMContentLoaded', function() {
    // Variables globales - se inicializarán cuando estén disponibles
    let menuToggle = null;
    let sidebar = null;
    let pageContent = null;
    let userMenuToggle = null;
    let userMenuDropdown = null;
    let sidebarOverlay = null;
    
    // Función para obtener elementos del DOM
    function getElements() {
        menuToggle = document.getElementById('menu-toggle');
        sidebar = document.getElementById('sidebar');
        pageContent = document.getElementById('page-content');
        userMenuToggle = document.getElementById('user-menu-toggle');
        userMenuDropdown = document.getElementById('user-menu-dropdown');
        
    }
    
    // Crear overlay para móviles si no existe
    function createSidebarOverlay() {
        if (!sidebarOverlay) {
            sidebarOverlay = document.createElement('div');
            sidebarOverlay.className = 'sidebar-overlay';
            sidebarOverlay.id = 'sidebar-overlay';
            document.body.appendChild(sidebarOverlay);
        }
        return sidebarOverlay;
    }
    
    // Función para mostrar/ocultar sidebar en móviles
    function toggleSidebar() {
        const isMobile = window.innerWidth <= 768;
        
        if (isMobile) {
            const overlay = createSidebarOverlay();
            
            if (sidebar.classList.contains('mobile-open')) {
                // Cerrar sidebar
                sidebar.classList.remove('mobile-open');
                overlay.classList.remove('show');
                document.body.style.overflow = '';
            } else {
                // Abrir sidebar
                sidebar.classList.add('mobile-open');
                overlay.classList.add('show');
                document.body.style.overflow = 'hidden';
            }
        }
    }
    
    // Función para cerrar sidebar al hacer clic en overlay
    function closeSidebarOnOverlay() {
        if (sidebarOverlay) {
            sidebarOverlay.addEventListener('click', function() {
                sidebar.classList.remove('mobile-open');
                sidebarOverlay.classList.remove('show');
                document.body.style.overflow = '';
            });
        }
    }
    
    // Función para manejar cambios de tamaño de ventana
    function handleResize() {
        const isMobile = window.innerWidth <= 768;
        
        if (!isMobile && sidebar) {
            // En desktop, asegurar que sidebar esté visible
            sidebar.classList.remove('mobile-open');
            if (sidebarOverlay) {
                sidebarOverlay.classList.remove('show');
            }
            document.body.style.overflow = '';
        }
    }
    
    // Función para manejar navegación activa
    function setActiveNavigation() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.sidebar-link');
        
        navLinks.forEach(link => {
            link.classList.remove('active');
            if (link.getAttribute('href') === currentPath) {
                link.classList.add('active');
            }
        });
    }
    
    // Función para animaciones suaves
    function addSmoothAnimations() {
        // Agregar clase de animación a elementos cuando son visibles
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        });
        
        // Observar elementos con clase 'card'
        document.querySelectorAll('.card').forEach(card => {
            observer.observe(card);
        });
    }
    
    // Función para manejar menú de usuario
    function toggleUserMenu(e) {
        e.preventDefault();
        e.stopPropagation();
        
        if (userMenuDropdown) {
            const isVisible = userMenuDropdown.classList.contains('show');
            
            if (isVisible) {
                userMenuDropdown.classList.remove('show');
            } else {
                userMenuDropdown.classList.add('show');
            }
        }
    }
    
    // Función para cerrar menú de usuario al hacer clic fuera
    function closeUserMenuOnClickOutside() {
        document.addEventListener('click', function(e) {
            if (userMenuToggle && userMenuDropdown) {
                const isClickInside = userMenuToggle.contains(e.target) || userMenuDropdown.contains(e.target);
                
                if (!isClickInside && userMenuDropdown.classList.contains('show')) {
                    userMenuDropdown.classList.remove('show');
                }
            }
        });
    }
    
    // Función para manejar teclas de acceso rápido
    function handleKeyboardShortcuts() {
        document.addEventListener('keydown', function(e) {
            // Ctrl/Cmd + M para alternar menú
            if ((e.ctrlKey || e.metaKey) && e.key === 'm') {
                e.preventDefault();
                toggleSidebar();
            }
            
            // Escape para cerrar menús
            if (e.key === 'Escape') {
                if (sidebar.classList.contains('mobile-open')) {
                    sidebar.classList.remove('mobile-open');
                    if (sidebarOverlay) {
                        sidebarOverlay.classList.remove('show');
                    }
                    document.body.style.overflow = '';
                }
                
                if (userMenuDropdown && userMenuDropdown.classList.contains('show')) {
                    userMenuDropdown.classList.remove('show');
                }
            }
        });
    }
    
    // Función para mejorar accesibilidad
    function improveAccessibility() {
        // Agregar atributos ARIA
        if (menuToggle) {
            menuToggle.setAttribute('aria-label', 'Alternar menú de navegación');
            menuToggle.setAttribute('aria-expanded', 'false');
        }
        
        if (sidebar) {
            sidebar.setAttribute('aria-label', 'Menú de navegación');
        }
        
        // Manejar cambios en aria-expanded
        if (menuToggle) {
            menuToggle.addEventListener('click', function() {
                const isExpanded = sidebar.classList.contains('mobile-open');
                menuToggle.setAttribute('aria-expanded', isExpanded.toString());
            });
        }
    }
    
    // Función para precargar recursos
    function preloadResources() {
        // Precargar imágenes críticas
        const criticalImages = [
            // Agregar aquí las rutas de imágenes críticas
        ];
        
        criticalImages.forEach(src => {
            const img = new Image();
            img.src = src;
        });
    }
    
    // Función para manejar errores de JavaScript
    function handleErrors() {
        window.addEventListener('error', function(e) {
            console.error('Error en JavaScript:', e.error);
            // Aquí podrías enviar el error a un servicio de monitoreo
        });
    }
    
    // Inicializar todas las funcionalidades
    function init() {
        // Obtener elementos del DOM
        getElements();
        
        // Event listeners
        if (menuToggle) {
            menuToggle.addEventListener('click', toggleSidebar);
        }
        
        if (userMenuToggle) {
            userMenuToggle.addEventListener('click', toggleUserMenu);
        }
        
        window.addEventListener('resize', handleResize);
        window.addEventListener('popstate', setActiveNavigation);
        
        // Inicializar funcionalidades
        setActiveNavigation();
        closeSidebarOnOverlay();
        closeUserMenuOnClickOutside();
        addSmoothAnimations();
        handleKeyboardShortcuts();
        improveAccessibility();
        preloadResources();
        handleErrors();
        
        // Configurar estado inicial
        handleResize();
    }
    
    // Ejecutar inicialización con retraso para elementos dinámicos
    setTimeout(init, 100);
    
    // También intentar inicializar después de un tiempo adicional para elementos que se cargan dinámicamente
    setTimeout(function() {
        getElements();
        if (userMenuToggle && !userMenuToggle.hasAttribute('data-listener-added')) {
            userMenuToggle.addEventListener('click', toggleUserMenu);
            userMenuToggle.setAttribute('data-listener-added', 'true');
        }
    }, 500);
    
    // Observer para detectar cambios en el DOM
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.type === 'childList') {
                // Verificar si se agregaron elementos del menú de usuario
                mutation.addedNodes.forEach(function(node) {
                    if (node.nodeType === 1) { // Element node
                        if (node.id === 'user-menu-toggle' || node.querySelector('#user-menu-toggle')) {
                            getElements();
                            if (userMenuToggle && !userMenuToggle.hasAttribute('data-listener-added')) {
                                userMenuToggle.addEventListener('click', toggleUserMenu);
                                userMenuToggle.setAttribute('data-listener-added', 'true');
                            }
                        }
                    }
                });
            }
        });
    });
    
    // Iniciar observación
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
    
    // Exportar funciones para uso global si es necesario
    window.DashboardUtils = {
        toggleSidebar,
        setActiveNavigation,
        handleResize
    };
});
