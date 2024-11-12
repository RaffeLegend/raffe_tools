import os
import shutil

def build_dataset(fake_dir, real_dir, data_list):
    """
    构建语义分割任务数据集
    :param image_dir: 原始图片文件夹路径
    :param gt_dir: Ground Truth 文件夹路径
    :param output_txt: 输出 txt 文件路径
    """
    # 确保文件夹存在
    if not os.path.exists(fake_dir):
        os.mkdir(fake_dir)
    if not os.path.exists(real_dir):
        os.mkdir(real_dir)

    for data in data_list:
        image_path, label = data
        if label == "0":
            shutil.copy2(image_path, real_dir)
        elif label == "1":
            shutil.copy2(image_path, fake_dir)
        else:
            print("the label is not real value!")


def read_dataset_from_txt(txt_file):
    """
    从 txt 文件读取语义分割数据集信息
    :param txt_file: 数据集的 txt 文件路径
    """
    data_list = list()
    # 检查文件是否存在
    if not os.path.exists(txt_file):
        raise FileNotFoundError(f"The txt file '{txt_file}' does not exist.")

    # 读取文件内容
    with open(txt_file, 'r') as f:
        lines = f.readlines()

    # 解析每一行
    for line in lines:
        line = line.strip()  # 去除多余的空白字符或换行符
        if not line:
            continue  # 跳过空行

        # 分割图片路径和 GT 路径
        try:
            image_path, gt_path, label = line.split()
            print(f"Image: {image_path}, GT: {gt_path}, label: {label}")
            data_list.append([image_path, label])
        except ValueError:
            print(f"Skipping invalid line: {line}")

    return data_list

# 设置 txt 文件路径
txt_file = "/mnt/data2/users/chengyh1/datasets/HiFi/yiwei.txt"  # 替换为你的 txt 文件路径

# 调用函数
data_list = read_dataset_from_txt(txt_file)

# 设置路径
fake_folder = "/mnt/data2/users/chengyh1/datasets/HiFi/data/ours/classification/1_fake"  # 替换为原始图片文件夹路径
real_folder = "/mnt/data2/users/chengyh1/datasets/HiFi/data/ours/classification/0_real"         # 替换为 Ground Truth 文件夹路径

# 构建数据集
build_dataset(fake_folder, real_folder, data_list)


