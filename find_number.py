import matplotlib.pyplot as plt
import numpy as np
from skimage import io, img_as_bool
from skimage.feature import match_template


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


image = io.imread('data/edges/0904.png')
image = img_as_bool(image)

fig, axes = plt.subplots(nrows=11, ncols=2, figsize=(4, 22))

for i in range(0, 22, 2):
    ax1 = axes[np.unravel_index(i, (11, 2))]

    template = io.imread(f'templates/{i // 2 + 1}.png')
    template = img_as_bool(template)
    ax1.imshow(template, cmap=plt.cm.gray)
    ax1.set_axis_off()

    ax2 = axes[np.unravel_index(i + 1, (11, 2))]
    score, offset = find_number(template, image, ax2)
    ax2.set_title(f'{i}: {score:.3}, {offset}')

plt.show()
