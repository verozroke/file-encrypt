from app.utils.biometric.recognize_face import recognize_face
from app.utils.encryption.decrypt_file import decrypt_file
from app.utils.encryption.key_management.load_key import load_key
from app.utils.metadata.store_metadata import load_metadata
import os

def execute(file_paths, username):
    for file_path in file_paths:
        decrypt_with_biometric(file_path, username)

def decrypt_with_biometric(file_path, username):
    metadata = load_metadata(file_path)
    if metadata is None:
        print("Metadata file does not exist.")
        return False

    if metadata["username"] != username:
        print("User not authorized to decrypt this file.")
        return False

    if not recognize_face(username):
        print("Face not recognized.")
        return False

    key_path = f"{file_path}.pub"
    key = load_key(key_path)
    decrypt_file(file_path, key)
    os.remove(key_path)
    os.remove(f"{file_path}.meta")
