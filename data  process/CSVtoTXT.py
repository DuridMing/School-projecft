'''

(class , x1 , x2 , y1 , y2)

'''

import os
import pandas as pd
'''

(class , x1 , x2 , y1 , y2)

'''


class DIRError(Exception):
    pass


path = input("path :")

try:
    if os.path.isdir(path):
        print("find dir")
    elif not os.path.isdir(path):
        os.makedirs(path)
        print("create dir.")
    else:
        raise DIRError
except DIRError:
    print("cannot found dir : ", path)
temp_name = []

csv = pd.read_csv("person_annotations.csv", nrows=10)
file_name = csv.pop('file_name')
csv['classes'] = pd.Categorical(csv['classes'])
csv['classes'] = csv.classes.cat.codes
for name in file_name:
    temp_name.append(name.split("."))
    print(temp_name[0])
    file_name

print("split done.")

cla = csv['classes'].values
x1 = csv['x1'].values
x2 = csv['x2'].values
y1 = csv['y1'].values
y2 = csv['y2'].values
print("file num :", len(temp_name))

for num in range(len(temp_name)):
    # num +=1
    with open(path+"/"+str(temp_name[num][0])+".txt", "w") as txt:
        write_data = str(cla[num]) + " " + str(x1[num]) + " " + \
            str(x2[num]) + " " + str(y1[num]) + " " + str(y2[num])
        txt.write(write_data)
        txt.close()
