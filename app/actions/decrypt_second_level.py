import os
from tkinter import filedialog, messagebox
from utils.key_management.load_key import load_key
from utils.encryption.decrypt_file import decrypt_file

def execute(file_paths):
    key_file_path = filedialog.askopenfilename(title="Выберите файл с ключом")
    if not key_file_path:
        messagebox.showerror("Ошибка", "Файл с ключом не выбран")
        return
    key = load_key(key_file_path)
    for file_path in file_paths:
        decrypt_file(file_path, key)
    os.remove(key_file_path)
    messagebox.showinfo("Успех", "Файлы расшифрованы и ключ удален")
