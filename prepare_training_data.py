import os.path

import numpy as np
from skimage import io, feature, img_as_uint

PUZZLES_DIR = 'data/puzzles'
HINTS_DIR = 'data/hints'
EDGES_DIR = 'data/edges'


def mkdir(path):
    try:
        os.mkdir(path)
    except FileExistsError:
        pass


def save(hint):
    global index

    io.imsave(os.path.join(HINTS_DIR, f'{index:04}.png'), img_as_uint(hint))
    hint = feature.canny(hint)
    io.imsave(os.path.join(EDGES_DIR, f'{index:04}.png'), img_as_uint(hint))
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
                save(hint)

        rows = im[632:1757, 38:294]
        rows = np.vsplit(rows, 15)
        for i, row in enumerate(rows):
            hints = np.hsplit(row, 4)
            for j, hint in enumerate(hints):
                save(hint)
