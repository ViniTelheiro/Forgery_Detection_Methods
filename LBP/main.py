import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str,
                        help='path of the input image')
    parser.add_argument('--save_dir', type=str, default='output/',
                        help='saving path of the output')
    return parser.parse_args()

      
def get_pixel(img, center, x, y):
      
    new_value = 0
      
    try:
        # If local neighbourhood pixel 
        # value is greater than or equal
        # to center pixel values then 
        # set it to 1
        if img[x][y] >= center:
            new_value = 1
              
    except:
        # Exception is required when 
        # neighbourhood value of a center
        # pixel value is null i.e. values
        # present at boundaries.
        pass
      
    return new_value
   
# Function for calculating LBP
def lbp_calculated_pixel(img, x, y):
   
    center = img[x][y]
   
    val_ar = []
      
    # top_left
    val_ar.append(get_pixel(img, center, x-1, y-1))
      
    # top
    val_ar.append(get_pixel(img, center, x-1, y))
      
    # top_right
    val_ar.append(get_pixel(img, center, x-1, y + 1))
      
    # right
    val_ar.append(get_pixel(img, center, x, y + 1))
      
    # bottom_right
    val_ar.append(get_pixel(img, center, x + 1, y + 1))
      
    # bottom
    val_ar.append(get_pixel(img, center, x + 1, y))
      
    # bottom_left
    val_ar.append(get_pixel(img, center, x + 1, y-1))
      
    # left
    val_ar.append(get_pixel(img, center, x, y-1))
       
    # Now, we need to convert binary
    # values to decimal
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
   
    val = 0
      
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
          
    return val

if __name__ == '__main__':
    args = get_args()
    name = os.path.split(args.image_path)[-1]
    img = cv2.imread(args.image_path, cv2.IMREAD_ANYCOLOR)
    img = np.array(img)
    height, width, _ = img.shape
   
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
   
    img_lbp = np.zeros((height, width), np.uint8)
   
    for i in range(0, height):
        for j in range(0, width):
            img_lbp[i, j] = lbp_calculated_pixel(gray, i, j)

    cv2.imwrite(os.path.join(args.save_dir,name),img_lbp)
