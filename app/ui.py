import os
from tkinter import Tk, Label, Button, StringVar, OptionMenu, filedialog, messagebox, Entry
from app.actions.handle_action import handle_action

class FileEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption App")
        self.root.geometry("500x500")

        self.file_paths = []

        self.action_var = StringVar(root)
        self.security_var = StringVar(root)
        self.username_var = StringVar(root)

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Выберите файлы или директорию:").pack(pady=10)
        Button(self.root, text="Выбрать файлы", command=self.select_files).pack()
        Button(self.root, text="Выбрать директорию", command=self.select_directory).pack()
        self.file_label = Label(self.root, text="")
        self.file_label.pack(pady=5)

        Label(self.root, text="Выберите действие:").pack(pady=10)
        self.action_var.set("Зашифровать")
        actions = ["Зашифровать", "Закрыть доступ", "Расшифровать", "Открыть доступ"]
        OptionMenu(self.root, self.action_var, *actions).pack()

        Label(self.root, text="Выберите уровень безопасности:").pack(pady=10)
        self.security_var.set("Первая ступень")
        security_levels = ["Первая ступень", "Вторая ступень", "Третья ступень", "Биометрия"]
        self.security_menu = OptionMenu(self.root, self.security_var, *security_levels, command=self.toggle_username_entry)
        self.security_menu.pack()

        self.username_label = Label(self.root, text="Введите ваше имя:")
        self.username_entry = Entry(self.root, textvariable=self.username_var)

        Button(self.root, text="Начать", command=self.start_action).pack(pady=20)

    def toggle_username_entry(self, value):
        if value == "Биометрия":
            self.username_label.pack(pady=10)
            self.username_entry.pack(pady=5)
        else:
            self.username_label.pack_forget()
            self.username_entry.pack_forget()

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames()
        if self.file_paths:
            self.file_label.config(text="; ".join(os.path.basename(path) for path in self.file_paths))

    def select_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.file_paths = [os.path.join(directory_path, f) for f in os.listdir(directory_path)]
            self.file_label.config(text=directory_path)

    def start_action(self):
        if not self.file_paths:
            messagebox.showerror("Ошибка", "Файлы или директория не выбраны")
            return

        action = self.action_var.get()
        security_level = self.security_var.get()
        username = self.username_var.get() if security_level == "Биометрия" else None
        handle_action(action, self.file_paths, security_level, username)
