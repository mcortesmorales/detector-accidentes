from PIL import Image
import os

input_dir = "model-implementor\original_images"
output_dir = "model-implementor\processed_images"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image = Image.open(os.path.join(input_dir, filename))
        image = image.resize((640, 640))
        image.save(os.path.join(output_dir, os.path.splitext(filename)[0] + ".jpg"))