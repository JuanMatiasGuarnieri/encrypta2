# Encriptador de Archivos de Grado Militar

Aplicación web para encriptar y desencriptar archivos utilizando estándares criptográficos de nivel militar.

## Características de Seguridad

| Capa | Tecnología | Detalles |
|------|------------|----------|
| **Cifrado** | XChaCha20-Poly1305 | Clave de 256 bits, nonce de 192 bits |
| **Derivación de clave** | PBKDF2 | 10000 iteraciones, SHA-256 |
| **Compresión** | Zstandard | Nivel 6 |
| **Autenticación** | Integrada | Tag de 16 bytes (Poly1305) |

## Estructura del Proyecto

```
encrypt_app/
├── backend/
│   ├── main.py              # API FastAPI (local)
│   ├── main_firebase.py     # Firebase Functions
│   ├── crypto.py            # Módulo de criptografía
│   ├── requirements.txt     # Dependencias Python
│   ├── firebase.json        # Config Firebase
│   └── deploy.sh            # Script de deploy (Linux/Mac)
├── frontend/
│   ├── index.html           # Interfaz web
│   ├── netlify.toml         # Config Netlify
│   └── _redirects           # Redirecciones
├── deploy.bat               # Script de deploy (Windows)
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

## Despliegue en la Nube

### Estructura Recomendada

```
┌─────────────────────────────────────────────────────────┐
│  Netlify (Frontend estático)                            │
│  https://tu-app.netlify.app                             │
│                                                         │
│         │                                               │
│         ▼                                               │
├─────────────────────────────────────────────────────────┤
│  Firebase Cloud Functions (Backend Python)              │
│  https://us-central1-TU_PROYECTO.cloudfunctions.net    │
└─────────────────────────────────────────────────────────┘
```

### Paso 1: Firebase (Backend)

1. **Instala Firebase CLI:**
   ```bash
   npm install -g firebase-tools
   ```

2. **Inicia sesión:**
   ```bash
   firebase login
   ```

3. **Crea un proyecto** en [console.firebase.google.com](https://console.firebase.google.com)

4. **Edita `.firebaserc`** y cambia `TU_PROYECTO_FIREBASE` por tu ID de proyecto:
   ```json
   {
     "projects": {
       "default": "mi-proyecto-encriptador"
     }
   }
   ```

5. **Inicializa funciones:**
   ```bash
   cd backend
   firebase init functions
   ```
   - Selecciona Python 3.12
   - Cuando pregunte por archivos existentes, selecciona Yes para sobrescribir

6. **Despliega:**
   ```bash
   firebase deploy --only functions
   ```

7. **Copia la URL** de tus funciones (algo como `https://us-central1-mi-proyecto.cloudfunctions.net`)

### Paso 2: Netlify (Frontend)

1. **Edita el frontend** para apuntar a tu Firebase:
   ```javascript
   // En frontend/index.html, línea ~353
   const API_URL = 'https://us-central1-MI_PROYECTO.cloudfunctions.net';
   ```
   Cambia `MI_PROYECTO` por tu ID de proyecto de Firebase.

2. **Sube a Netlify:**
   - Ve a [netlify.com](https://netlify.com)
   - Arrastra la carpeta `frontend/` o conecta tu repositorio
   - Netlify asignará una URL como `tu-app.netlify.app`

### O: Deploy Automático (Scripts)

```bash
# Windows
deploy.bat

# Linux/Mac
chmod +x deploy.sh
./deploy.sh
```

---

## Notas de Seguridad

- **La contraseña no se almacena en ningún momento**
- Si la contraseña es incorrecta, la desencriptación fallará
- Los archivos encriptados solo pueden ser abiertos con la contraseña correcta
- La clave se deriva usando PBKDF2 con 10000 iteraciones

## Solución de Problemas

### Error de CORS
Si el frontend no puede comunicarse con Firebase:
1. Verifica que la URL de la API sea correcta en `index.html`
2. Asegúrate de que Firebase permita conexiones desde tu dominio de Netlify

### Error al desplegar funciones
Asegúrate de tener Python 3.12 configurado en `firebase.json`

### El archivo no se descarga
Verifica que el navegador permita descargas automáticas desde dominios externos