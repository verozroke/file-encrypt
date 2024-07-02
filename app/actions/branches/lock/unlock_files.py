from tkinter import messagebox
from app.utils.encryption.file_locks.unlock_file import unlock_file

def execute(file_paths):
    for file_path in file_paths:
        unlock_file(file_path)
    messagebox.showinfo("Успех", "Доступ к файлам открыт")
