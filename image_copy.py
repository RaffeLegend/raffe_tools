import os
import shutil
import random


if __name__ == "__main__":
    # 示例路径（请根据实际情况修改）
    source_directory = "/mnt/data2/users/chengyh1/datasets/USED/"
    target_directory = "/mnt/data2/users/hilight/yiwei/dataset/FakeSocial/train/0_real/USED/"
    max_images = 1000
    valid_extensions = (".jpg", ".jpeg", ".png")
    
    # 获取所有图片文件路径
    all_images = []
    for root, _, files in os.walk(source_directory):
        for file in files:
            if file.lower().endswith(valid_extensions):
                all_images.append(os.path.join(root, file))

    # 随机选择图片
    selected_images = random.sample(all_images, min(len(all_images), max_images))

    # 拷贝随机选择的图片
    copied_count = 0
    for source_path in selected_images:
        target_path = os.path.join(target_directory, os.path.basename(source_path))
        
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
            break

    print(f"Finished copying {copied_count} images.")