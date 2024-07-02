from cryptography.hazmat.primitives.asymmetric import padding  # type: ignore
from cryptography.hazmat.primitives import hashes  # type: ignore

def encrypt_with_public_key(data, public_key):
    return public_key.encrypt(
        data,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
