import time
import numpy as np
from PIL import Image
from numpy import asarray
import os

path = 'c:\\Users\\pnytko\\Desktop\\color\\'

header = 'Nazwa,Kolor 0,Kolor 1,Kolor 2,Kolor 3'
out = open('out.csv', 'w')
out.write(f'{header}\n')
def count_colors_2(cv_img, filename) -> list:
    from PIL import Image
    c_bgr_arr = []
    count_arr = []
    start_time = time.time()
    pil_image = Image.fromarray(cv_img)
    colors_count_list = pil_image.getcolors()
    print('\nPoliczenie kolorów zajęło: {:.10f}s\n'.format(time.time() - start_time))
    for count, c_bgr in colors_count_list:
        c_bgr_arr.append(c_bgr)
        count_arr.append(count)
        print(f'Kolor {c_bgr} pojawił się {count} razy')
    
    out.write(f'{filename},{count_arr[3]},{count_arr[2]},{count_arr[1]},{count_arr[0]}\n')

    return colors_count_list

for image in os.listdir(r'c:\Users\pnytko\Desktop\color'):
    if image.endswith('.tif'):
        print(f'Przetwarzam: {image}')
        img = Image.open(path+image)
        numpydata = asarray(img)
        count_colors_2(numpydata, image)

out.close()