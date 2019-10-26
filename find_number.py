import numpy as np
import matplotlib.pyplot as plt

from skimage import data, io, img_as_bool
from skimage.feature import match_template

image = io.imread('data/edges/0295.png')
image = img_as_bool(image)

image2 = io.imread('data/edges/0068.png')
image2 = img_as_bool(image2)

image3 = io.imread('data/edges/0405.png')
image3 = img_as_bool(image3)

template = io.imread('3.png')
template = img_as_bool(template)

result = match_template(image, template)
print(np.max(result))
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

fig, axes = plt.subplots(nrows=1, ncols=4)
ax1, ax2, ax3, ax4 = axes

ax1.imshow(template, cmap=plt.cm.gray)
ax1.set_axis_off()

ax2.imshow(image, cmap=plt.cm.gray)
ax2.set_axis_off()
ax2.set_title(format(np.max(result), '.4f'))
# highlight matched region
w, h = template.shape
rect = plt.Rectangle((x, y), h, w, edgecolor='r', facecolor='none')
ax2.add_patch(rect)

result = match_template(image2, template)
print(np.max(result))
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

ax3.imshow(image2, cmap=plt.cm.gray)
ax3.set_axis_off()
ax3.set_title(format(np.max(result), '.4f'))
# highlight matched region
w, h = template.shape
rect = plt.Rectangle((x, y), h, w, edgecolor='r', facecolor='none')
ax3.add_patch(rect)

result = match_template(image3, template)
print(np.max(result))
ij = np.unravel_index(np.argmax(result), result.shape)
x, y = ij[::-1]

ax4.imshow(image3, cmap=plt.cm.gray)
ax4.set_axis_off()
ax4.set_title(format(np.max(result), '.4f'))
# highlight matched region
w, h = template.shape
rect = plt.Rectangle((x, y), h, w, edgecolor='r', facecolor='none')
ax4.add_patch(rect)

plt.show()
