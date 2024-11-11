import os
import shutil

def build_dataset(image_dir, gt_dir, output_txt, data_list):
    """
    构建语义分割任务数据集
    :param image_dir: 原始图片文件夹路径
    :param gt_dir: Ground Truth 文件夹路径
    :param output_txt: 输出 txt 文件路径
    """
    # 确保文件夹存在
    if not os.path.exists(image_dir):
        os.mkdir(image_dir)
    if not os.path.exists(gt_dir):
        os.mkdir(gt_dir)

    # 获取文件列表
    image_files = sorted(os.listdir(image_dir))
    gt_files = sorted(os.listdir(gt_dir))

    with open(output_txt, 'w') as f:
        for data in data_list:
            image, gt = data
            file_name = image.split("/")[-1]
            gt_name = file_name.split(".")[0] + "_gt." + file_name.split(".")[-1]
            dest_path = os.path.join(image_dir, file_name)
            gt_path = os.path.join(gt_dir, gt_name)
            shutil.copy2(image, dest_path)
            shutil.copy2(gt, gt_path)
            f.write(f"{file_name}\n")

    # 检查文件数量是否一致
    if len(image_files) != len(gt_files):
        print("Warning: The number of images and GT files do not match.")

    print(f"Dataset txt file saved to: {output_txt}")

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
            if label !=0 and gt_path != "None":
                data_list.append([image_path, gt_path])
        except ValueError:
            print(f"Skipping invalid line: {line}")

    return data_list

# 设置 txt 文件路径
txt_file = "/mnt/data2/users/chengyh1/datasets/HiFi/yiwei.txt"  # 替换为你的 txt 文件路径

# 调用函数
data_list = read_dataset_from_txt(txt_file)

# 设置路径
image_folder = "/mnt/data2/users/chengyh1/datasets/HiFi/data/ours/fake"  # 替换为原始图片文件夹路径
gt_folder = "/mnt/data2/users/chengyh1/datasets/HiFi/data/ours/mask"         # 替换为 Ground Truth 文件夹路径
output_file = "/mnt/data2/users/chengyh1/datasets/HiFi/data/ours/fake.txt"      # 输出 txt 文件名

# 构建数据集
build_dataset(image_folder, gt_folder, output_file, data_list)


