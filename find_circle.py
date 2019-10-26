import matplotlib.pyplot as plt
from skimage import color
from skimage import io, img_as_ubyte
from skimage.draw import circle_perimeter
from skimage.feature import canny
from skimage.transform import hough_circle, hough_circle_peaks
import numpy as np

RADII = np.arange(31, 36)


def find_circles(im):
    edges = canny(im)
    hough_res = hough_circle(edges, RADII)

    # Select the most prominent 3 circles
    accums, cx, cy, radii = hough_circle_peaks(hough_res, RADII, total_num_peaks=3)
    print(list(zip(accums, radii)))

    # Draw them
    im = img_as_ubyte(color.gray2rgb(im))
    for center_y, center_x, radius in zip(cy, cx, radii):
        circy, circx = circle_perimeter(center_y, center_x, radius, shape=im.shape)
        im[circy, circx] = (220, 20, 20)

    return im


connected = io.imread('data/hints/0015.png')
disconnected = io.imread('data/hints/0021.png')
fig3 = io.imread('data/hints/0040.png')
fig4 = io.imread('data/hints/0041.png')

fig, axes = plt.subplots(nrows=2, ncols=2)

axes[0, 0].imshow(find_circles(connected), cmap=plt.cm.gray)
axes[0, 1].imshow(find_circles(disconnected), cmap=plt.cm.gray)
axes[1, 0].imshow(find_circles(fig3), cmap=plt.cm.gray)
axes[1, 1].imshow(find_circles(fig4), cmap=plt.cm.gray)

plt.show()
