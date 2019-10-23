from z3 import And, If, Not, Or, Sum


def consecutive(cells, hint):
    possibilities = []
    for i in range(len(cells) - hint + 1):
        possibility = (cell if i <= j < i + hint else Not(cell) for j, cell in enumerate(cells))
        possibilities.append(And(*possibility))
    return Or(*possibilities)


def nonconsecutive(cells, hint):
    return And(Sum([If(cell, 1, 0) for cell in cells]) == hint,
               Not(consecutive(cells, hint)))
