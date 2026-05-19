# PROPUESTA COMERCIAL

---

## ENCRIPTADOR DE GRADO MILITAR

**Protección de archivos con estándares de seguridad militar**

---

<p align="center">
  <img src="frontend/logo.svg" alt="Logo" width="80">
</p>

<p align="center">
  <strong>Desarrollado por GUARNIERI NETWORK</strong>
</p>

<p align="center">
  2026
</p>

---

# 1. RESUMEN EJECUTIVO

En un mundo donde la información sensible está constantemente expuesta a amenazas cibernéticas, la protección de datos personales y empresariales se ha convertido en una necesidad crítica. Cada día, miles de archivos confidenciales son comprometidos por falta de herramientas accesibles y efectivas de encriptación.

**El Problema:** Las soluciones de encriptación existentes en el mercado son demasiado complejas para el usuario común, requieren instalaciones complicadas, o tienen costos prohibitivos. Las alternativas gratuitas suelen comprometer la seguridad o carecen de funcionalidades esenciales.

**Nuestra Solución:** El Encriptador de Grado Militar es una aplicación web que proporciona protección de nivel militar de forma accesible, intuitiva y económica. Con solo arrastrar un archivo e ingresar una contraseña, cualquier usuario puede proteger sus datos con la misma tecnología utilizada por instituciones gubernamentales y fuerzas militares.

**Propuesta de Valor:** Seguridad de grado militar accesible para todos, sin instalaciones, sin conocimientos técnicos previos, y a una fracción del costo de las alternativas comerciales.

---

# 2. NUESTRA SOLUCIÓN

## Características Principales

### Interfaz Intuitiva
- Sistema de arrastrar y soltar (drag & drop)
- Diseño moderno y responsivo
- Funciona en cualquier navegador web
- Sin necesidad de instalar software

### Encriptación de Grado Militar
- Algoritmo **XChaCha20-Poly1305** (256 bits)
- Clave derivada con **PBKDF2** (10,000 iteraciones)
- Nonce de 192 bits para máxima seguridad
- Autenticación integrada (Poly1305)

### Compresión Integrada
- Tecnología **Zstandard** nivel 6
- Reduce el tamaño de los archivos antes de encriptar
- Proceso transparente para el usuario

### Formato Universal
- Extensión de archivo: **.enc**
- Compatible con cualquier tipo de archivo
- Portabilidad total

## Ventajas Diferenciadoras

| Característica | Encriptador de Grado Militar | Competidores |
|----------------|------------------------------|--------------|
| Algoritmo | XChaCha20-Poly1305 | AES-256 |
| Compresión | Incluida (Zstandard) | No incluye |
| Instalación | No requiere | Required |
| Costo | Accesible | Alto |
| Uso | Navegador web | Software local |

---

# 3. MODELO DE NEGOCIO

## Planes de Servicio

### PLAN BÁSICO - Gratis
- Encriptación básica
- Archivos hasta 50 MB
- Interfaz web completa
- Ideal para uso personal

### PLAN PROFESIONAL - $4.99/mes
- Archivos hasta 500 MB
- Prioridad de procesamiento
- Soporte técnico por email
- Ideal para profesionales y pequeñas empresas

### PLAN EMPRESARIAL - $14.99/mes
- Archivos ilimitados
- Soporte prioritario 24/7
- API para integración
- Licenciasmulti-usuario
- Ideal para empresas

## Garantía de Seguridad

- **Contraseña no se almacena**: La clave se deriva en tiempo real
- **Fallback si es incorrecta**: La desencriptación falla si la contraseña es errónea
- **Zero Knowledge**: Solo el usuario conoce su contraseña

---

# 4. CARACTERÍSTICAS TÉCNICAS

## Stack Tecnológico

| Componente | Tecnología |
|------------|------------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | Python (Flask) |
| Encriptación | XChaCha20-Poly1305 (PyNaCl) |
| Compresión | Zstandard |
| Derivación de clave | PBKDF2-SHA256 |

## Formato del Archivo Encriptado

```
[24 bytes: Nonce][16 bytes: Tag][Datos comprimidos y encriptados]
```

- **Nonce**: Vector único de 24 bytes por archivo
- **Tag**: Autenticación Poly1305 de 16 bytes
- **Datos**: Archivo original comprimido y encriptado

## Despliegue

- Frontend: Netlify (CDN global)
- Backend: Render (infraestructura escalable)
- Costo de operación: Minimizado

---

# 5. CONCLUSIÓN

El Encriptador de Grado Militar representa una oportunidad única en el mercado de seguridad de archivos. Mientras que los competidores ofrecen soluciones complejas y costosas, nuestra propuesta combina:

- **Tecnología más moderna** (XChaCha20-Poly1305 vs AES-256)
- **Compresión integrada** (ahorro de espacio)
- **Accesibilidad** (interfaz web sin instalación)
- **Precio competitivo** (planes accesibles)

**Llamado a la Acción:**

¿Interesado en proteger sus archivos con tecnología de grado militar?

Contáctenos para una demostración personalizada:

**GUARNIERI NETWORK**
- Email: [correo electrónico]
- Web: [URL de la aplicación]

---

*Este documento es confidencial y está destinado únicamente al destinatario indicado.*