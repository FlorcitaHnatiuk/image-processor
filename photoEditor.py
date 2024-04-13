from PIL import Image, ImageEnhance, ImageFilter, ImageOps
import os

# Define paths
path = "./imgs"
pathOut = "./editedImgs"

# Create directories if they do not exist
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(pathOut):
    os.makedirs(pathOut)

# Supported image file extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

# Define a function to apply color transformations
def apply_color_transformations(image, name, path):
    outputs = {
        "grayscale": os.path.join(path, f"{name}_grayscale.jpg"),
        "sepia": os.path.join(path, f"{name}_sepia.jpg"),
        "negative": os.path.join(path, f"{name}_negative.jpg"),
        "saturated": os.path.join(path, f"{name}_saturated.jpg")
    }

    # Check if the files already exist to avoid reprocessing
    if all(os.path.exists(output) for output in outputs.values()):
        print(f"All transformations for {name} already exist. Skipping...")
        return

    # Grayscale
    gray = image.convert('L')
    gray.save(outputs["grayscale"])

    # Sepia
    sepia = ImageOps.colorize(gray, '#704214', '#C0A080')  # Dark brown, light brown
    sepia.save(outputs["sepia"])

    # Negative
    negative = ImageOps.invert(image)
    negative.save(outputs["negative"])

    # Enhanced Saturation
    converter = ImageEnhance.Color(image)
    saturated = converter.enhance(2.0)  # Increase saturation by factor of 2
    saturated.save(outputs["saturated"])

# Process each file in the directory
for filename in os.listdir(path):
    # Check if the file has a valid image file extension
    if os.path.splitext(filename)[1].lower() in valid_extensions:
        img_path = os.path.join(path, filename)
        try:
            # Open the image file
            img = Image.open(img_path)
            img = img.filter(ImageFilter.SHARPEN).rotate(-90)  # Apply initial sharpening and rotation

            # Prepare output path for color edits
            color_path = os.path.join(pathOut, os.path.splitext(filename)[0])
            if not os.path.exists(color_path):
                os.makedirs(color_path)

            # Apply color transformations and save
            apply_color_transformations(img, os.path.splitext(filename)[0], color_path)

        except IOError:
            # Print an error message if the image cannot be opened or processed
            print(f"Cannot open or process {img_path}")
    else:
        # Print a message for files that are skipped
        print(f"Skipped non-image file: {filename}")
