from tkinter import Label, Button, StringVar, OptionMenu, filedialog, messagebox
import os
from app.actions import handle_action

class FileEncryptionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Encryption App")
        self.root.geometry("500x500")

        self.file_path = None

        self.action_var = StringVar(root)
        self.method_var = StringVar(root)

        self.create_widgets()

    def create_widgets(self):
        Label(self.root, text="Выберите файл:").pack(pady=10)
        Button(self.root, text="Выбрать файл", command=self.select_file).pack()
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

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))

    def start_action(self):
        if not self.file_path:
            messagebox.showerror("Ошибка", "Файл не выбран")
            return

        action = self.action_var.get()
        method = self.method_var.get()
        handle_action(action, method, self.file_path)
