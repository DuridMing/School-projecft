import os
import pandas as pd
'''

(class , x1 , x2 , y1 , y2)

'''


def convert(size, box):
	dw = 1./size[0]
	dh = 1./size[1]
	x = box[0]*dw
	y = box[1]*dh
	w = box[2]*dw
	h = box[3]*dh
	return (x, y, w, h)

class DIRError(Exception):
    pass


path = input("path :")
label_name= input("label name : ")
label_classes ={"person" : 0 , "car" : 1}

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

csv = pd.read_csv(label_name + "_annotations.csv", nrows=10)
file_name = csv.pop('file_name')
csv['classes'] = pd.Categorical(csv['classes'])
# csv['classes'] = csv.classes.cat.codes
for name in file_name:
    temp_name.append(name.split("."))
    print(temp_name[0])


print("split done.")

cla = csv['classes'].values
x1 = csv['x1'].values
x2 = csv['x2'].values
y1 = csv['y1'].values
y2 = csv['y2'].values
print("file num :", len(temp_name))

for num in range(len(temp_name)):
    # num +=1
    f = "download_images-" + label_name + "/" + temp_name[num][0] + temp_name[num][1]
    if os.path.isfile(f):
        with open(path+"/"+str(temp_name[num][0])+".txt", "w") as txt:
            write_data = str(label_classes([cla[num]])) + " " + str(x1[num]) + " " + str(x2[num]) + " " + str(y1[num]) + " " + str(y2[num])
            txt.write(write_data)
        
        txt.close()
print("Convert to TXT done.")
