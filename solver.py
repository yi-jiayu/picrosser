from z3 import And, If, Not, Or, Sum


def consecutive(cells, hint):
    return Or([And([cell if i <= j < i + hint else Not(cell) for j, cell in enumerate(cells)])
               for i in range(len(cells) - hint + 1)])


def nonconsecutive(cells, hint):
    return And(Sum([If(cell, 1, 0) for cell in cells]) == hint,
               Not(consecutive(cells, hint)))


def one(cells):
    return Or([And([cell if i == j else Not(cell) for j, cell in enumerate(cells)])
               for i in range(len(cells))])
