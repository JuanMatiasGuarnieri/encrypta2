#!/bin/bash
echo "========================================"
echo "  DEPLOY ENCRIPTADOR DE GRADO MILITAR"
echo "========================================"
echo ""

echo "[1] Verificando Node.js..."
if ! command -v node &> /dev/null; then
    echo "ERROR: Node.js no esta instalado"
    exit 1
fi
node --version

echo "[2] Verificando Firebase CLI..."
if ! command -v firebase &> /dev/null; then
    echo "ERROR: Firebase CLI no esta instalado"
    exit 1
fi
firebase --version

echo ""
echo "========================================"
echo "PASO 1: Desplegar Backend (Firebase)"
echo "========================================"
echo ""
read -p "Desplegar funciones a Firebase? (s/n): " confirm
if [ "$confirm" = "s" ]; then
    cd backend
    firebase deploy --only functions
    cd ..
fi

echo ""
echo "========================================"
echo "PASO 2: Desplegar Frontend (Netlify)"
echo "========================================"
echo ""
read -p "Desplegar frontend a Netlify? (s/n): " confirm2
if [ "$confirm2" = "s" ]; then
    echo ""
    echo "Antes de continuar, edita frontend/index.html y cambia:"
    echo "  'MI_PROYECTO' por tu proyecto de Firebase"
    echo ""
    read -p "Presiona enter cuando estes listo..."

    cd frontend
    netlify deploy --prod --dir=.
    cd ..
fi

echo ""
echo "========================================"
echo "DEPLOY COMPLETO"
echo "========================================"
echo ""
echo "Backend: https://us-central1-MI_PROYECTO.cloudfunctions.net"
echo "Frontend: Tu URL de Netlify"