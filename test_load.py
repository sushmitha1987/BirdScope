import cv2
import os

image_dir = "D:/BirdSpecies/input/inference_images"

for img_name in os.listdir(image_dir):
    img_path = os.path.join(image_dir, img_name)
    print(f"Trying to load: {img_path}")
    image = cv2.imread(img_path)
    if image is None:
        print(f" Failed to load: {img_name}")
    else:
        print(f" Successfully loaded: {img_name}")
