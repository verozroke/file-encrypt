from cryptography.hazmat.primitives import serialization  # type: ignore

def save_rsa_key(key, path, is_private=False):
    with open(path, 'wb') as file:
        if is_private:
            file.write(key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            ))
        else:
            file.write(key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            ))
