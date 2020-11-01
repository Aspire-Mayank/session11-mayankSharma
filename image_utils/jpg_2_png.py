from PIL import Image
import os
import argparse

def jpg_2_png_converter(image_folder_path: "Image Path"):
	"""
	Convert jpg/jpeg image to png.
	"""
	if not os.path.isfile(image_folder_path):
		raise ValueError('Image file does not exists.')
	elif image_folder_path.split('.')[-1] not in ['jpg', 'jpeg']:
		raise ValueError('Image is not of jpg/jpeg extension.')

	new_path = image_folder_path.split('.'+image_folder_path.split('.')[-1])[0]+'.png'
	img = Image.open(image_folder_path).convert('RGB')
	img.save(new_path,'png')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Extension jpg/jpeg to png conversion')
	parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

	args = parser.parse_args()
	jpg_2_png_converter(args.image_path)