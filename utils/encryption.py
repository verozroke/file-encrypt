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

def encrypt_files(file_paths, key):
    fernet = Fernet(key)
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            original = file.read()
        encrypted = fernet.encrypt(original)
        with open(file_path, 'wb') as file:
            file.write(encrypted)

def decrypt_files(file_paths, key, key_file_path):
    fernet = Fernet(key)
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        with open(file_path, 'wb') as file:
            file.write(decrypted)
    os.remove(key_file_path)

def save_key_with_filename(key, file_paths):
    common_dir = os.path.commonpath(file_paths)
    key_file_name = f"SHA256-keys.pub"
    key_file_path = os.path.join(common_dir, key_file_name)
    save_key(key, key_file_path)
    return key_file_path
