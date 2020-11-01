import argparse
import jpg_2_png
import png_2_jpg
import image_resizer_util
import image_cropper_util

if __name__ == '__main__':
    command_parser = argparse.ArgumentParser()

    subparsers = command_parser.add_subparsers(help='Select functionality to operate on Images.', dest='functionality')

    j2p_parser = subparsers.add_parser('j2p', help='jpg/jpeg to png conversion')
    j2p_parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    p2j_parser = subparsers.add_parser('p2j', help='png to jpg conversion')
    p2j_parser.add_argument('-ip', '--image_path', type=str, required=True, help='path of the source image')

    res_p_parser = subparsers.add_parser('res_p', help='image resize using realtive percentage')
    res_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='relative size percentage of the output images')

    res_w_parser = subparsers.add_parser('res_w', help='image resize to new width')
    res_w_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_w_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')

    res_h_parser = subparsers.add_parser('res_h', help='image resize to new height')
    res_h_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    res_h_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_px_parser = subparsers.add_parser('crp_px', help='center crop images of required dimensions')
    crp_px_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_px_parser.add_argument('-w', '--width', type=int, required=True, help='reqired width for the output images')
    crp_px_parser.add_argument('-H', '--height', type=int, required=True, help='reqired height for the output images')

    crp_p_parser = subparsers.add_parser('crp_p', help='center crop images of required relative percentage')
    crp_p_parser.add_argument('-fp', '--folder_path', type=str, required=True, help='parent folder of the source images')
    crp_p_parser.add_argument('-p', '--percentage', type=int, required=True, help='reqired relative percentage size for the output images')

    args = command_parser.parse_args()

    if args.functionality == 'j2p':
        jpg_2_png.jpg_2_png_converter(args.image_path)
    elif args.functionality == 'p2j':
        png_2_jpg.png_2_jpg_converter(args.image_path)
    elif args.functionality == 'res_p':
        image_resizer_util.image_resize_percentage(args.folder_path, args.percentage)
    elif args.functionality == 'res_w':
        image_resizer_util.image_resize_width(args.folder_path, args.width)
    elif args.functionality == 'res_h':
        image_resizer_util.image_resize_height(args.folder_path, args.height)
    elif args.functionality == 'crp_px':
        image_cropper_util.crop_center_by_dimension(args.folder_path, (args.width, args.height))
    elif args.functionality == 'crp_p':
        image_cropper_util.crop_center_by_percentange(args.folder_path, args.percentage)