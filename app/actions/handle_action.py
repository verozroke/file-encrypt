import importlib

def handle_action(action, file_paths, security_level):
    action_map = {
        "Зашифровать": {
            "Первая ступень": "app.actions.branches.encrypt_first_level",
            "Вторая ступень": "app.actions.branches.encrypt_second_level",
            "Третья ступень": "app.actions.branches.encrypt_third_level"
        },
        "Расшифровать": {
            "Первая ступень": "app.actions.branches.decrypt_first_level",
            "Вторая ступень": "app.actions.branches.decrypt_second_level",
            "Третья ступень": "app.actions.branches.decrypt_third_level"
        },
        "Закрыть доступ": "app.actions.lock.lock_files",
        "Открыть доступ": "app.actions.lock.unlock_files"
    }
    
    if action in ["Зашифровать", "Расшифровать"]:
        module_name = action_map[action][security_level]
    else:
        module_name = action_map[action]
    
    module = importlib.import_module(module_name)
    module.execute(file_paths)
