from pycocotools.coco import COCO
import requests
import os
import csv


def convert(size, box):
	dw = 1./size[0]
	dh = 1./size[1]
	x = box[0]*dw
	y = box[1]*dh
	w = box[2]*dw
	h = box[3]*dh
	return (x, y, w, h)

label_name = input("input label name :")

coco = COCO('instances_val2017.json')
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=[label_name])
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)


with open(label_name + '_annotations' + '.csv', mode='w', newline='') as annot:
    
    annot_writer = csv.writer(annot)
    annot_writer.writerow(["file_name", "classes", "x1", "x2", "y1", "y2"])

    for im in images:
        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        
        width = im['width']
        height = im['height']
        for i in range(len(anns)):
            box = [int(round(anns[i]['bbox'][0])),
                int(round(anns[i]['bbox'][1])),
                int(round(anns[i]['bbox'][2])),
                int(round(anns[i]['bbox'][3])),
                ]
            bb = convert((width, height),box)
            # annot_writer = csv.writer(annot)
            annot_writer.writerow([im['file_name'], 
                                    label_name , 
                                    bb[0] , 
                                    bb[1] , 
                                    bb[2] , 
                                    bb[3]])

            print(bb)
print("writing csv. done.")

# coco dataset [top left x position, top left y position, width, height]
# lx , ly
