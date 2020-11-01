from PIL import Image
import glob
import os
import argparse

def image_resize_percentage(image_folder_path: "Folder Path", resize_percentage: "Percentage(int)" = 100):
    """
    Functio to resize bulk images by user defined percentage,
    keeping aspect ratio constant.
    Takes the folder path and percentage as input.
    """
    if not os.path.isdir(image_folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        img_paths.extend(glob.glob(os.path.join(image_folder_path, ext)))
    ratio = resize_percentage / 100

    dest_folder_path = os.path.join(image_folder_path, 'resized_images_percent_'+str(resize_percentage))
    os.mkdir(dest_folder_path)

    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        out = img.resize([int(ratio * s) for s in img.size])
        out.save(os.path.join(dest_folder_path, tail))

def image_resize_width(image_folder_path: "Folder Path", width: "width(int)"):
    """
    Functio to resize bulk images by user defined width,
    keeping aspect ratio constant.
    Takes the folder path and width as input.
    """
    if not os.path.isdir(image_folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for ext in ('*.jpeg', '*.png', '*.jpg'):
        img_paths.extend(glob.glob(os.path.join(image_folder_path, ext)))

    dest_folder_path = os.path.join(image_folder_path, 'resized_images_width_'+str(width))
    os.mkdir(dest_folder_path)

    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        ratio = img.size[1]/img.size[0]
        new_size = (width, int(ratio*width))
        out = img.resize(new_size)
        out.save(os.path.join(dest_folder_path, tail))

def image_resize_height(image_folder_path: "Folder Path", height: "Height (int)"):
    """
    Functio to resize bulk images by user defined height,
    keeping aspect ratio constant.
    Takes the folder path and height as input.
    """
    if not os.path.isdir(image_folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for extension in ('*.jpeg', '*.png', '*.jpg'):
        img_paths.extend(glob.glob(os.path.join(image_folder_path, extension)))

    dest_folder_path = os.path.join(image_folder_path, 'resized_images_height_'+str(height))
    os.mkdir(dest_folder_path)

    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        ratio = img.size[0]/img.size[1]
        new_size = (int(ratio*height), height)
        out = img.resize(new_size)
        out.save(os.path.join(dest_folder_path, tail))



if __name__ == '__main__':
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    res_p_parser = subparsers.add_parser('res_p', help='image resize using realtive percentage')
    res_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='relative size percentage of the output images')

    res_w_parser = subparsers.add_parser('res_w', help='image resize to new width')
    res_w_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_w_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')

    res_h_parser = subparsers.add_parser('res_h', help='image resize to new height')
    res_h_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_h_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    args = command_parser.parse_args()
    if args.functionality == 'res_p':
        image_resize_percentage(args.folder_path, args.percentage)
    elif args.functionality == 'res_w':
        image_resize_width(args.folder_path, args.width)
    elif args.functionality == 'res_h':
        image_resize_height(args.folder_path, args.height)