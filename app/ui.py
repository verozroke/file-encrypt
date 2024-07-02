from tkinter import Label, Button, StringVar, OptionMenu, filedialog, messagebox
import os
from app.actions import handle_action
from utils.file_operations import get_all_files_in_directory

class FileEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption App")
        self.root.geometry("500x500")

        self.file_paths = []

        self.action_var = StringVar(root)
        self.method_var = StringVar(root)

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

        Label(self.root, text="Выберите метод шифрования:").pack(pady=10)
        self.method_var.set("По ключу")
        methods = ["По ключу", "По секретному слову"]
        OptionMenu(self.root, self.method_var, *methods).pack()

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
        method = self.method_var.get()
        handle_action(action, method, self.file_paths)
