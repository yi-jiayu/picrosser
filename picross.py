"""
Solves a simple 2x2 picross puzzle with the following clues:

   ②  1  2
 2
②
 1
"""

from z3 import *
from solver import consecutive

nrows = 3
ncols = 3
puzzle = [[Bool(f'({row}, {col})') for col in range(ncols)] for row in range(nrows)]

row_0 = And(puzzle[0][0], puzzle[0][2])
row_1 = consecutive(puzzle[1], 2)
row_2 = Or(And(puzzle[2][0], Not(puzzle[2][1]), Not(puzzle[2][2])),
           And(Not(puzzle[2][0]), puzzle[2][1], Not(puzzle[2][2])),
           And(Not(puzzle[2][0]), Not(puzzle[2][1]), puzzle[2][2]))

col_0 = consecutive([puzzle[i][0] for i in range(nrows)], 2)
col_1 = Or(And(puzzle[0][1], Not(puzzle[1][1]), Not(puzzle[2][1])),
           And(Not(puzzle[0][1]), puzzle[1][1], Not(puzzle[2][1])),
           And(Not(puzzle[0][1]), Not(puzzle[1][1]), puzzle[2][1]))
col_2 = And(puzzle[0][2], puzzle[2][2])

s = Solver()
s.add(row_0, row_1, row_2, col_0, col_1, col_2)

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(puzzle[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
else:
    print(unsat)
