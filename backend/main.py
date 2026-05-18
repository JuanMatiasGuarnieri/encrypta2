import io
import os
from pathlib import Path
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import tempfile
import crypto

app = FastAPI(title="Encriptador de Grado Militar", version="1.0.0")

FRONTEND_DIR = Path(__file__).parent.parent / "frontend"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def serve_frontend():
    index_path = FRONTEND_DIR / "index.html"
    return FileResponse(index_path, media_type="text/html")


@app.get("/health")
async def health_check():
    return {"status": "ok", "service": "encrypt-military-grade"}


@app.post("/encrypt")
async def encrypt_file(
    file: UploadFile = File(...),
    password: str = Form(...)
):
    if not password:
        raise HTTPException(status_code=400, detail="La contraseña es requerida")

    if len(password) < 8:
        raise HTTPException(status_code=400, detail="La contraseña debe tener al menos 8 caracteres")

    try:
        temp_input = tempfile.NamedTemporaryFile(delete=False)
        temp_output = tempfile.NamedTemporaryFile(delete=False)

        content = await file.read()
        temp_input.write(content)
        temp_input.close()

        with open(temp_input.name, 'rb') as fin:
            with open(temp_output.name, 'wb') as fout:
                crypto.encrypt_file_chunked(fin, fout, password, file.filename)

        original_name = file.filename
        encrypted_name = f"{original_name}.enc"

        return FileResponse(
            temp_output.name,
            media_type="application/octet-stream",
            filename=encrypted_name,
            background=None
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al encriptar: {str(e)}")
    finally:
        try:
            os.unlink(temp_input.name)
        except:
            pass
        try:
            os.unlink(temp_output.name)
        except:
            pass


@app.post("/decrypt")
async def decrypt_file(
    file: UploadFile = File(...),
    password: str = Form(...)
):
    if not password:
        raise HTTPException(status_code=400, detail="La contraseña es requerida")

    try:
        temp_input = tempfile.NamedTemporaryFile(delete=False)
        temp_output = tempfile.NamedTemporaryFile(delete=False)

        content = await file.read()
        temp_input.write(content)
        temp_input.close()

        with open(temp_input.name, 'rb') as fin:
            with open(temp_output.name, 'wb') as fout:
                crypto.decrypt_file_chunked(fin, fout, password)

        original_filename = file.filename
        if original_filename.endswith('.enc'):
            decrypted_name = original_filename[:-4]
        else:
            decrypted_name = f"decrypted_{original_filename}"

        return FileResponse(
            temp_output.name,
            media_type="application/octet-stream",
            filename=decrypted_name,
            background=None
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail="Contraseña incorrecta o archivo corrupto")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)