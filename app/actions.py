# actions.py
import os
from tkinter import filedialog, messagebox, simpledialog
from utils.encryption import (
    decrypt_with_private_key,
    encrypt_with_public_key,
    generate_key,
    generate_key_from_password,
    generate_rsa_key_pair,
    load_rsa_key,
    save_key,
    load_key,
    encrypt_file,
    decrypt_file,
    save_rsa_key
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
            public_key_file = os.path.join(os.path.dirname(file_paths[0]), f"{os.path.basename(file_paths[0])}.pub")
            save_rsa_key(public_key, public_key_file)
            private_key_file = filedialog.asksaveasfilename(defaultextension=".private", filetypes=[("Private Key", "*.private")])
            save_rsa_key(private_key, private_key_file, is_private=True)
            for file_path in file_paths:
                key = generate_key()
                encrypted_key = encrypt_with_public_key(key, public_key)
                with open(f"{file_path}.key", 'wb') as key_file:
                    key_file.write(encrypted_key)
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
            messagebox.showinfo("Успех", "Файлы расшифрованы")
        elif security_level == "Третья ступень":
            public_key_path = filedialog.askopenfilename(title="Выберите публичный ключ")
            private_key_path = filedialog.askopenfilename(title="Выберите приватный ключ")
            if not public_key_path or not private_key_path:
                messagebox.showerror("Ошибка", "Публичный или приватный ключ не выбран")
                return
            public_key = load_rsa_key(public_key_path)
            private_key = load_rsa_key(private_key_path, is_private=True)
            for file_path in file_paths:
                key_file_path = f"{file_path}.key"
                if not os.path.exists(key_file_path):
                    messagebox.showerror("Ошибка", f"Ключевой файл не найден для {file_path}")
                    return
                with open(key_file_path, 'rb') as key_file:
                    encrypted_key = key_file.read()
                key = decrypt_with_private_key(encrypted_key, private_key)
                decrypt_file(file_path, key)
                os.remove(key_file_path)
            messagebox.showinfo("Успех", "Файлы расшифрованы")

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
