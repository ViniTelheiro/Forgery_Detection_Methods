import argparse
from PIL import Image, ImageChops, ImageEnhance
import os

from yaml import parse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', type=str,
                        help='path of the input image')
    parser.add_argument('--save_dir', type=str, default='output/',
                        help='saving path of the output')
    args = parser.parse_args()
    return args


def ela(fname, orig_dir, save_dir):
    TMP_EXT = ".tmp_ela.jpg"
    ELA_EXT = ".ela.png"
    SAVE_REL_DIR = "generated"
    threads = []
    quality = 90
    """
    Generates an ELA image on save_dir.
    Params:
        fname:      filename w/out path
        orig_dir:   origin path
        save_dir:   save path
    """
    basename, ext = os.path.splitext(fname)

    org_fname = os.path.join(orig_dir, fname)
    tmp_fname = os.path.join(save_dir, basename + TMP_EXT)
    ela_fname = os.path.join(save_dir, basename + ELA_EXT)

    im = Image.open(org_fname)
    im.save(tmp_fname, 'JPEG', quality=quality)

    tmp_fname_im = Image.open(tmp_fname)
    ela_im = ImageChops.difference(im, tmp_fname_im)

    extrema = ela_im.getextrema()
    max_diff = max([ex[1] for ex in extrema])
    scale = 255.0/max_diff
    ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)

    ela_im.save(ela_fname)
    os.remove(tmp_fname)


if __name__ == "__main__":
    args = get_args()
    name = os.path.split(args.image_dir)[-1]
    dir = os.path.split(args.image_dir)[0]
    save = args.save_dir
    img = ela(name,dir,save)    
    
