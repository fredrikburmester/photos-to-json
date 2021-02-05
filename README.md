# photos-to-json
A python program for scanning all photos in a folder(s) and create a neat JSON file from it.

This python program will scan a folder and all its subfolders, look for all files with a jpg file extention and then create a JOSN file with the following structure:
```
[{
  title ""
  album "<folder-name>"
  filename "<filename>"
  display "<vertical|landscape"
  x = <width in px>
  y = <height in px>
}]
```
