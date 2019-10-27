from classify import is_zero, get_number
from skimage import io
import os
import glob
import shutil

shutil.rmtree('data/sorted')
os.mkdir('data/sorted')

for i in range(16):
    os.mkdir(f'data/sorted/{i}')

for f in glob.glob('data/edges/*.pbm'):
    im = io.imread(f)
    if is_zero(im):
        print(f'{f}: 0')
        shutil.copy(f, 'data/sorted/0')
    else:
        number = get_number(im)
        print(f'{f}: {number}')
        shutil.copy(f, f'data/sorted/{number}')
