from z3 import And, Not, Or


def consecutive(cells, hint):
    possibilities = []
    for i in range(len(cells) - hint + 1):
        possibility = (cell if i <= j < i + hint else Not(cell) for j, cell in enumerate(cells))
        possibilities.append(And(*possibility))
    return Or(*possibilities)
