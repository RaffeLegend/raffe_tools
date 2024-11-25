import os
from PIL import Image

def resize_images(input_dir, output_dir, size=(256, 256)):
    """
    Resize all images in the input directory to the specified size and save them in the output directory,
    preserving the original directory structure.

    :param input_dir: Path to the input directory.
    :param output_dir: Path to the output directory.
    :param size: Tuple specifying the new size (width, height) for the images.
    """
    for root, dirs, files in os.walk(input_dir):
        # Compute the relative path to preserve the directory structure
        relative_path = os.path.relpath(root, input_dir)
        output_path = os.path.join(output_dir, relative_path)
        
        # Create the output directory if it doesn't exist
        os.makedirs(output_path, exist_ok=True)

        for file in files:
            try:
                # Check if the file is an image
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                    input_file = os.path.join(root, file)
                    output_file = os.path.join(output_path, file)

                    # Open and resize the image
                    with Image.open(input_file) as img:
                        img = img.resize(size, Image.Resampling.LANCZOS)
                        img.save(output_file)
                        print(f"Processed: {input_file} -> {output_file}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

if __name__ == "__main__":
    # Specify the input and output directories
    input_directory = "/path/to/input/directory"
    output_directory = "/path/to/output/directory"
    
    # Resize images
    resize_images(input_directory, output_directory)