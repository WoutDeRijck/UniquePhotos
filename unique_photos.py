import cv2
import numpy as np
import os
import PIL

images = []

folder_dir = "./images_input"
for image in os.listdir(folder_dir):
    add = True
    original = cv2.imread("./images_input/" + image)

    for im in images:
        possibleDuplicate = cv2.imread("./images_input/" + im)
        if original.shape == possibleDuplicate.shape:
            difference = cv2.subtract(original, possibleDuplicate)
            b, g, r = cv2.split(difference)
            
            # The images are completely Equal
            if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
                add = False
        
    if add:
        images.append(image)

# Make folder with only the Unique Photos
if not os.path.exists("./images_output"):
    os.mkdir("images_output")

directory_output = "/home/wout/Documents/Varia/UniquePhotos/images_output"
directory_input = "/home/wout/Documents/Varia/UniquePhotos/images_input/"
for image in images:
    img = cv2.imread(directory_input + image)
    os.chdir(directory_output)
    cv2.imwrite(image, img)