import os
import shutil
from tkinter import filedialog, messagebox

def unlock_file(file_path):
    lock_info_path = filedialog.askopenfilename(title="Выберите файл с информацией о закрытых файлах")
    if not lock_info_path:
        messagebox.showerror("Ошибка", "Файл с информацией не выбран")
        return
    with open(lock_info_path, "r") as file:
        lines = file.readlines()
    unlock_success = False
    for line in lines:
        base_name, new_path = line.strip().split()
        if base_name == os.path.basename(file_path):
            shutil.move(new_path, file_path)
            unlock_success = True
            break
    if unlock_success:
        messagebox.showinfo("Успех", "Доступ к файлу открыт")
    else:
        messagebox.showerror("Ошибка", "Информация о файле не найдена")
