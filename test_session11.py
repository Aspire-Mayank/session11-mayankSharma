import pytest
import os
import inspect
import re
from image_utils import jpg_2_png
from image_utils import png_2_jpg
from image_utils import image_resizer_util
from image_utils import image_cropper_util

all_modules = [jpg_2_png, png_2_jpg, image_resizer_util, image_cropper_util]

README_CONTENT_CHECK_FOR = [
                'j2p',
                'p2j',
                'res_w',
                'res_h',
                'res_p',
                'crp_p',
                'crp_px',
            ]


# ----------------------------------------------Default checks Begin--------------------------------------------------#

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    for each_module in all_modules:
        lines = inspect.getsource(each_module)
        spaces = re.findall('\n +.', lines)
        for space in spaces:
            assert len(space) % 4 == 2, f"Your script {each_module} contains misplaced indentations"
            assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 5

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    #readme_words = [word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_function_doc_string():
    '''
    Test case to check whether the functions have docstrings or not.
    '''
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            assert function[1].__doc__

def test_function_annotations():
    '''
    Test case to check whether the functions have annotations or not.
    '''
    for each_module in all_modules:
        functions = inspect.getmembers(each_module, inspect.isfunction)
        for function in functions:
            if function[1].__name__ not in ['namedtuple', 'wraps']:
                assert function[1].__annotations__

# ----------------------------------------------Default checks End--------------------------------------------------#



# ----------------------------------------------Custom checks Begin-------------------------------------------------#

image_folder_path = os.path.abspath('Input_Image_data')

def test_jpg_to_png_converter():
    command = f'python image_utils/jpg_2_png.py -ip {image_folder_path}/1.jpg'
    execute_command =  os.system(command)
    assert not execute_command, "Image JPG/JPEG Conversion failed"

def test_png_to_jpg_converter():
    command = f'python image_utils/png_2_jpg.py -ip {image_folder_path}/1.png'
    execute_command = os.system(command)
    assert not execute_command, "Image PNG Conversion failed"

def test_resize_by_percent():
    command = f'python image_utils/image_resizer_util.py res_p -fp {image_folder_path} -p 50'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Percent failed"

def test_resize_by_width():
    command = f'python image_utils/image_resizer_util.py res_w -fp {image_folder_path} -w 1000'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Width failed"

def test_resize_by_height():
    command = f'python image_utils/image_resizer_util.py res_h -fp {image_folder_path} -H 900'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Height failed"

def test_crop_by_pixel():
    command = f'python image_utils/image_cropper_util.py crp_px -fp {image_folder_path} -H 700 -w 500'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Pixel failed"

def test_crop_by_percent():
    command = f'python image_utils/image_cropper_util.py crp_p -fp {image_folder_path} -p 50'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Percent failed"

def test_zip_convert_to_png():
    command = f'python image_utils_modules j2p -ip {image_folder_path}/5.jpg'
    execute_command =  os.system(command)
    assert not execute_command, "JPG/JPEG Conversion failed"

def test_zip_convert_to_jpg():
    command = f'python image_utils_modules p2j -ip {image_folder_path}/5.png'
    execute_command = os.system(command)
    assert not execute_command, "PNG Conversion failed"

def test_zip_resize_to_80_percent():
    command = f'python image_utils_modules res_p -fp {image_folder_path} -p 80'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Percent failed"

def test_zip_center_crop_to_224_224():
    command = f'python image_utils_modules crp_px -fp {image_folder_path} -H 224 -w 224'
    execute_command = os.system(command)
    assert not execute_command, "Image Cropping by Pixel failed"

def test_zip_resize_to_500_width():
    command = f'python image_utils_modules res_w -fp {image_folder_path} -w 500'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Width failed"

def test_zip_resize_to_500_height():
    command = f'python image_utils_modules res_h -fp {image_folder_path} -H 500'
    execute_command = os.system(command)
    assert not execute_command, "Image Resize by Height failed"

# ----------------------------------------------Custom checks End---------------------------------------------------#