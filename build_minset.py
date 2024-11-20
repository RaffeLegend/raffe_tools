import os
import shutil

def copy_images_with_limit(src_dir, dst_dir, max_files_per_folder):
    """
    Copy images from src_dir to dst_dir while preserving the folder structure.
    Limit the number of files in each folder.
    
    Args:
        src_dir (str): Path to the source directory.
        dst_dir (str): Path to the destination directory.
        max_files_per_folder (int): Maximum number of files per folder.
    """
    if not os.path.exists(src_dir):
        print(f"Source directory '{src_dir}' does not exist.")
        return
    
    # Ensure the destination directory exists
    os.makedirs(dst_dir, exist_ok=True)

    for root, dirs, files in os.walk(src_dir):
        # Relative path from source directory
        relative_path = os.path.relpath(root, src_dir)

        # Corresponding destination folder
        dst_folder = os.path.join(dst_dir, relative_path)

        # Filter files to include only images
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff'))]

        # Limit the number of files
        limited_files = image_files[:max_files_per_folder]

        if limited_files:
            # Create the destination folder
            os.makedirs(dst_folder, exist_ok=True)

            # Copy limited files
            for file in limited_files:
                src_file_path = os.path.join(root, file)
                dst_file_path = os.path.join(dst_folder, file)
                shutil.copy(src_file_path, dst_file_path)
                print(f"Copied: {src_file_path} -> {dst_file_path}")

if __name__ == "__main__":
    # Example usage
    source_directory = "/mnt/data2/users/hilight/yiwei/dataset/FakeSocial/"
    destination_directory = "/mnt/data2/users/hilight/yiwei/dataset/MiniTest/"
    max_files = 1000  # Maximum number of files per folder

    copy_images_with_limit(source_directory, destination_directory, max_files)

