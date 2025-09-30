# Migración a JWT para Múltiples Instancias

## Resumen de Cambios

Se ha migrado el sistema de autenticación de sesiones en memoria a JWT (JSON Web Tokens) para soportar múltiples instancias de la aplicación detrás de nginx con balanceador de carga.

## Problemas Resueltos

### 1. **Sesiones en Memoria**
- **Problema**: Cada instancia tenía su propio almacén de sesiones
- **Solución**: JWT stateless que funciona en cualquier instancia

### 2. **Escalabilidad**
- **Problema**: Usuarios autenticados en instancia A no eran reconocidos en instancia B
- **Solución**: Tokens JWT portables entre instancias

### 3. **Pérdida de Sesiones**
- **Problema**: Reinicio de instancia perdía todas las sesiones
- **Solución**: Tokens JWT persisten en el cliente

## Arquitectura JWT

### Componentes Principales

1. **JWTManager** (`src/auth/jwt_manager.py`)
   - Creación y verificación de tokens
   - Gestión de blacklist
   - Renovación de tokens

2. **TokenStorage** (`src/auth/token_storage.py`)
   - Almacenamiento en Redis para múltiples instancias
   - Blacklist distribuida
   - Limpieza automática

3. **Middleware Actualizado** (`src/auth/middleware.py`)
   - Verificación JWT en lugar de sesiones
   - Validación de roles desde token

### Flujo de Autenticación

```
1. Usuario ingresa credenciales
2. Sistema valida credenciales
3. Se crean tokens JWT (access + refresh)
4. Tokens se almacenan en sessionStorage
5. Cada request valida el token JWT
6. Tokens se renuevan automáticamente
```

## Configuración

### Variables de Entorno

```bash
# JWT Configuration
JWT_SECRET_KEY=your-secret-key-change-in-production
JWT_ALGORITHM=HS256
JWT_ACCESS_TOKEN_EXPIRY=900  # 15 minutos
JWT_REFRESH_TOKEN_EXPIRY=604800  # 7 días

# Redis Configuration (opcional)
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
REDIS_PASSWORD=
```

### Instalación de Dependencias

```bash
pip install PyJWT redis
```

## Características de Seguridad

### 1. **Tokens de Corta Duración**
- Access Token: 15 minutos
- Refresh Token: 7 días
- Renovación automática

### 2. **Blacklist de Tokens**
- Tokens invalidados se marcan como usados
- Soporte para Redis distribuido
- Limpieza automática de tokens expirados

### 3. **Validación Robusta**
- Verificación de firma digital
- Validación de expiración
- Verificación de tipo de token

## Ventajas del Nuevo Sistema

### 1. **Escalabilidad**
- ✅ Funciona con múltiples instancias
- ✅ No requiere estado compartido
- ✅ Balanceador de carga transparente

### 2. **Rendimiento**
- ✅ Validación local de tokens
- ✅ No requiere consultas a base de datos
- ✅ Menos latencia

### 3. **Seguridad**
- ✅ Tokens firmados digitalmente
- ✅ Expiración automática
- ✅ Blacklist para invalidación

### 4. **Mantenibilidad**
- ✅ Código más limpio
- ✅ Menos dependencias de estado
- ✅ Fácil debugging

## Migración Gradual

### Fase 1: Implementación JWT ✅
- [x] Crear JWTManager
- [x] Actualizar middleware
- [x] Modificar callbacks de autenticación

### Fase 2: Testing y Validación
- [ ] Probar con múltiples instancias
- [ ] Validar renovación de tokens
- [ ] Verificar blacklist

### Fase 3: Producción
- [ ] Configurar Redis
- [ ] Variables de entorno de producción
- [ ] Monitoreo de tokens

## Consideraciones de Producción

### 1. **Clave Secreta**
- Usar clave fuerte y única
- Rotar periódicamente
- Almacenar de forma segura

### 2. **Redis**
- Configurar persistencia
- Monitorear memoria
- Backup de configuración

### 3. **Monitoreo**
- Logs de autenticación
- Métricas de tokens
- Alertas de seguridad

## Troubleshooting

### Problemas Comunes

1. **Token Expirado**
   - Verificar configuración de expiración
   - Revisar renovación automática

2. **Redis No Disponible**
   - Sistema funciona sin Redis
   - Blacklist local como fallback

3. **Tokens No Válidos**
   - Verificar clave secreta
   - Revisar algoritmo de firma

## Próximos Pasos

1. **Testing Exhaustivo**
   - Probar con múltiples instancias
   - Simular fallos de red
   - Validar casos edge

2. **Optimizaciones**
   - Cache de validaciones
   - Compresión de tokens
   - Métricas avanzadas

3. **Documentación**
   - Guías de deployment
   - Troubleshooting avanzado
   - Mejores prácticas
