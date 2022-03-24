import json
import os
import sys
from PIL import Image
from os import walk
from natsort import natsorted, ns

try:
    if len(sys.argv) != 3:
        print("Usage: photos-to-json.py <photosDirectory> <jsonDirectory>")
        sys.exit(1)
    photosDirectory = sys.argv[1]
    jsonDirectory = sys.argv[2] + '/photos.json'
    if not os.path.isdir(photosDirectory) and not os.path.isdir(jsonDirectory):
        print("Directory not found. Please check the path.")
        sys.exit(1)
except:
    print("Missing agruments. Usage: photos-to-json.py <photosDirectory> <jsonDirectory>")
    sys.exit(1)


# try to open json file, if fail, create it
try:
    print("Trying to find existing json file...")
    with open(jsonDirectory, "r") as file:
        data = json.load(file)
    print("Found existing json file.")
except:
    print("[Error] Json file not found. Creating new one...")
    with open(jsonDirectory, 'w') as outfile:
        outfile.write('[]')
    
    try:
        print("Trying again...")
        with open(jsonDirectory, "r") as file:
            data = json.load(file)
        print("Found json file.")
    except:
        print("[Error] Something went wrong. Please check the path.")
        sys.exit(1)

print("\nReading photos from " + photosDirectory)
print("Writing json to " + jsonDirectory)

g = open(jsonDirectory, 'w') # open json file

console = sys.stdout
sys.stdout = g # redirect output to json file

f = []
id = 0
ignored_files= [".DS_Store"]

print('[')
sys.stdout = console # redirect output back to console

def replaceUTFCharacters(s):
    s.replace("\u00f6", "o\u0308") # ö
    s.replace("\u00D6", "O\u0308") # Ö
    s.replace("\u00E4", "a\u0308") # ä
    s.replace("\u00C4", "A\u0308") # Ä
    return s

def getBackUTFCharacters(s):
    s.replace("o\u0308", "\u00f6") # ö
    s.replace("O\u0308", "\u00D6") # Ö
    s.replace("a\u0308", "\u00E4") # ä
    s.replace("A\u0308", "\u00C4") # Ä
    return s

def getOrientation(i):
    if i.size[0] / i.size[1] > 1: 
        return 'wide'
    else:
        return 'tall'


for dirname in walk(photosDirectory):
    for album in dirname[1]:
        album = replaceUTFCharacters(album)

        sys.stdout = console
        print("Processing: " + album)

        albumImages = []
        for image in walk(photosDirectory + '/' + album):
            # Get filename
            for filename in image[2]: 
                print(" - " + filename)
                if filename not in ignored_files:
                    filename = replaceUTFCharacters(filename)
                    albumImages.append(filename)
                else: 
                    print("   - [Ignored] " + filename)

            albumImages = natsorted(albumImages, reverse=True)

        for filename in albumImages:
            im = Image.open(photosDirectory + '/' + album + '/' + filename)

            orientation = getOrientation(im)

            for(x) in (data):
                if(x['filename'] == filename and x['album'] == album):
                    title = x['title']
                    orientation = x['display']

            album = getBackUTFCharacters(album)

            jsonitem = {
                'id': id,
                'title': '',
                'album': str(album),
                'filename': filename,
                'display': orientation,
                'x': im.size[0],
                'y': im.size[1]
            }

            student_dumped = json.dumps(jsonitem)

            sys.stdout = g # redirect output to json file
            
            if id != 0:
                print(',')
            id += 1

            print(student_dumped)
print(']')
