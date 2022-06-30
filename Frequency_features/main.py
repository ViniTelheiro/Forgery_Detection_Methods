import cv2
import numpy as np
import os
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str,
                        help='path of the input image')
    parser.add_argument('--save_dir', type=str, default='output/',
                        help='saving path of the output')
    return parser.parse_args()

def hpf(img):
    return img - cv2.GaussianBlur(img,(0,0),3)

def hf_feature(src):
    img = cv2.imread(src, cv2.IMREAD_ANYCOLOR)
    img = np.array(img).astype('float32')
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    img = cv2.dct(img)
    img = hpf(img)
    img = cv2.idct(img)
    img = ((img - img.min())/(img.max() - img.min()))*255
    img = np.array(img).astype(np.uint8)
    img = cv2.applyColorMap(img, cv2.COLORMAP_JET)    
    return img

if __name__ == "__main__":
    args = get_args()
    name = os.path.split(args.image_path)[-1]
    img = hf_feature(args.image_path)
    cv2.imwrite(os.path.join(args.save_dir,name), img)
    
    