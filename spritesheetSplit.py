from PIL import Image
from os import mkdir

#mkdir("cavesprites/")
sheet = Image.open("cavesprites.png")
count = 0

for y in range(4):
    for x in range(16):
        a = (x + 1) * 66
        b = (y + 1) * 66
        icon = sheet.crop((a - 66, b - 66, a, b))  # Problem here
        icon.save("cavesprites/{}.png".format(count))
        count += 1