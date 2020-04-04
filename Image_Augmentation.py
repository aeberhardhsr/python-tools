#Name: Andreas
#Project: SmartProducts

from cv2 import cv2
import os
import numpy as np
import time 
import shutil

startTime_pictures = time.time()


#Set import folder path for images
def loadImages(path = "O:/02_images_rotated/spezial"):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')] #choose the extension you want and replace '.jpg' with your own extension

#Set destination folder path for images
Folder_name_images="O:/03_images_augmented/images"

#Set import path of all the labels you want to copy and multiply
dir_src = "O:/02_images_rotated/spezial/"

#Set Counter Variables
num=1
num1=1
num2=1
num3=1
num4=1

#Definitions of Image Augmentation Modes
def emboss_image(image):
    kernel_emboss_1=np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
    image = cv2.filter2D(image, -1, kernel_emboss_1)+128
    cv2.imwrite(Folder_name_images + "/Augmented_Emboss_"+str(num)+ ".jpg", image)
    

def edge_image(image,ksize):
    image = cv2.Sobel(image,cv2.CV_16U,1,0,ksize=ksize)
    cv2.imwrite(Folder_name_images + "/Augmented_Edge_"+ str(num1) + ".jpg", image)
    

def addeptive_gaussian_noise(image):
    h,s,v=cv2.split(image)
    s = cv2.adaptiveThreshold(s, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    h = cv2.adaptiveThreshold(h, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    v = cv2.adaptiveThreshold(v, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    image=cv2.merge([h,s,v])
    cv2.imwrite(Folder_name_images + "/Augmented_Addaptive_Gaussian_Noise_" +str(num2)+ ".jpg", image)
    

def contrast_image(image,contrast):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image[:,:,2] = [[max(pixel - contrast, 0) if pixel < 190 else min(pixel + contrast, 255) for pixel in row] for row in image[:,:,2]]
    image= cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    cv2.imwrite(Folder_name_images + "/Augmented_Contrast_" +str(num3)+ ".jpg", image)

def grayscale_image(image):
    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(Folder_name_images + "/Augmented_Grayscale_"+str(num4)+".jpg", image)



#Main Code

#Code for Image Processing
filenames_image = (loadImages())
images = []
for file_images in filenames_image:
    images.append(cv2.imread(file_images, cv2.IMREAD_UNCHANGED))



for image in images:
    
    emboss_image(image)
    num=num+1

    edge_image(image,3)
    num1=num1+1

    addeptive_gaussian_noise(image)
    num2=num2+1

    contrast_image(image,50)
    num3=num3+1
    
    grayscale_image(image)
    num4=num4+1
 
print('All Pictures were augmented and saved successfully in {0} seconds'.format(time.time() - startTime_pictures) ) #print the needed time for image processing


startTime_labels = time.time()

#Code for Copy and Renaming all the labels from the original labeled Images
#shutil.copyfile(/your/own/path/to/source/directory, /your/own/path/to/destination/directory, .format() for increment counter in filename)
i=1
for filename in os.listdir(dir_src):
    if filename.endswith('.txt'):
        shutil.copyfile( dir_src + filename, 'O:/03_images_augmented/images/Augmented_Emboss_{}.txt'.format(i))
        shutil.copyfile( dir_src + filename, 'O:/03_images_augmented/images/Augmented_Edge_{}.txt'.format(i))
        shutil.copyfile( dir_src + filename, 'O:/03_images_augmented/images/Augmented_Addaptive_Gaussian_Noise_{}.txt'.format(i))
        shutil.copyfile( dir_src + filename, 'O:/03_images_augmented/images/Augmented_Contrast_{}.txt'.format(i))
        shutil.copyfile( dir_src + filename, 'O:/03_images_augmented/images/Augmented_Grayscale_{}.txt'.format(i))
        i=i+1

print("All labels were multiplied within {0} seconds".format(time.time() - startTime_labels)) #print the needed time for multiply the label files