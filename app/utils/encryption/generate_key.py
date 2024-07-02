from cryptography.fernet import Fernet  # type: ignore

def generate_key():
    return Fernet.generate_key()
