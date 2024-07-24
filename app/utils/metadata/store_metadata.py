import json
import os

def save_metadata(file_path, metadata):
    meta_file_path = f"{file_path}.meta"
    with open(meta_file_path, 'w') as meta_file:
        json.dump(metadata, meta_file)

def load_metadata(file_path):
    meta_file_path = f"{file_path}.meta"
    if not os.path.exists(meta_file_path):
        return None
    with open(meta_file_path, 'r') as meta_file:
        return json.load(meta_file)
