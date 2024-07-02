from tkinter import simpledialog

def get_password():
    return simpledialog.askstring("Пароль", "Введите секретное слово:", show='*')
