import cv2
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_path', type=str,
                        help='path of the input image.')
    parser.add_argument('--save_dir', type=str, default='output/',
                        help='saving path of the output image.')
    return parser.parse_args()


def laplacian(src):
    src = cv2.imread(src, cv2.IMREAD_COLOR)
    src = cv2.GaussianBlur(src, (3,3), 0)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    lap = cv2.Laplacian(gray, cv2.CV_16S, ksize=3)
    img = cv2.convertScaleAbs(lap)
    return img


if __name__ == '__main__':
    args = get_args()
    name = os.path.split(args.image_path)[-1]
    lap = laplacian(args.image_path)
    cv2.imwrite(os.path.join(args.save_dir,name), lap)
    