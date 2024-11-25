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
    # f_transform = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
    f_transform = cv2.dct(np.float32(image))
    magnitude_spectrum = np.log(np.abs(f_transform) + 1)
    # f_transform = np.fft.fft2(image)
    # f_shift = np.fft.fftshift(f_transform)  # 移频操作，低频移动到中心
    # magnitude_spectrum = 20 * np.log(np.abs(f_shift))  # 计算幅值谱
    # magnitude_spectrum = 20 * np.log(cv2.magnitude(f_shift[:, :, 0], f_shift[:, :, 1]) + 1)
    
    # Step 3: 将幅值谱归一化到0-255并转换为8位图像
    magnitude_spectrum = np.uint8(255 * (magnitude_spectrum - np.min(magnitude_spectrum)) / (np.max(magnitude_spectrum) - np.min(magnitude_spectrum)))
    
    # Step 4: 将灰度图像转换为彩色图像
    color_magnitude_spectrum = cv2.applyColorMap(magnitude_spectrum, cv2.COLORMAP_JET)
    
    # Step 5: 保存结果图像
    output_name = os.path.splitext(os.path.basename(image_path))[0] + '_frequency.png'
    output_path = os.path.join(output_path, output_name)
    cv2.imwrite(output_path, color_magnitude_spectrum)
    return color_magnitude_spectrum

if __name__ == "__main__":
    input_path = '/mnt/data2/users/hilight/yiwei/dataset/TestSet'
    output_path = '/mnt/data2/users/hilight/yiwei/dataset/frequency'
    os.makedirs(output_path, exist_ok=True)
    image_list = get_image_list(directory=input_path)
    for image_path in image_list:
        # Create the corresponding directory structure in the output path
        relative_path = os.path.relpath(image_path, input_path)
        output_image_path = os.path.join(output_path, os.path.dirname(relative_path))
        os.makedirs(output_image_path, exist_ok=True)
        
        # Generate and save the frequency image
        get_frequency(image_path, output_image_path)
        print(f"Frequency image saved for {image_path}")
