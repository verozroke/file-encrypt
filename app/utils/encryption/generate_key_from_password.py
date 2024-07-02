import hashlib
import base64

def generate_key_from_password(password):
    hash = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(hash[:32])
