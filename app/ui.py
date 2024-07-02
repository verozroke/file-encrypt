import os
from tkinter import Tk, Label, Button, StringVar, OptionMenu, filedialog, messagebox
from app.actions.handle_action import handle_action
from app.utils.encryption.file_locks.get_all_files_in_directory import get_all_files_in_directory

class FileEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption App")
        self.root.geometry("500x500")

        self.file_paths = []

        self.action_var = StringVar(root)
        self.security_var = StringVar(root)

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
        security_levels = ["Первая ступень", "Вторая ступень", "Третья ступень"]
        OptionMenu(self.root, self.security_var, *security_levels).pack()

        Button(self.root, text="Начать", command=self.start_action).pack(pady=20)

    def select_files(self):
        self.file_paths = filedialog.askopenfilenames()
        if self.file_paths:
            self.file_label.config(text="; ".join(os.path.basename(path) for path in self.file_paths))

    def select_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.file_paths = get_all_files_in_directory(directory_path)
            self.file_label.config(text=directory_path)

    def start_action(self):
        if not self.file_paths:
            messagebox.showerror("Ошибка", "Файлы или директория не выбраны")
            return

        action = self.action_var.get()
        security_level = self.security_var.get()
        handle_action(action, self.file_paths, security_level)
