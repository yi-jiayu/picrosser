import itertools
from z3 import And, Bool, If, Not, Or, Solver, Sum, sat


def column(puzzle, n):
    return [row[n] for row in puzzle]


def consecutive(cells, hint):
    return Or([And([cell if i <= j < i + hint else Not(cell) for j, cell in enumerate(cells)])
               for i in range(len(cells) - hint + 1)])


def nonconsecutive(cells, hint):
    return And(Sum([If(cell, 1, 0) for cell in cells]) == hint,
               Not(consecutive(cells, hint)))


def one(cells):
    return Or([And([cell if i == j else Not(cell) for j, cell in enumerate(cells)])
               for i in range(len(cells))])


def constraint(cells, hint):
    if hint == 0:
        return none(cells)
    elif hint == 1:
        return one(cells)
    elif hint < 0:
        return consecutive(cells, -hint)
    else:
        return nonconsecutive(cells, hint)


def none(cells):
    return And([Not(cell) for cell in cells])


def exclusive(*cells):
    cells = (itertools.chain.from_iterable(cells) for cells in cells)
    return And([Sum([If(cell, 1, 0) for cell in corresponding_cells]) <= 1 for corresponding_cells in zip(*cells)])


def solve(puzzle):
    nrows = puzzle['nrows']
    ncols = puzzle['ncols']
    ncolours = puzzle['ncolours']

    colours = [[[Bool(f'({row}, {col}, {colour})')
                 for col in range(ncols)]
                for row in range(nrows)]
               for colour in range(ncolours)]

    row_hints = puzzle['rows']
    column_hints = puzzle['columns']

    constraints = []

    for i, hints in enumerate(row_hints):
        for colour, hint in enumerate(hints):
            cells = colours[colour][i]
            constraints.append(constraint(cells, hint))

    for i, hints in enumerate(column_hints):
        for colour, hint in enumerate(hints):
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
        return solution
