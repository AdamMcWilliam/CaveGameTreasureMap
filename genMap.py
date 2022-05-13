
import json
import numpy as np
from PIL import Image
import glob


f = open('1026.json')

data = json.load(f)
len = len(data['layers'][0]['data'])
arr = np.array(data['layers'][0]['data'])


width = 1405
height = 1405
img_wid = width *66
img_hei = height *66


new_im = Image.new('RGB', (img_wid, img_hei))


##select sprite id -1, place on map
for row in range (0,101):
    for col in range(0,101):
        loc = row*height + col
        #print(loc)
        sprite = data['layers'][0]['data'][loc] -1
        #print(sprite)
        small_img = Image.open(f"cavesprites/{sprite}.png")
        new_im.paste(small_img, ((col*66), (row*66)))

new_im.show()
new_im.save('full_image.jpg', quality = 90)