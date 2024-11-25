import os
import cv2
import numpy as np

def get_image_list(directory):
    # Supported image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'}
    
    # List to store image file names
    image_files = []
    
    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                image_files.append(os.path.join(root, file))

    return image_files

def get_frequency(image_path, output_path):
    # Step 1: 加载图像
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Step 2: 计算傅里叶变换
    f_transform = np.fft.fft2(image)
    f_shift = np.fft.fftshift(f_transform)  # 移频操作，低频移动到中心
    magnitude_spectrum = 20 * np.log(np.abs(f_shift))  # 计算幅值谱
    
    # Step 3: 保存结果图像
    output_name = os.path.splitext(image_path)[0] + '_frequency.png'
    output_path = os.path.join(output_path, output_name)
    cv2.imwrite(output_path, magnitude_spectrum)
    return magnitude_spectrum

if __name__ == "__main__":
    input_path = '/path/to/your/image/directory'
    output_path = ''
    os.makedirs(output_path, exist_ok=True)
    image_list = get_image_list(directory=input_path)

    for image_path in image_list:
        get_frequency(image_path, output_path)
        print(f"Frequency image saved for {image_path}")
    