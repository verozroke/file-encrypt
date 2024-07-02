import os
from tkinter import filedialog, messagebox
from utils.encryption.key_management.load_key import load_key
from utils.encryption.rsa.load_rsa_key import load_rsa_key
from utils.encryption.rsa.decrypt_with_private_key import decrypt_with_private_key
from utils.encryption.decrypt_file import decrypt_file

def execute(file_paths):
    public_key_path = filedialog.askopenfilename(title="Выберите публичный ключ")
    private_key_path = filedialog.askopenfilename(title="Выберите приватный ключ")
    if not public_key_path or not private_key_path:
        messagebox.showerror("Ошибка", "Публичный или приватный ключ не выбран")
        return
    encrypted_key = load_key(public_key_path)
    private_key = load_rsa_key(private_key_path, is_private=True)
    for file_path in file_paths:
        key = decrypt_with_private_key(encrypted_key, private_key)
        decrypt_file(file_path, key)
    os.remove(public_key_path)
    messagebox.showinfo("Успех", "Файлы расшифрованы и публичный ключ удален")
