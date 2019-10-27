import numpy as np
from skimage.feature import match_template
from skimage.filters import gaussian
from skimage.io import imread
from skimage.transform import hough_circle, hough_circle_peaks

RADII = np.arange(31, 36)
TEMPLATES = {i: gaussian(imread(f'templates/{i}.pbm')) for i in range(1, 12)}


def is_zero(im):
    # crop out a 5-pixel border along each edge
    # in case there are spurious pixels
    crop = im[5:-5, 5:-5]

    # return true if everything within the crop is the same
    unique = np.unique(crop)
    return unique.shape == (1,)


def is_connected(im):
    # Select the most prominent circle
    hough_res = hough_circle(im, RADII)
    [score], _, _, _ = hough_circle_peaks(hough_res, RADII, total_num_peaks=1)

    return score >= 0.3


def get_number(im):
    im = gaussian(im)
    scores = {i: np.max(match_template(im, tmpl)) for i, tmpl in TEMPLATES.items()}
    scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return scores[0][0]


def get_hint(im):
    if is_zero(im):
        return 0
    number = get_number(im)
    return -number if is_connected(im) else number


if __name__ == '__main__':
    import glob

    fs = glob.glob('data/edges/*.pbm')
    for f in sorted(fs):
        im = imread(f)
        print(f, get_hint(im))
