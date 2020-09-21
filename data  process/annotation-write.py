from pycocotools.coco import COCO
import requests
import os
import csv



coco = COCO('instances_val2017.json')
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)


with open('person_annotations' + '.csv', mode='w', newline='') as annot:
    for im in images:
        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        for i in range(len(anns)):
            annot_writer = csv.writer(annot)
            annot_writer.writerow(
                                [ im['file_name'],'person' ,
                                int(round(anns[i]['bbox'][0])),
                                int(round(anns[i]['bbox'][0]) + int(round(anns[i]['bbox'][2])) ),
                                int(round(anns[i]['bbox'][1])),
                                int(round(anns[i]['bbox'][1])) + int(round(anns[i]['bbox'][3]))]
                                )
print("writing csv. done.")

# coco dataset [top left x position, top left y position, width, height]
# lx , ly
