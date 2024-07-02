import hashlib
import base64
from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def generate_key_from_password(password):
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash[:32])

def load_key(key_file):
    with open(key_file, 'rb') as file:
        key = file.read()
    return key

def save_key(key, key_file):
    with open(key_file, 'wb') as file:
        file.write(key)

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path, key, key_file_path):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as file:
        file.write(decrypted)
    os.remove(key_file_path)

def save_key_with_filename(key, file_path):
    base_name = os.path.basename(file_path)
    file_name, _ = os.path.splitext(base_name)
    key_file_name = f"SHA256-{file_name}.pub"
    key_file_path = os.path.join(os.path.dirname(file_path), key_file_name)
    save_key(key, key_file_path)
    return key_file_path
