import toml
from solver import solve
import numpy as np
from PIL import Image

with open('puzzle2.toml') as f:
    puzzle = toml.load(f)

solution = solve(puzzle)
for row in solution:
    print(row)

colours = [[0, 71, 119],
           [163, 0, 0],
           [255, 119, 0],
           [239, 210, 141]]

coloured_solution = np.array([[colours[col - 1] for col in row] for row in solution], dtype=np.uint8)
img = Image.fromarray(coloured_solution, mode='RGB')
img = img.resize((200, 300))
img.save('output.png')
img.show()
