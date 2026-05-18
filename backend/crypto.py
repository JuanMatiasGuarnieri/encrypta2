import io
import os
from typing import Tuple
from nacl.secret import Aead
from nacl.utils import random
import zstandard as zstd
import hashlib


NONCE_SIZE = 24
TAG_SIZE = 16
CHUNK_SIZE = 64 * 1024 * 1024
COMPRESSION_LEVEL = 6


def derive_key(password: str) -> bytes:
    password_bytes = password.encode('utf-8')
    salt = b'ENCRIPTADOR_MILITAR_GRADO_2026'
    key = hashlib.pbkdf2_hmac('sha256', password_bytes, salt, 10000, dklen=32)
    return key


def compress_data(data: bytes) -> bytes:
    compressor = zstd.ZstdCompressor(level=COMPRESSION_LEVEL)
    return compressor.compress(data)


def decompress_data(data: bytes) -> bytes:
    dctx = zstd.ZstdDecompressor()
    dobj = dctx.decompressobj()
    return dobj.decompress(data)


def encrypt_file(file_data: bytes, password: str) -> bytes:
    key = derive_key(password)

    compressed = compress_data(file_data)

    aead = Aead(key)
    nonce = random(NONCE_SIZE)

    encrypted = aead.encrypt(compressed, nonce)

    return nonce + encrypted


def decrypt_file(encrypted_data: bytes, password: str) -> Tuple[bytes, str]:
    if len(encrypted_data) < NONCE_SIZE + TAG_SIZE:
        raise ValueError("Archivo encriptado inválido: datos insuficientes")

    key = derive_key(password)

    nonce = encrypted_data[:NONCE_SIZE]
    ciphertext = encrypted_data[NONCE_SIZE:]

    aead = Aead(key)

    decrypted_compressed = aead.decrypt(ciphertext, nonce)

    original_data = decompress_data(decrypted_compressed)

    return original_data


def encrypt_file_chunked(input_stream, output_stream, password: str, original_filename: str):
    key = derive_key(password)

    compressed_stream = io.BytesIO()
    compressor = zstd.ZstdCompressor(level=COMPRESSION_LEVEL)
    compressor.copy_stream(input_stream, compressed_stream)
    compressed_data = compressed_stream.getvalue()

    aead = Aead(key)
    nonce = random(NONCE_SIZE)

    encrypted = aead.encrypt(compressed_data, nonce)

    output_stream.write(nonce)
    output_stream.write(encrypted)


def decrypt_file_chunked(input_stream, output_stream, password: str):
    key = derive_key(password)

    input_stream.seek(0)
    file_content = input_stream.read()

    if len(file_content) < NONCE_SIZE + TAG_SIZE:
        raise ValueError("Archivo encriptado inválido")

    nonce = file_content[:NONCE_SIZE]
    ciphertext = file_content[NONCE_SIZE:]

    aead = Aead(key)

    decrypted_compressed = aead.decrypt(ciphertext, nonce)

    decompressed = decompress_data(decrypted_compressed)

    output_stream.write(decompressed)