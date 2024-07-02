from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore

def decrypt_with_private_key(data, private_key):
    return private_key.decrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
