# photos-to-json

> A python script that scans all photos in a directory and creates a neat JSON file from it where each folder is an album.

*The directory walking is only one level deep, as depicted in the example below. If you want to have thumbnails for example i recommend putting them in a subfolder named thumbs in the album folder and naming the files the same. This way you can load the thumbnails by just appending /thumb.*

## Who is this for? 
This script is created for photographers and/or web developers who organize their photos into folders and want to keep track of them and/or display them on a website.

## Why is it useful? 
This json file can come in handly when loading images on a website since websites like to know the width and height of a photo before the image has been loaded to prevent content shift. It also comes in handy when lazy loading images, since you'll know which image is next. The script also computes if it's a portrait or landscape image, which can also help when designing a website or grid of images.

## Real world example
For a real world example, see <https://fredrik.studio>

## Folder structure
```
Directory
  - <folder-name>
    - filename.jpg
    - filename.jpg
  - <folder-name>
    - filename.jpg
    - filename.jpg
```
## Result
This python program will scan a folder and all its subfolders, look for all files with a jpg file extention and then create a JSON file with the following structure:
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

## Usage
```
Usage: `photos-to-json.py <photosDirectory> <jsonDirectory>`
Example: `photos-to-json.py /User/john/images /User/john/json`
```
**Note:** If the file `photos.json` already exist the exact path, then that files content will be copied into the new file and the existing information about a certain file will not be overwritten. This means that if you were to change a files name or resolution etc. then that will be carried over to the new file.  

## To-do

- Break up file into functions
