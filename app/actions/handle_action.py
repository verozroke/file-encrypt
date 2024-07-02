import importlib

def handle_action(action, file_paths, security_level):
    action_map = {
        "Зашифровать": {
            "Первая ступень": "app.actions.encrypt_first_level",
            "Вторая ступень": "app.actions.encrypt_second_level",
            "Третья ступень": "app.actions.encrypt_third_level"
        },
        "Расшифровать": {
            "Первая ступень": "app.actions.decrypt_first_level",
            "Вторая ступень": "app.actions.decrypt_second_level",
            "Третья ступень": "app.actions.decrypt_third_level"
        },
        "Закрыть доступ": "app.actions.lock_files",
        "Открыть доступ": "app.actions.unlock_files"
    }
    
    if action in ["Зашифровать", "Расшифровать"]:
        module_name = action_map[action][security_level]
    else:
        module_name = action_map[action]
    
    module = importlib.import_module(module_name)
    module.execute(file_paths)
