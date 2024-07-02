from cryptography.fernet import Fernet  # type: ignore

def generate_key():
    return Fernet.generate_key()

def generate_key_from_password(password):
    import hashlib, base64
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash[:32])

def encrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as file:
        file.write(encrypted)

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as file:
        file.write(decrypted)
