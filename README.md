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
The exported filename is `photos.json`. The export path is hardcoded.

**Note:** If the file `photos.json` already exist the exact path, then that files content will be copied into the new file and the existing information about a certain file will not be overwritten. This means that if you were to change a files name or resolution etc. then that will be carried over to the new file.  
