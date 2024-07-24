from app.utils.biometric.capture_face import capture_face
from app.utils.encryption.generate_key import generate_key
from app.utils.encryption.encrypt_file import encrypt_file
from app.utils.encryption.key_management.save_key import save_key
from app.utils.metadata.store_metadata import save_metadata

def execute(file_paths, username):
    for file_path in file_paths:
        encrypt_with_biometric(file_path, username)

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
