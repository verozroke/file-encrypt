from utils.biometric.capture_face import capture_face
from utils.encryption import generate_key, encrypt_file
from utils.encryption.key_management.save_key import save_key
from utils.metadata.store_metadata import save_metadata

def encrypt_with_biometric(file_path, username):
    face_file = capture_face(username)
    key = generate_key()
    key_path = f"{file_path}.pub"
    save_key(key, key_path)
    encrypt_file(file_path, key)

    metadata = {
        "username": username,
        "face_file": face_file,
        "file_path": file_path
    }

    save_metadata(file_path, metadata)
