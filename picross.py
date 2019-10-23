from z3 import *
from solver import column, consecutive, nonconsecutive, none, one

##################
# 3x3 1-colour 1 #
##################

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

##################
# 3x3 1-colour 2 #
##################

nrows = 3
ncols = 3
puzzle = [[Bool(f'({row}, {col})') for col in range(ncols)] for row in range(nrows)]

rows = [
    consecutive(puzzle[0], 2),
    consecutive(puzzle[1], 2),
    none(puzzle[2]),
]

columns = [
    consecutive(column(puzzle, 0), 2),
    consecutive(column(puzzle, 1), 2),
    none(column(puzzle, 2)),
]

s = Solver()
s.add(rows + columns)

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(puzzle[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
else:
    print(unsat)

#################
# 5x5 2-colours #
#################

nrows = 5
ncols = 5
red = [[Bool(f"({row}, {col}, 'red')") for col in range(ncols)] for row in range(nrows)]
blue = [[Bool(f"({row}, {col}, 'blue')") for col in range(ncols)] for row in range(nrows)]

red_rows = [
    consecutive(red[0], 5),
    consecutive(red[1], 5),
    consecutive(red[2], 2),
    consecutive(red[3], 2),
    consecutive(red[4], 2),
]

blue_rows = [
    none(blue[0]),
    none(blue[1]),
    consecutive(blue[2], 3),
    consecutive(blue[3], 3),
    consecutive(blue[4], 3),
]

red_columns = [
    consecutive(column(red, 0), 2),
    consecutive(column(red, 1), 2),
    consecutive(column(red, 2), 2),
    consecutive(column(red, 3), 5),
    consecutive(column(red, 4), 5),
]

blue_columns = [
    consecutive(column(blue, 0), 3),
    consecutive(column(blue, 1), 3),
    consecutive(column(blue, 2), 3),
    none(column(blue, 3)),
    none(column(blue, 4)),
]

s = Solver()
s.add(red_rows + red_columns
      + blue_rows + blue_columns
      )

if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(red[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
    r = [[m.evaluate(blue[i][j]) for j in range(ncols)] for i in range(nrows)]
    print_matrix(r)
else:
    print(unsat)
