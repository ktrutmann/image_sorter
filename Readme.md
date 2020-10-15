# Image Sorter Script

I wrote this script because I wanted to quickly sort the images on my phone into "Keep", "Archive on HD" and "Delete" folders.
The goal was to make the process as fast as possible, making the sorting process more of a "guitar hero" experience where you only have to push one button in response to an image rather than drag and drop it.


## Usage

### Requirements
The script requires `python 3.6` or higher since I use the f-string feature.
Further modules that should be installed are `shutil`, `keyboard`, and `Pillow`.

### Setup
Drag the script in a top level folder in which you have a folder with the images as well as the folders you want them sorted into.
Set `source_folder` in the script to the folder with the pictures and use the `key_mappings` dict to map the keys you want to the destination folders. The sky is the limit! Well, the 36 alphanumerical keys on your keyboard minus b, a and q is the limit. But that's basically the sky.
`file_types` lets you choose what kind of pictures to look for and `img_display_height` sets the height in pixels in which the images will be displayed. Sometimes this doesn't work perfectly if for example you have very broad (panorama) pictures. If you have many of those consider setting up a "sort_manually" folder.

### Sorting
The prompt pretty much says it all.
Once the script started it will capture all keyboard inputs. That means you should make sure you have stopped the script before doing something else involving the keyboard.
Move the picture window to a place you're comfortable with and start sorting.
The actual files will only be moved once you are done, either because you have sorted all detected files or because you pressed the `a` key to apply the changes. If you want to quit the script without moving any files press `q` and confirm by typing `yes` into the console and hitting enter. Type anything else (or nothing) to continue.
If you have made a mistake you can go back one picture by pressing `b` (an advantage over the "move files immediately" method).

Happy sorting!

