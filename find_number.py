import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.feature import match_template
from skimage.filters import gaussian


def find_number(tmpl, im, ax):
    result = match_template(im, tmpl)
    ij = np.unravel_index(np.argmax(result), result.shape)
    x, y = ij[::-1]

    ax.imshow(im, cmap=plt.cm.gray)
    ax.set_axis_off()
    # highlight matched region
    h, w = tmpl.shape
    rect = plt.Rectangle((x, y), w, h, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    offset = (x + w // 2) - (im.shape[1] // 2)
    return np.max(result), np.abs(offset)


image = io.imread('data/edges/0001_col6_2.pbm')
image = gaussian(image, sigma=2)

fig, axes = plt.subplots(nrows=15, ncols=2, figsize=(4, 30))

for i in range(0, 30, 2):
    ax1 = axes[np.unravel_index(i, (15, 2))]

    template = io.imread(f'templates/{i // 2 + 1}.pbm')
    template = gaussian(template, sigma=2)
    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()

    ax2 = axes[np.unravel_index(i + 1, (15, 2))]
    score, offset = find_number(template, image, ax2)
    ax2.set_title(f'{i}: {score:.3}, {offset}')

plt.show()
