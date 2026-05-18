@echo off
echo ========================================
echo   DEPLOY ENCRIPTADOR DE GRADO MILITAR
echo ========================================
echo.

echo [1] Verificando Node.js...
node --version >nul 2>&1 || (echo ERROR: Node.js no esta instalado & exit /b 1)

echo [2] Verificando Firebase CLI...
firebase --version >nul 2>&1 || (echo ERROR: Firebase CLI no esta instalado & exit /b 1)

echo.
echo ========================================
echo PASO 1: Desplegar Backend (Firebase)
echo ========================================
echo.

cd backend
echo Estas seguro de desplegar las funciones? (s/n)
set /p confirm=
if /i not "%confirm%"=="s" goto skip_backend
    echo Desplegando funciones...
    firebase deploy --only functions
    if errorlevel 1 (echo ERROR al desplegar backend & exit /b 1)
:skip_backend

echo.
echo ========================================
echo PASO 2: Desplegar Frontend (Netlify)
echo ========================================
echo.

cd ..\frontend
echo Estas seguro de desplegar el frontend? (s/n)
set /p confirm2=
if /i not "%confirm2%"=="s" goto skip_frontend

    echo.
    echo Antes de continuar, edita index.html y cambia:
    echo   'MI_PROYECTO' por tu proyecto de Firebase
    echo.
    pause

    echo Desplegando a Netlify...
    netlify deploy --prod --dir=.
    if errorlevel 1 (echo ERROR al desplegar frontend & exit /b 1)

:skip_frontend

echo.
echo ========================================
echo DEPLOY COMPLETO
echo ========================================
echo.
echo Backend: https://us-central1-MI_PROYECTO.cloudfunctions.net
echo Frontend: Tu URL de Netlify
pause