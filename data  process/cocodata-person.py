from pycocotools.coco import COCO
import requests
import os 
import csv


class DIRError(Exception):
    pass

try:
    if os.path.isdir("downloaded_images-person"):
        print("find dir")
    elif not os.path.isdir("downloaded_images-person"):
        os.makedirs("downloaded_images-person")
        print("create dir.")
    else :
        raise DIRError
except DIRError :
    print("cannot found dir : downloaded_images-person")

coco = COCO('instances_val2017.json')
cats = coco.loadCats(coco.getCatIds())
nms = [cat['name'] for cat in cats]
# print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)
# print("imgIds: ", imgIds)
# print("images: ", images)

# for wirting img and csv
for im in images:
    print("im: ", im)
    img_data = requests.get(im['coco_url']).content
    with open('downloaded_images-person/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)
with open('person_annotations_download' + '.csv', mode='w', newline='') as annot:
    for im in images:
        annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
        anns = coco.loadAnns(annIds)
        for i in range(len(anns)):
            annot_writer = csv.writer(annot)
            annot_writer.writerow(['downloaded_images-person/' + im['file_name'], int(round(anns[i]['bbox'][0])), int(round(anns[i]['bbox'][1])),
                       int(round(anns[i]['bbox'][0] + anns[i]['bbox'][2])), int(round(anns[i]['bbox'][1] + anns[i]['bbox'][3])), 'person'])

# coco dataset [top left x position, top left y position, width, height]
# lx , ly 