import json
import os
import sys
from PIL import Image
from os import walk
from natsort import natsorted, ns

j = open("/unraid-data/appdata/NginxProxyManager/static/json/photos.json",) 
data = json.load(j) 
g = open("/unraid-data/appdata/NginxProxyManager/static/json/photos.json", 'w')
sys.stdout = g

mypath = "/unraid-data/appdata/NginxProxyManager/static/images"

firstTime = 0

f = []
print('[')
id = 0
for dirname in walk(mypath):
    for album in dirname[1]:
        album.replace("\u00f6", "o\u0308")
        currentImage = []
        for image in walk(mypath + '/' + album):
            counter = 0
            for i in image[2]:
                if i != ".DS_Store":
                    name = i.split('.')[0]
                    if len(name) > 0:
                        currentImage.append(name)
                        counter += 1
            currentImage = natsorted(currentImage, reverse=True)
            counter = 0
            for i in currentImage:
                currentImage[counter] = str(currentImage[counter]) + '.jpg'
                counter += 1
            for filename in currentImage:
                im = Image.open(mypath + '/' + album + '/' + filename)
                display = ''
                if im.size[0]/im.size[1] > 1: 
                  display = 'wide'
                else:
                  display = 'tall'
                for(x) in (data):
                    if(x['filename'] == filename and x['album'] == album):
                        title = x['title']
                        display = x['display']
                album = album.replace("o\u0308","\u00f6")
                jsonitem = {
                    'id': id,
                    'title': '',
                    'album': str(album),
                    'filename': filename,
                    'display': display,
                    'x': im.size[0],
                    'y': im.size[1]
                }
                id += 1
                student_dumped = json.dumps(jsonitem)
                if firstTime == 1:
                  print(',')
                print(student_dumped)
                firstTime = 1
            break
        
    break
print(']')
