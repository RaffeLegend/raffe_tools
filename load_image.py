import os
import json
import shutil

def load_image_paths(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data.get('image_paths', [])

def copy_images(image_paths, target_folder):
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    
    for image_path in image_paths:
        if os.path.exists(image_path):
            shutil.copy(image_path, target_folder)
        else:
            print(f"Image not found: {image_path}")

if __name__ == "__main__":
    json_file = 'path_to_your_json_file.json'
    target_folder = 'path_to_target_folder'
    
    image_paths = load_image_paths(json_file)
    copy_images(image_paths, target_folder)