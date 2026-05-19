import os
import tempfile
from flask import Flask, request, send_file, jsonify, make_response
import crypto

app = Flask(__name__)


@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response


@app.route('/encrypt', methods=['OPTIONS'])
@app.route('/decrypt', methods=['OPTIONS'])
def handle_options():
    return make_response('', 204)


@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "service": "encrypt-military-grade"})


@app.route('/encrypt', methods=['POST'])
def encrypt_file():
    if 'file' not in request.files:
        return jsonify({"error": "No se proporcionó archivo"}), 400

    file = request.files['file']
    password = request.form.get('password', '')

    if not password:
        return jsonify({"error": "La contraseña es requerida"}), 400

    if len(password) < 8:
        return jsonify({"error": "La contraseña debe tener al menos 8 caracteres"}), 400

    try:
        file_content = file.read()
        encrypted = crypto.encrypt_file(file_content, password)

        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.enc')
        temp_file.write(encrypted)
        temp_file.close()

        filename = f"{file.filename}.enc"

        return send_file(
            temp_file.name,
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({"error": f"Error al encriptar: {str(e)}"}), 500


@app.route('/decrypt', methods=['POST'])
def decrypt_file():
    if 'file' not in request.files:
        return jsonify({"error": "No se proporcionó archivo"}), 400

    file = request.files['file']
    password = request.form.get('password', '')

    if not password:
        return jsonify({"error": "La contraseña es requerida"}), 400

    try:
        file_content = file.read()
        decrypted = crypto.decrypt_file(file_content, password)

        temp_file = tempfile.NamedTemporaryFile(delete=False)
        temp_file.write(decrypted)
        temp_file.close()

        filename = file.filename
        if filename.endswith('.enc'):
            filename = filename[:-4]
        else:
            filename = f"decrypted_{filename}"

        return send_file(
            temp_file.name,
            mimetype='application/octet-stream',
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({"error": "Contraseña incorrecta o archivo corrupto"}), 400


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)