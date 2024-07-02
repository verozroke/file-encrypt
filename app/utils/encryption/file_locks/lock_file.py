import os
import shutil

def lock_file(file_path):
    hidden_dir = os.path.join(os.path.dirname(file_path), ".hidden")
    if not os.path.exists(hidden_dir):
        os.makedirs(hidden_dir)
    base_name = os.path.basename(file_path)
    new_path = os.path.join(hidden_dir, base_name)
    shutil.move(file_path, new_path)
    lock_info = f"{base_name} {new_path}"
    lock_info_path = os.path.join(os.path.dirname(file_path), "lock_info.txt")
    with open(lock_info_path, "a") as file:
        file.write(lock_info + "\n")
