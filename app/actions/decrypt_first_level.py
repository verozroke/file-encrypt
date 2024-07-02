from tkinter import messagebox
from utils.encryption.generate_key_from_password import generate_key_from_password
from utils.encryption.decrypt_file import decrypt_file
from shared.dialogs import get_password

def execute(file_paths):
    password = get_password()
    if password:
        key = generate_key_from_password(password)
        for file_path in file_paths:
            decrypt_file(file_path, key)
        messagebox.showinfo("Успех", "Файлы расшифрованы с использованием секретного слова")
