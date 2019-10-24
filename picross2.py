from z3 import Solver, Bool, sat, unsat, print_matrix

from solver import column, exclusive, constraint

##################
# 15x10 4-colour #
##################

nrows = 15
ncols = 10
ncolours = 4
colours = [[[Bool(f'({row}, {col}, {colour})')
             for col in range(ncols)]
            for row in range(nrows)]
           for colour in range(ncolours)]

row_hints = [
    [9, 8, 8, 4, 5, 5, 5, 3, 2, 0, 0, 0, 0, 0, 0],
    [1, -2, 1, 6, 4, 5, 4, 4, 5, -2, -2, -2, 0, 3, 4],
    [0, 0, 0, 0, 0, 0, 0, -3, 1, 4, 3, 2, 2, 3, 2],
    [0, 0, 1, 0, 1, 0, 1, 0, -2, 4, 5, 6, 8, 4, 4]
]

column_hints = [
    [-9, -8, -3, -3, -9, -7, 1, 0, 6, -3],
    [0, 1, -6, 11, 5, 0, -6, 4, 4, 8],
    [-6, 1, 1, 0, 0, 1, 3, -8, 0, 0],
    [0, -5, -5, 1, 1, -7, 5, 3, -5, -4]
]

constraints = []

for colour, row in enumerate(row_hints):
    for i, hint in enumerate(row):
        cells = colours[colour][i]
        constraints.append(constraint(cells, hint))

for colour, row in enumerate(column_hints):
    for i, hint in enumerate(row):
        cells = column(colours[colour], i)
        constraints.append(constraint(cells, hint))

s = Solver()
s.add(constraints)
s.add(exclusive(*colours))

if s.check() == sat:
    m = s.model()
    solution = [[0 for j in range(ncols)] for i in range(nrows)]
    for colour, matrix in enumerate(colours):
        r = [[m.evaluate(matrix[i][j]) for j in range(ncols)] for i in range(nrows)]
        for i in range(nrows):
            for j in range(ncols):
                if r[i][j]:
                    solution[i][j] = colour + 1
    print_matrix(solution)
else:
    print(unsat)
