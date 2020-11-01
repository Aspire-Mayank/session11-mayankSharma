from PIL import Image
import os
import argparse

def png_2_jpg_converter(image_folder_path: "Image Path"):
	"""
	"""
	if not os.path.isfile(image_folder_path):
		raise ValueError('Image file does not exists.')
	elif image_folder_path.split('.')[-1] != 'png':
		raise ValueError('Image is not a png file..')

	new_path = image_folder_path.split("."+image_folder_path.split('.')[-1])[0]+'.jpg'
	img = Image.open(image_folder_path).convert('RGB')
	img.save(new_path, 'jpeg')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Extension png to jpg conversion')
	parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source')

	args = parser.parse_args()
	png_2_jpg_converter(args.image_path)