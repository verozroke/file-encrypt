import os
from tkinter import filedialog, messagebox
from utils.encryption import encrypt_files, decrypt_files, generate_key, generate_key_from_password, load_key, save_key_with_filename
from utils.file_operations import lock_file, unlock_file

def handle_action(action, method, file_paths):
    if action == "Зашифровать":
        encrypt_or_lock_files(method, file_paths, encrypt=True)
    elif action == "Закрыть доступ":
        for file_path in file_paths:
            lock_file(file_path)
    elif action == "Расшифровать":
        encrypt_or_lock_files(method, file_paths, encrypt=False)
    elif action == "Открыть доступ":
        for file_path in file_paths:
            unlock_file(file_path)

def encrypt_or_lock_files(method, file_paths, encrypt=True):
    if method == "По ключу":
        if encrypt:
            key = generate_key()
            key_file = save_key_with_filename(key, file_paths)
            encrypt_files(file_paths, key)
            messagebox.showinfo("Успех", f"Файлы зашифрованы. Ключ сохранен в {key_file}")
        else:
            key_file = filedialog.askopenfilename(title="Выберите файл с ключом")
            if not key_file:
                messagebox.showerror("Ошибка", "Файл с ключом не выбран")
                return
            key = load_key(key_file)
            decrypt_files(file_paths, key, key_file)
            messagebox.showinfo("Успех", "Файлы расшифрованы и ключ удалён")
    elif method == "По секретному слову":
        password = get_password()
        if password:
            key = generate_key_from_password(password)
            if encrypt:
                encrypt_files(file_paths, key)
                messagebox.showinfo("Успех", "Файлы зашифрованы с использованием секретного слова")
            else:
                decrypt_files(file_paths, key, None)
                messagebox.showinfo("Успех", "Файлы расшифрованы с использованием секретного слова")

def get_password():
    from tkinter import simpledialog
    return simpledialog.askstring("Пароль", "Введите секретное слово:", show='*')
