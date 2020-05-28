import os
import random
 
val_percent = 0.5
xmlfilepath = 'Annotations'
txtsavepath = 'ImageSets'
total_xml = os.listdir(xmlfilepath)
 
num = len(total_xml)
list = range(num)
tv = int(num * val_percent)
val = random.sample(list, tv)

ftrain = open('ImageSets/train.txt', 'w')
fval = open('ImageSets/val.txt', 'w')
 
for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in val:
        fval.write(name)
    else:
        ftrain.write(name)
 

ftrain.close()
fval.close()