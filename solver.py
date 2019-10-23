import itertools
from z3 import And, If, Not, Or, Sum


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


def none(cells):
    return And([Not(cell) for cell in cells])


def exclusive(*cells):
    cells = (itertools.chain.from_iterable(cells) for cells in cells)
    return And([Sum([If(cell, 1, 0) for cell in corresponding_cells]) <= 1 for corresponding_cells in zip(*cells)])