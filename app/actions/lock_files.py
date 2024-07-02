from tkinter import messagebox
from utils.file_locks.lock_file import lock_file

def execute(file_paths):
    for file_path in file_paths:
        lock_file(file_path)
    messagebox.showinfo("Успех", "Доступ к файлам закрыт")
