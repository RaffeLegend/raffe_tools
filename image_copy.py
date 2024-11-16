import os
import shutil

def copy_images(source_dir, target_dir, max_images=10000):
    """
    拷贝图片文件到目标路径。

    :param source_dir: 源目录路径
    :param target_dir: 目标目录路径
    :param max_images: 最大拷贝图片数量，默认为 10,000
    """
    # 确保目标路径存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 支持的图片文件扩展名
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

    # 统计已拷贝图片数量
    copied_count = 0

    # 遍历源目录
    for root, _, files in os.walk(source_dir):
        for file in files:
            if file.lower().endswith(valid_extensions):
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)
                
                # 如果目标文件已存在，跳过
                if os.path.exists(target_path):
                    continue
                
                # 拷贝文件
                shutil.copy2(source_path, target_path)
                copied_count += 1

                # 打印拷贝进度
                print(f"Copied: {source_path} -> {target_path} ({copied_count}/{max_images})")
                
                # 如果达到最大拷贝数量，停止操作
                if copied_count >= max_images:
                    print(f"Reached the limit of {max_images} images.")
                    return
    
    print(f"Finished copying {copied_count} images.")

if __name__ == "__main__":
    # 示例路径（请根据实际情况修改）
    source_directory = "/mnt/data2/users/chengyh1/datasets/USED/"
    target_directory = "/mnt/data2/users/hilight/yiwei/dataset/FakeSocial/train/0_real/USED/"
    
    # 调用函数拷贝图片
    copy_images(source_directory, target_directory, max_images=20000)

