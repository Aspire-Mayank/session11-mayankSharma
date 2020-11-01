import os
import glob
from PIL import Image
import argparse

def crop_center_by_dimension(image_folder_path: "Image Folder Path", dimension: "dimension of Image (W, H)"):
	"""
	Defined function to crop bulk images by square/rectangle by given input dimension.
	Input would be Image folders path and image dimension to crop.
	"""
	if not os.path.isdir(image_folder_path):
		raise ValueError('No such folder exists.')
	img_paths = []
	for extension in ('*.jpeg','*.png','*.jpg','*.JPEG','*.PNG','*.JPG'):
		img_paths.extend(glob.glob(os.path.join(image_folder_path, extension)))

	dest_folder_path = os.path.join(image_folder_path, 'crop_image_size_'+str(dimension))
	os.mkdir(dest_folder_path)

	pending_images = []
	for img_path in img_paths:
		head, tail = os.path.split(img_path)
		img = Image.open(img_path)
		img_dim = img.size
		if img_dim[0]>=dimension[0] and img_dim[1]>=dimension[1]:
			out = img.crop(((img_dim[0] - dimension[0]) // 2,
				(img_dim[1] - dimension[1]) // 2,
				(img_dim[0] + dimension[0]) // 2,
				(img_dim[1] + dimension[1]) // 2))
			out.save(os.path.join(dest_folder_path, tail))
		else:
			del img
			pending_images.append(tail)
	if len(pending_images) > 0:
		print("This Images unable to proccessed:")
		print("\n".join(pending_images))


def crop_center_by_percentange(image_folder_path: "Folder Path", crop_percentage: "Percentage(int)"):
    """
    Function center square/rectangle crops bulk images by user-determined percentage.
    Takes the folder path and percentage as input.
    The images that are not cropped due to exceeding size are printed.
    """
    if not os.path.isdir(image_folder_path):
        raise ValueError('No such folder exists.')
    img_paths = []
    for ext in ('*.jpeg', '*.png', '*.jpg', '*.JPEG', '*.PNG', '*.JPG'):
        img_paths.extend(glob.glob(os.path.join(image_folder_path, ext)))

    dest_folder_path = os.path.join(image_folder_path, 'cropeed_images_percentage_'+str(crop_percentage))
    os.mkdir(dest_folder_path)

    skipped_images = []
    for img_path in img_paths:
        head, tail = os.path.split(img_path)
        img = Image.open(img_path)
        img_size = img.size
        ratio = crop_percentage / 100
        size = (int(ratio*img_size[0]), int(ratio*img_size[1]))
        if img_size[0]>=size[0] and img_size[1]>=size[1]:
            out = img.crop(((img_size[0] - size[0]) // 2, 
                (img_size[1] - size[1]) // 2,
                (img_size[0] + size[0]) // 2,
                (img_size[1] + size[1]) // 2))
            out.save(os.path.join(dest_folder_path, tail))
        else:
            del img
            skipped_images.append(tail)

    if len(skipped_images) > 0:
        print("The following images couldn't be processed:")
        print("\n".join(skipped_images))



if __name__ == '__main__':
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Choose a functionality.', dest='functionality')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')

    args = command_parser.parse_args()
    if args.functionality == 'crp_px':
        crop_center_by_dimension(args.folder_path, (args.width, args.height))
    elif args.functionality == 'crp_p':
        crop_center_by_percentange(args.folder_path, args.percentage)