## Assignment Task

Create these modules:
1. jpg/jpeg to png conversion (use PIL library) j2p
2. png to jpg conversion (use PIL library) p2j

Image resizer that can resize bulk images with these features:
1. resize by user determined percentage (say 50% for height and width) (proportional) res_p
2. resize by user determined width (proportional) res_w
3. resize by user determined height (proportional) res_h

Image cropper that can crop bulk images with these features:
1. center square/rectangle crop by user-determined pixels crp_px
2. centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p

It let's user know which all images were not cropped due to size mismatches
a __main__ module that exposes all these features (using argparse)
finally create an zipped app, that exposes all of these features

How to test your code:
each module must be independently available and tested (write test to check whether you can call them from command line) 
each feature must be available via argument selection
images must not be required to be in the same folder where your code is

Final test:
1. download 20 jpeg images of size more than 1000x1000
2. convert to png
3. convert to jpg
4. resize to 80%
5. resize to 500 width
6. resize to 500 height

all this using your zipped app
center crop to 224x224

You must have at least 20+ test. (github actions)
Each test is worth 50 points (no additional points for more tests). So total 1000 pts.
Failing test, reduces mark. 

## Package Usage

```
usage: image_util_modules [-h] {j2p,p2j,res_p,res_w,res_h,crp_px,crp_p} ...

positional arguments:
  {j2p,p2j,res_p,res_w,res_h,crp_px,crp_p}
                        Choose a functionality.
    j2p                 jpg/jpeg to png conversion
    p2j                 png to jpg conversion
    res_p               image resize using realtive percentage
    res_w               image resize to new width
    res_h               image resize to new height
    crp_px              center crop images of required dimensions
    crp_p               center crop images of required relative percentage
```

## Modules

A module allows you to logically organize your Python code. Grouping related code into a module makes the code easier to understand and use. A module is a Python object with arbitrarily named attributes that you can bind and reference.

Simply, a module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

When you import a module, the Python interpreter searches for the module in the following sequences −

The current directory.

If the module isn't found, Python then searches each directory in the shell variable PYTHONPATH.

If all else fails, Python checks the default path. On UNIX, this default path is normally /usr/local/lib/python/.

The module search path is stored in the system module sys as the sys.path variable. The sys.path variable contains the current directory, PYTHONPATH, and the installation-dependent default.



### JPG/JPEG to PNG Conversion

Converts a single image from *jpg/jpeg* format to *png* format.

> usage: image_util_modules j2p [-h] -ip IMAGE_PATH

### PNG to JPG Conversion

Converts a single image from *png* format to *jpg* format.

> usage: image_util_modules p2j [-h] -ip IMAGE_PATH

### Resize using Percentage

Resizes and saves bulk of images by altering the size by given relative percentage.

> usage: image_util_modules res_p [-h] -fp FOLDER_PATH -p PERCENTAGE

### Resize using Width

Resizes and saves bulk of images by changing the width of the images as provided by the user and the height is calculated according to the aspect ratio.

> usage: image_util_modules res_w [-h] -fp FOLDER_PATH -w WIDTH

### Resize using Height

Resizes and saves bulk of images by changing the height of the images as provided by the user and the width is calculated according to the aspect ratio.

> usage: image_util_modules res_h [-h] -fp FOLDER_PATH -H HEIGHT

### Crop by pixel

Center crops bulk of images by a given height and width, pixel value provided by the user. If the input size exceeds the size of any image, it's not processed and the name is printed in the end.

> usage: image_util_modules crp_px [-h] -fp FOLDER_PATH -w WIDTH -H HEIGHT

### Crop by percentage

Center crops bulk of images by a given relative percentage size of the original. If the input size exceeds the size of any image, it's not processed and the name is printed in the end.

> usage: image_util_modules crp_p [-h] -fp FOLDER_PATH -p PERCENTAGE