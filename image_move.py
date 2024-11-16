import os
import shutil

def move_images(source_dir, target_dir, num_images):
    """
    移动固定数量的图片文件到目标文件夹。

    :param source_dir: 源文件夹路径
    :param target_dir: 目标文件夹路径
    :param num_images: 要移动的图片数量
    """
    # 检查源文件夹和目标文件夹是否存在
    if not os.path.exists(source_dir):
        print(f"源文件夹不存在: {source_dir}")
        return
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"目标文件夹已创建: {target_dir}")

    # 支持的图片文件扩展名
    valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

    # 获取源文件夹中的所有图片文件
    images = [file for file in os.listdir(source_dir) if file.lower().endswith(valid_extensions)]

    # 检查是否有足够的图片
    if len(images) < num_images:
        print(f"源文件夹中只有 {len(images)} 张图片，无法移动 {num_images} 张图片。")
        return

    # 移动图片
    for i, image in enumerate(images[:num_images]):
        source_path = os.path.join(source_dir, image)
        target_path = os.path.join(target_dir, image)
        shutil.move(source_path, target_path)
        print(f"Moved: {source_path} -> {target_path}")

    print(f"成功移动了 {num_images} 张图片到目标文件夹: {target_dir}")

if __name__ == "__main__":
    # 示例路径，请根据实际情况修改
    source_directory = "/mnt/data2/users/hilight/yiwei/dataset/FakeSocial/train/1_fake/SDXLLightning"  # 源文件夹路径
    target_directory = "/mnt/data2/users/hilight/yiwei/dataset/FakeSocial/test/1_fake/SDXLLightning"  # 目标文件夹路径
    number_of_images = 3000  # 要移动的图片数量

    # 调用函数移动图片
    move_images(source_directory, target_directory, number_of_images)

