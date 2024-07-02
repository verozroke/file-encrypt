import os
from tkinter import messagebox
from app.utils.encryption.generate_key_from_password import generate_key_from_password
from app.utils.encryption.encrypt_file import encrypt_file
from app.shared.dialogs import get_password

def execute(file_paths):
    password = get_password()
    if password:
        key = generate_key_from_password(password)
        for file_path in file_paths:
            encrypt_file(file_path, key)
        messagebox.showinfo("Успех", "Файлы зашифрованы с использованием секретного слова")
