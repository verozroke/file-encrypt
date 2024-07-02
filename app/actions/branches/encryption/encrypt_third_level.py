import os
from tkinter import filedialog, messagebox
from utils.encryption.generate_key import generate_key
from utils.encryption.encrypt_file import encrypt_file
from utils.encryption.key_management.save_key import save_key
from utils.encryption.rsa.generate_rsa_key_pair import generate_rsa_key_pair
from utils.encryption.rsa.save_rsa_key import save_rsa_key
from utils.encryption.rsa.encrypt_with_public_key import encrypt_with_public_key

def execute(file_paths):
    private_key, public_key = generate_rsa_key_pair()
    public_key_file = os.path.join(os.path.dirname(file_paths[0]), f"SHA256-{os.path.basename(file_paths[0])}.pub")
    private_key_file = filedialog.asksaveasfilename(defaultextension=".private", filetypes=[("Private Key", "*.private")])
    if not private_key_file:
        messagebox.showerror("Ошибка", "Файл для приватного ключа не выбран")
        return
    save_rsa_key(private_key, private_key_file, is_private=True)
    for file_path in file_paths:
        key = generate_key()
        encrypted_key = encrypt_with_public_key(key, public_key)
        save_key(encrypted_key, public_key_file)
        encrypt_file(file_path, key)
    messagebox.showinfo("Успех", f"Файлы зашифрованы. Публичный ключ сохранен в {public_key_file}. Приватный ключ сохранен на флэшку.")
