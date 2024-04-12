from PIL import Image, ImageEnhance, ImageFilter
import os

# Define paths
path = "./imgs"  # Directory containing the original images
pathOut = "./editedImgs"  # Directory where edited images will be stored

# Create directories if they do not exist
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Supported image file extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Process each file in the directory
for filename in os.listdir(path):
    # Check if the file has a valid image file extension
    if os.path.splitext(filename)[1].lower() in valid_extensions:
        img_path = os.path.join(path, filename)
        try:
            # Open the image file
            img = Image.open(img_path)

            # Apply image edits
            # Sharpen the image, convert to black and white, and rotate 90 degrees counter-clockwise
            edit = img.filter(ImageFilter.SHARPEN).convert('L').rotate(-90)

            # Enhance the contrast by a factor of 1.5
            enhancer = ImageEnhance.Contrast(edit)
            edit = enhancer.enhance(1.5)

            # Save the edited image
            clean_name = os.path.splitext(filename)[0]  # Remove the file extension
            edit.save(os.path.join(pathOut, f"{clean_name}_edited.jpg"))

        except IOError:
            # Print an error message if the image cannot be opened or processed
            print(f"Cannot open or process {img_path}")
    else:
        # Print a message for files that are skipped
        print(f"Skipped non-image file: {filename}")
