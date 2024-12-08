import os
import cv2
import numpy as np
from tqdm import tqdm
from scipy import fftpack

def fft_filter(im, mode=1):
    im = im.astype(np.float32)
    im = im/255.0
    for i in range(3):
        img = im[:,:,i]
        fft_img = np.fft.fft2(img)
        fft_img = np.log(np.abs(fft_img)+1e-3)
        fft_min = np.percentile(fft_img,5)
        fft_max = np.percentile(fft_img,95)
        fft_img = (fft_img - fft_min)/(fft_max - fft_min)
        fft_img = (fft_img-0.5)*2
        fft_img[fft_img<-1] = -1
        fft_img[fft_img>1] = 1
        #set mid and high freq to 0
        if mode>0:
            fft_img = np.fft.fftshift(fft_img)
            if mode == 1:
                fft_img[:57, :] = 0
                fft_img[:, :57] = 0
                fft_img[177:, :] = 0
                fft_img[:, 177:] = 0
            #set low and high freq to 0
            elif mode == 2:
                fft_img[:21, :] = 0
                fft_img[:, :21] = 0
                fft_img[203:, :] = 0
                fft_img[:, 203:] = 0
                fft_img[57:177, 57:177] = 0
            #set low and mid freq to 0
            elif mode == 3:
                fft_img[21:203, 21:203] = 0
            fft_img = np.fft.fftshift(fft_img)
        im[:,:,i] = fft_img
    return np.transpose(im, (2,0,1))

def get_average_frequency(directory, method='FFT', nums_images=200):
    image_list = get_image_list(directory)
    frequency_sum = None
    count = 0
    
    progress_bar = tqdm(total=len(image_list), desc="Processing images")
    for image_path in image_list:
        progress_bar.update(1)
        
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        
        if method == 'DFT':
            f_transform = cv2.dft(np.float32(image), flags=cv2.DFT_COMPLEX_OUTPUT)
            magnitude_spectrum = 20 * np.log(cv2.magnitude(f_transform[:, :, 0], f_transform[:, :, 1]) + 1)
        elif method == 'FFT':
            f_transform = fftpack.fft2(image)
            f_shift = fftpack.fftshift(f_transform)
            magnitude_spectrum = 20 * np.log(np.abs(f_shift) + 1)
        elif method == 'DCT':
            f_transform = cv2.dct(np.float32(image))
            magnitude_spectrum = np.log(np.abs(f_transform) + 1)
        elif method == 'FFT_FILTER':
            f_transform = fft_filter(image, mode=3)
            magnitude_spectrum = np.log(np.abs(f_transform) + 1)
        else:
            raise ValueError("Unsupported method. Choose from 'DFT', 'FFT', or 'DCT'.")

        # Resize magnitude_spectrum to a fixed size (e.g., 256x256) before accumulation
        fixed_size = (512, 512)
        resized_magnitude_spectrum = cv2.resize(magnitude_spectrum, fixed_size)
        
        if frequency_sum is None:
            frequency_sum = np.zeros_like(resized_magnitude_spectrum)
        
        frequency_sum += resized_magnitude_spectrum
        count += 1
        if count >= nums_images:
            break
    progress_bar.close()
    
    if count == 0:
        raise ValueError("No images found in the directory.")
    
    average_frequency = frequency_sum / count

    return average_frequency

def save_average_frequency_image(directory, output_path, method='FFT'):
    average_frequency = get_average_frequency(directory, method)
    
    # Normalize the average frequency to 0-255
    normalized_frequency = np.uint8(255 * (average_frequency - np.min(average_frequency)) / (np.max(average_frequency) - np.min(average_frequency)))
    
    # Convert to color image
    color_average_frequency = cv2.applyColorMap(normalized_frequency, cv2.COLORMAP_JET)
    
    # Save the result image
    output_name = 'average_frequency.png'
    output_file_path = os.path.join(output_path, output_name)
    cv2.imwrite(output_file_path, color_average_frequency)
    print(f"Average frequency image saved at {output_file_path}")

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

if __name__ == "__main__":
    input_path = '/mnt/data2/users/hilight/datasets/FakeSocialMedia/Images/sdxl_lightning'
    # output_path = '/mnt/data2/users/hilight/yiwei/dataset/frequency'
    output_path = './'
    os.makedirs(output_path, exist_ok=True)
    save_average_frequency_image(input_path, output_path, method='FFT')
