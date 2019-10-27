import numpy as np
import toml
from skimage import io
from skimage.feature import canny

from classify import get_hint

if __name__ == '__main__':
    import sys

    fname = sys.argv[1]
    puzzle = io.imread(fname, as_gray=True)

    nrows = 15
    ncols = 10
    ncolours = 4

    row_hints = []
    rows = puzzle[632:1757, 38:294]
    rows = np.vsplit(rows, nrows)
    for i, row in enumerate(rows):
        row_hints.append([])
        hints = np.hsplit(row, ncolours)
        for j, hint in enumerate(hints):
            hint = canny(hint)
            hint_value = get_hint(hint)
            row_hints[-1].append(hint_value)
            print(hint_value, end=' ')
        print()

    print()

    column_hints = []
    columns = puzzle[371:627, 297:1047]
    columns = np.hsplit(columns, ncols)
    for i, column in enumerate(columns):
        column_hints.append([])
        hints = np.vsplit(column, ncolours)
        for j, hint in enumerate(hints):
            hint = canny(hint)
            hint_value = get_hint(hint)
            column_hints[-1].append(hint_value)
            print(hint_value, end=' ')
        print()

    serialised_puzzle = {
        'nrows': nrows,
        'ncols': ncols,
        'ncolours': ncolours,
        'rows': row_hints,
        'columns': column_hints,
    }

    output_file = sys.argv[2]
    with open(output_file, 'w') as f:
        toml.dump(serialised_puzzle, f)
