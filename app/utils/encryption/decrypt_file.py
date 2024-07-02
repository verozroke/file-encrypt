from cryptography.fernet import Fernet  # type: ignore

def decrypt_file(file_path, key):
    fernet = Fernet(key)
    with open(file_path, 'rb') as file:
        encrypted = file.read()
    decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as file:
        file.write(decrypted)
