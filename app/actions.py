# actions.py
import os
from tkinter import filedialog, messagebox, simpledialog
from utils.encryption import (
    generate_key,
    generate_key_from_password,
    generate_rsa_key_pair,
    save_key,
    load_key,
    save_rsa_key,
    load_rsa_key,
    encrypt_file,
    decrypt_file,
    encrypt_with_public_key,
    decrypt_with_private_key
)
from utils.file_operations import lock_file, unlock_file

def handle_action(action, file_paths, security_level):
    if action == "Зашифровать":
        if security_level == "Первая ступень":
            password = get_password()
            if password:
                key = generate_key_from_password(password)
                for file_path in file_paths:
                    encrypt_file(file_path, key)
                messagebox.showinfo("Успех", "Файлы зашифрованы с использованием секретного слова")
        elif security_level == "Вторая ступень":
            key = generate_key()
            for file_path in file_paths:
                key_file = os.path.join(os.path.dirname(file_path), f"SHA256-{os.path.basename(file_path)}.pub")
                save_key(key, key_file)
                encrypt_file(file_path, key)
            messagebox.showinfo("Успех", f"Файлы зашифрованы. Ключи сохранены.")
        elif security_level == "Третья ступень":
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

    elif action == "Расшифровать":
        if security_level == "Первая ступень":
            password = get_password()
            if password:
                key = generate_key_from_password(password)
                for file_path in file_paths:
                    decrypt_file(file_path, key)
                messagebox.showinfo("Успех", "Файлы расшифрованы с использованием секретного слова")
        elif security_level == "Вторая ступень":
            key_file_path = filedialog.askopenfilename(title="Выберите файл с ключом")
            if not key_file_path:
                messagebox.showerror("Ошибка", "Файл с ключом не выбран")
                return
            key = load_key(key_file_path)
            for file_path in file_paths:
                decrypt_file(file_path, key)
            os.remove(key_file_path)
            messagebox.showinfo("Успех", "Файлы расшифрованы и ключ удален")
        elif security_level == "Третья ступень":
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

    elif action == "Закрыть доступ":
        for file_path in file_paths:
            lock_file(file_path)
        messagebox.showinfo("Успех", "Доступ к файлам закрыт")

    elif action == "Открыть доступ":
        for file_path in file_paths:
            unlock_file(file_path)
        messagebox.showinfo("Успех", "Доступ к файлам открыт")

def get_password():
    return simpledialog.askstring("Пароль", "Введите секретное слово:", show='*')
