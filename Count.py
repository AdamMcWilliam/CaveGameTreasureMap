import json
import numpy as np

f = open('1026.json')

data = json.load(f)
print(len(data['layers'][0]['data']))

##loop through and count instances

print (data['layers'][0]['data'][358331])

arr = np.array(data['layers'][0]['data'])


for i in range (70):
    count = (arr == i).sum()
    print(f"{i} : {count}")