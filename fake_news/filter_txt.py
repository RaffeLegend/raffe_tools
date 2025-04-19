import os
import json
import shutil

# JSON 文件路径
json_file_path = 'output.json'

# 新文件夹路径
destination_folder = './article'

# 确保目标文件夹存在
os.makedirs(destination_folder, exist_ok=True)

# 读取 JSON 文件
with open(json_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

base_path = '/mnt/data1/users/yiwei/data/origin/'
# 假设 JSON 文件中包含一个列表，列表中是 txt 文件的路径
for txt_file in data:  # 根据 JSON 的结构调整键名
    txt_file = base_path + txt_file['article_path']
    if os.path.isfile(txt_file):
        shutil.copy(txt_file, destination_folder)
        print(f"Copied: {txt_file}")
    else:
        print(f"File not found: {txt_file}")
