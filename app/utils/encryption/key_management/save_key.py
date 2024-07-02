def save_key(key, path):
    with open(path, 'wb') as file:
        file.write(key)
