import matplotlib.pyplot as plt
from skimage import color
from skimage import io, img_as_ubyte
from skimage.draw import circle_perimeter
from skimage.feature import canny
from skimage.transform import hough_circle, hough_circle_peaks
import numpy as np

RADII = np.arange(31, 36)


def find_circles(im, ax):
    edges = canny(im)
    hough_res = hough_circle(edges, RADII)

    # Select the most prominent 3 circles
    [score], [cx], [cy], [radius] = hough_circle_peaks(hough_res, RADII, total_num_peaks=1)

    # Draw them
    im = img_as_ubyte(color.gray2rgb(im))
    circy, circx = circle_perimeter(cy, cx, radius, shape=im.shape)
    im[circy, circx] = (220, 20, 20)

    ax.imshow(im, cmap=plt.cm.gray)
    ax.set_title(f'{score:.3} (radius: {radius})')


connected = io.imread('data/hints/0015.png')
disconnected = io.imread('data/hints/0021.png')
fig3 = io.imread('data/hints/0040.png')
fig4 = io.imread('data/hints/0041.png')

fig, axes = plt.subplots(nrows=2, ncols=2)

find_circles(connected, axes[0, 0])
find_circles(disconnected, axes[0, 1])
find_circles(fig3, axes[1, 0])
find_circles(fig4, axes[1, 1])

plt.show()
