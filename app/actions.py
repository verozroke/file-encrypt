import os
from tkinter import filedialog, messagebox
from utils.encryption import encrypt_file, decrypt_file, generate_key, generate_key_from_password, load_key, save_key_with_filename
from utils.file_operations import lock_file, unlock_file

def handle_action(action, method, file_path):
    if action == "Зашифровать":
        encrypt_or_lock_file(method, file_path, encrypt=True)
    elif action == "Закрыть доступ":
        lock_file(file_path)
    elif action == "Расшифровать":
        encrypt_or_lock_file(method, file_path, encrypt=False)
    elif action == "Открыть доступ":
        unlock_file(file_path)

def encrypt_or_lock_file(method, file_path, encrypt=True):
    if method == "По ключу":
        if encrypt:
            key = generate_key()
            key_file = save_key_with_filename(key, file_path)
            encrypt_file(file_path, key)
            messagebox.showinfo("Успех", f"Файл зашифрован. Ключ сохранен в {key_file}")
        else:
            key_file = filedialog.askopenfilename(title="Выберите файл с ключом")
            if not key_file:
                messagebox.showerror("Ошибка", "Файл с ключом не выбран")
                return
            key = load_key(key_file)
            decrypt_file(file_path, key, key_file)
            messagebox.showinfo("Успех", "Файл расшифрован и ключ удалён")
    elif method == "По секретному слову":
        password = get_password()
        if password:
            key = generate_key_from_password(password)
            if encrypt:
                encrypt_file(file_path, key)
                messagebox.showinfo("Успех", "Файл зашифрован с использованием секретного слова")
            else:
                decrypt_file(file_path, key, None)
                messagebox.showinfo("Успех", "Файл расшифрован с использованием секретного слова")

def get_password():
    from tkinter import simpledialog
    return simpledialog.askstring("Пароль", "Введите секретное слово:", show='*')
