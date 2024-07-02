from cryptography.hazmat.primitives import serialization  # type: ignore

def load_rsa_key(path, is_private=False):
    with open(path, 'rb') as file:
        key_data = file.read()
        if is_private:
            return serialization.load_pem_private_key(key_data, password=None)
        else:
            return serialization.load_pem_public_key(key_data)
