"""
Solves a simple 2x2 picross puzzle with the following clues:

   ②  1  2
 2
②
 1
"""

from z3 import *
from solver import consecutive, nonconsecutive, one

nrows = 3
ncols = 3
puzzle = [[Bool(f'({row}, {col})') for col in range(ncols)] for row in range(nrows)]

row_0 = nonconsecutive(puzzle[0], 2)
row_1 = consecutive(puzzle[1], 2)
row_2 = one(puzzle[2])

col_0 = consecutive([puzzle[i][0] for i in range(nrows)], 2)
col_1 = one([puzzle[i][1] for i in range(nrows)])
col_2 = nonconsecutive([puzzle[i][2] for i in range(nrows)], 2)

s = Solver()
s.add(row_0, row_1, row_2, col_0, col_1, col_2)

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(puzzle[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
else:
    print(unsat)
