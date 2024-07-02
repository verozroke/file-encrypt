def save_key(key, path):
    with open(path, 'wb') as file:
        file.write(key)

def load_key(path):
    with open(path, 'rb') as file:
        return file.read()
