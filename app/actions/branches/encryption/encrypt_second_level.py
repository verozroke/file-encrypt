import os
from tkinter import messagebox
from app.utils.encryption.generate_key import generate_key
from app.utils.encryption.encrypt_file import encrypt_file
from app.utils.encryption.key_management.save_key import save_key

def execute(file_paths):
    key = generate_key()
    for file_path in file_paths:
        key_file = os.path.join(os.path.dirname(file_path), f"SHA256-{os.path.basename(file_path)}.pub")
        save_key(key, key_file)
        encrypt_file(file_path, key)
    messagebox.showinfo("Успех", f"Файлы зашифрованы. Ключи сохранены.")
