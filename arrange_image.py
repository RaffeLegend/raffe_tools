import os
import shutil

def copy_images(source_folder, destination_folder):
    # 检查目标文件夹是否存在，如果不存在则创建
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # 支持的图像文件扩展名
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    # 遍历源文件夹及其所有子文件夹
    for root, _, files in os.walk(source_folder):
        for filename in files:
            # 检查文件是否是图像
            if any(filename.lower().endswith(ext) for ext in image_extensions):
                # 构建完整的源文件路径
                source_path = os.path.join(root, filename)
                destination_path = os.path.join(destination_folder, filename)
                
                # 如果文件名重复，添加后缀避免覆盖
                if os.path.exists(destination_path):
                    base, ext = os.path.splitext(filename)
                    count = 1
                    while os.path.exists(destination_path):
                        new_filename = f"{base}_{count}{ext}"
                        destination_path = os.path.join(destination_folder, new_filename)
                        count += 1
                
                # 复制文件到目标文件夹
                shutil.copy2(source_path, destination_path)
                print(f"复制文件: {filename} 至 {destination_folder}")

# 使用例子
source_folder = '/path/to/source_folder'  # 替换为源文件夹路径
destination_folder = '/path/to/destination_folder'  # 替换为目标文件夹路径

copy_images(source_folder, destination_folder)