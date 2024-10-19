import os
import re
import img2pdf
from PIL import Image

def natural_sort(l):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

directory_path = "..."
output_file = "C:\\Users\\...\\Desktop\\output.pdf"

image_files = [i for i in os.listdir(directory_path) if i.endswith(".png")]
image_files = natural_sort(image_files)

# Convert images to remove alpha channel
processed_images = []
for image_file in image_files:
    with Image.open(os.path.join(directory_path, image_file)) as img:
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        processed_images.append(os.path.join(directory_path, image_file))
        img.save(os.path.join(directory_path, image_file), "PNG")

with open(output_file, "wb") as file:
    pdf_data = img2pdf.convert([os.path.join(directory_path, img) for img in processed_images])
    file.write(pdf_data)
