import importlib

def handle_action(action, file_paths, security_level, username):
    action_map = {
        "Зашифровать": {
            "Первая ступень": "app.actions.branches.encryption.encrypt_first_level",
            "Вторая ступень": "app.actions.branches.encryption.encrypt_second_level",
            "Третья ступень": "app.actions.branches.encryption.encrypt_third_level",
            "Биометрия": "app.actions.branches.encryption.encrypt_with_biometric"
        },
        "Расшифровать": {
            "Первая ступень": "app.actions.branches.encryption.decrypt_first_level",
            "Вторая ступень": "app.actions.branches.encryption.decrypt_second_level",
            "Третья ступень": "app.actions.branches.encryption.decrypt_third_level",
            "Биометрия": "app.actions.branches.encryption.decrypt_with_biometric"
        },
        "Закрыть доступ": "app.actions.branches.lock.lock_files",
        "Открыть доступ": "app.actions.branches.lock.unlock_files"
    }
    
    if action in ["Зашифровать", "Расшифровать"]:
        module_name = action_map[action][security_level]
    else:
        module_name = action_map[action]
    
    module = importlib.import_module(module_name)
    module.execute(file_paths, username)
