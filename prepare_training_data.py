import os.path

import numpy as np
from PIL import Image
from skimage import io, feature, img_as_uint

PUZZLES_DIR = 'data/puzzles'
HINTS_DIR = 'data/hints'
EDGES_DIR = 'data/edges'


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def save(hint, puzzle, orientation, i, j):
    global index

    io.imsave(os.path.join(HINTS_DIR, f'{index:04}.png'), img_as_uint(hint), check_contrast=False)
    hint = feature.canny(hint)
    # use PIL to save as bitmap PBM images
    # because skimage doesn't seem to support 1-bit resolution
    Image.fromarray(hint).save(os.path.join(EDGES_DIR, f'{puzzle.split(".")[0]}_{orientation}{i}_{j}.pbm'))
    index += 1


if __name__ == '__main__':
    mkdir(HINTS_DIR)
    mkdir(EDGES_DIR)

    index = 0

    for puzzle in sorted(os.listdir(PUZZLES_DIR)):
        fname = os.path.join(PUZZLES_DIR, puzzle)
        im = io.imread(fname, as_gray=True)

        columns = im[371:627, 297:1047]
        columns = np.hsplit(columns, 10)
        for i, column in enumerate(columns):
            hints = np.vsplit(column, 4)
            for j, hint in enumerate(hints):
                save(hint, puzzle, 'col', i, j)

        rows = im[632:1757, 38:294]
        rows = np.vsplit(rows, 15)
        for i, row in enumerate(rows):
            hints = np.hsplit(row, 4)
            for j, hint in enumerate(hints):
                save(hint, puzzle, 'row', i, j)
