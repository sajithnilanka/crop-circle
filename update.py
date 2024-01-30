#!/usr/local/bin/python3
import os
import numpy as np
from PIL import Image, ImageDraw

#Define input and output folders
input_folder = "input_images"
output_folder = "output_images"

#loop through all the files in the input folder
for filename in os.listdir(input_folder):
    #check if the file is an image file
    if filename.endswith('.jpg') or filename.endswith('.png'):
        #Define input and output file paths
        input_path = os.path.join(input_folder,filename)
        output_path = os.path.join(output_folder,filename.split('.')[0]+'.png')


        #load the input image
        input_image = Image.open(input_path).convert("RGB")
        # Open the input image as numpy array, convert to RGB
        #img=Image.open("dog.jpg").convert("RGB")  888
        npImage=np.array(input_image)
        h,w=input_image.size
        alpha = Image.new('L', input_image.size,0)
        draw = ImageDraw.Draw(alpha)
        draw.pieslice([0,0,h,w],0,360,fill=255)

        npAlpha=np.array(alpha)
        npImage=np.dstack((npImage,npAlpha))
        Image.fromarray(npImage).save('result.png')

        output_image =Image.fromarray(npImage)
        output_image.save(output_path)
