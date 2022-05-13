from tqdm import tqdm
import json
import numpy as np
from PIL import Image
from pathlib import Path
import glob


with open(Path('1026.json')) as f:
    data = json.load(f)
len = len(data['layers'][0]['data'])
arr = np.array(data['layers'][0]['data'])

iterations = 703
sprite_size = 33
width = 1405
height = 1405
img_wid = width * sprite_size
img_hei = height * sprite_size

new_im = Image.new('RGBA', (img_wid, img_hei))

# select sprite id -1, place on map
for row in tqdm(range (0, width)):
    for col in range(0, height):
        loc = row*height + col
        sprite = data['layers'][0]['data'][loc] -1
        #print(sprite)
        small_img = Image.open(Path(f"cavesprites/{sprite}.png"))
        new_im.paste(small_img, ((col * sprite_size), (row * sprite_size)))

new_im.save(Path('full_image.png'))
