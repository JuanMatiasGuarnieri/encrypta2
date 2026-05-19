# Encriptador de Archivos de Grado Militar

Aplicación web para encriptar y desencriptar archivos utilizando estándares criptográficos de nivel militar.

<p align="center">
  <img src="frontend/logo.svg" alt="Logo Encriptador" width="100">
</p>

![Logo](https://img.shields.io/badge/Encriptación-XChaCha20--Poly1305-00d9ff)

## Características de Seguridad

| Capa | Tecnología | Detalles |
|------|------------|----------|
| **Cifrado** | XChaCha20-Poly1305 | Clave de 256 bits, nonce de 192 bits |
| **Derivación de clave** | PBKDF2 | 10000 iteraciones, SHA-256 |
| **Compresión** | Zstandard | Nivel 6 |
| **Autenticación** | Integrada | Tag de 16 bytes (Poly1305) |
| **CORS** | Headers personalizados | Compatible con despliegues externos |

## Características Visuales

- **Logo SVG**: Escudo con candado representando encriptación militar
- **Favicon**: Icono en la pestaña del navegador
- **Footer**: Marca "GUARNIERI NETWORK"
- **Diseño responsivo**: Compatible con dispositivos móviles

## Estructura del Proyecto

```
encrypt_app/
├── backend/
│   ├── main.py              # API FastAPI (local)
│   ├── main_render.py       # Flask para Render
│   ├── main_firebase.py     # Firebase Functions
│   ├── crypto.py            # Módulo de criptografía
│   ├── requirements.txt     # Dependencias Python
│   ├── render.yaml          # Config Render
│   └── firebase.json        # Config Firebase
├── frontend/
│   ├── index.html           # Interfaz web
│   ├── logo.svg              # Logo de la aplicación
│   ├── favicon.svg           # Icono de pestaña del navegador
│   ├── netlify.toml         # Config Netlify
│   └── _redirects           # Redirecciones
├── deploy.bat               # Script de deploy (Windows)
├── deploy.sh                # Script de deploy (Linux/Mac)
└── README.md
```

## Uso Local

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Accede a: `http://localhost:8080`

---

## Despliegue en la Nube (Versión Actual)

### Estructura Recomendada

```
┌─────────────────────────────────────────────────────────┐
│  Netlify (Frontend estático)                            │
│  https://tu-app.netlify.app                             │
│                                                         │
│         │                                               │
│         ▼                                               │
├─────────────────────────────────────────────────────────┤
│  Render (Backend Python - Gratis)                      │
│  https://tu-servicio.onrender.com                       │
└─────────────────────────────────────────────────────────┘
```

### Paso 1: Render (Backend)

1. Ve a [render.com](https://render.com) y crea una cuenta

2. Crea un nuevo **Web Service**:
   - Conecta tu repositorio de GitHub
   - Configura:
     - **Name**: `encriptador-backend`
     - **Region**: Oregon
     - **Root Directory**: `backend`
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `python main_render.py`

3. Despliega y copia la URL (ej: `https://tu-servicio.onrender.com`)

### Paso 2: Netlify (Frontend)

1. Edita `frontend/index.html` y configura tu URL de Render:
   ```javascript
   const API_URL = 'https://tu-servicio.onrender.com';
   ```

2. Sube la carpeta `frontend/` a Netlify:
   - Ve a [netlify.com](https://netlify.com)
   - Arrastra la carpeta `frontend/` o conecta tu repositorio

---

## Formato del Archivo Encriptado

```
[24 bytes: Nonce][16 bytes: Tag][Datos comprimidos y encriptados]
```

Extensión: `.enc`

## Notas de Seguridad

- **La contraseña no se almacena en ningún momento**
- Si la contraseña es incorrecta, la desencriptación fallará
- Los archivos encriptados solo pueden ser abiertos con la contraseña correcta
- La clave se deriva usando PBKDF2 con 10000 iteraciones
- Soporte completo para CORS en despliegues remotos

## Solución de Problemas

### Error de CORS
Si el frontend no puede comunicarse con el backend:
1. Verifica que la URL de la API sea correcta en `index.html`
2. Asegúrate de que el backend tenga headers CORS configurados

### Error al desplegar en Render
- Verifica que el `Root Directory` esté configurado como `backend`
- Asegúrate de que `requirements.txt` tenga todas las dependencias incluyendo `flask` y `flask-cors`

### El archivo no se descarga
Verifica que el navegador permita descargas automáticas desde dominios externos

---

## Tecnologías Utilizadas

- **Backend**: Python, Flask, PyNaCl, Zstandard
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Hosting**: Render (backend), Netlify (frontend)

## Licencia

MIT License

---

**Desarrollado por GUARNIERI NETWORK**