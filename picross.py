"""
Solves a simple 2x2 picross puzzle with the following clues:

   ②  1  2
 2
②
 1
"""

from z3 import *
from solver import column, consecutive, nonconsecutive, one

nrows = 3
ncols = 3
puzzle = [[Bool(f'({row}, {col})') for col in range(ncols)] for row in range(nrows)]

row_0 = nonconsecutive(puzzle[0], 2)
row_1 = consecutive(puzzle[1], 2)
row_2 = one(puzzle[2])

col_0 = consecutive(column(puzzle, 0), 2)
col_1 = one(column(puzzle, 1))
col_2 = nonconsecutive(column(puzzle, 2), 2)

s = Solver()
s.add(row_0, row_1, row_2, col_0, col_1, col_2)

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(puzzle[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
else:
    print(unsat)
