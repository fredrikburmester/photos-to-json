# Photos -> JSON

> A python script that scans all photos in a directory and creates a neat JSON file from it where each folder is an album.

*The directory walking is only one level deep, as depicted in the example below. If you want to have thumbnails for example i recommend putting them in a subfolder named thumbs in the album folder and naming the files the same. This way you can load the thumbnails by just appending /thumb.*

## 🤖 Who is this for?
This script is created for photographers and/or web developers who organize their photos into folders and want to keep track of them and/or display them on a website.

## 🤷🏻‍♂️ Why is it useful?
This json file can come in handly when loading images on a website since websites like to know the width and height of a photo before the image has been loaded to prevent content shift. It also comes in handy when lazy loading images, since you'll know which image is next. The script also computes if it's a portrait or landscape image, which can also help when designing a website or grid of images.

## 🌐 Real world example 
For a real world example, see <https://fredrik.studio>

## 📂 Folder structure 
```
Directory
  - <folder-name>
    - filename.jpg
    - filename.jpg
  - <folder-name>
    - filename.jpg
    - filename.jpg
```
## 🎉 Result
The JSON file will have the following structure:
```
[{
  title ""
  album "<folder-name>"
  filename "<filename>"
  display "<tall|wide>"
  x = <width in px>
  y = <height in px>
}]
```

The exported filename is `photos.json`.

## 🧑🏻‍💻 Usage
Example:
```
virtual env . 
source bin/activate
pip install -r requirements.txt
photos-to-json.py /User/john/images /User/john/json
```

## To-do

- Break up file into functions
