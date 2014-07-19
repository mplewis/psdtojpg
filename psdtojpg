#!/usr/bin/env python3

import argparse
import os
import subprocess

import PIL
from psd_tools import PSDImage


DEFAULT_ORIGINAL_FOLDER = 'Converted/Original'
DEFAULT_RESIZED_FOLDER = 'Converted/Resized'
JPG_EXTENSION = '.jpg'
OUTPUT_QUALITY = 80
IMAGEOPTIM_CMD = 'imageOptim -d %s'
CONVERT_TO_CHAR = '→'


def check_negative(value):
    """Validates integers greater than or equal to 0."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            '"%s" must be an integer' % value)
    if ivalue < 0:
        raise argparse.ArgumentTypeError(
            '"%s" must not be a negative value' % value)
    return ivalue


def check_0_to_100(value):
    """Validates integers from 0 to 100, inclusive."""
    try:
        ivalue = int(value)
    except ValueError:
        raise argparse.ArgumentTypeError(
            '"%s" must be an integer' % value)
    if ivalue < 0 or ivalue > 100:
        raise argparse.ArgumentTypeError(
            '"%s" must be from 0 to 100, inclusive' % value)
    return ivalue


def parse_args():
    """Parses the command line arguments and returns an args object."""
    parser = argparse.ArgumentParser(
        description='Convert PSD files to JPG images.')

    parser.add_argument('files', metavar='psd_file', type=str, nargs='+',
                        help='One or more PSD files to be converted')

    parser.add_argument('-w', '--max-width', type=check_negative,
                        help='The maximum width of resized output files '
                             'in pixels.')

    parser.add_argument('-t', '--max-height', type=check_negative,
                        help='The maximum height of resized output files '
                             'in pixels.')

    parser.add_argument('-q', '--quality', type=check_0_to_100,
                        default=OUTPUT_QUALITY,
                        help='The output quality of JPG files. Default is 80.')

    parser.add_argument('-o', '--optimize', action='store_true',
                        help='Optimize output files with ImageOptim after '
                             'conversion. Requires the imageOptim CLI to be '
                             'installed.')

    parser.add_argument('-n', '--no-originals', action='store_true',
                        help='Do not output original-size JPGs.')

    parser.add_argument('-g', '--original-folder', type=str,
                        default=DEFAULT_ORIGINAL_FOLDER,
                        help='The name of the output folder for '
                             'original-size JPGs. Can be nested.')

    parser.add_argument('-r', '--resized-folder', type=str,
                        default=DEFAULT_RESIZED_FOLDER,
                        help='The name of the output folder for '
                             'resized JPGs. Can be nested.')

    return parser.parse_args()


def mkdir(path):
    """Create a directory if it does not already exist."""
    os.makedirs(path, exist_ok=True)


def downsize_by_height(*, width, height, new_height):
    """
    Given the original width and height of an image and a new target height,
    return the new width and height. If the image would be larger than the
    original, return the original size.
    """
    if (height <= new_height):
        return (width, height)
    ratio = new_height / height
    new_width = int(width * ratio)
    return (new_width, new_height)


def downsize_by_width(*, width, height, new_width):
    """
    Given the original width and height of an image and a new target width,
    return the new width and height. If the image would be larger than the
    original, return the original size.
    """
    if (width <= new_width):
        return (width, height)
    ratio = new_width / width
    new_height = int(height * ratio)
    return (new_width, new_height)


def convert_psd_to_jpg(psd_path, jpg_path, *,
                       quality, max_width=None, max_height=None):
    """
    Convert a PSD at a given path to a JPG at a given path.

    Optional arguments for setting JPG quality from 0 to 100, max width in px,
    and max height in px.
    """
    print('%s %s %s' % (psd_path, CONVERT_TO_CHAR, jpg_path))

    img = PSDImage.load(psd_path).as_PIL()
    width, height = img.size

    if max_width or max_height:
        if max_width and max_height:
            new_size_a = downsize_by_height(width=width, height=height,
                                            new_height=max_height)
            new_size_b = downsize_by_width(width=width, height=height,
                                           new_width=max_width)
            if new_size_a[0] * new_size_a[1] <= new_size_b[0] * new_size_b[1]:
                new_size = new_size_a
            else:
                new_size = new_size_b
        elif max_height:
            new_size = downsize_by_height(width=width, height=height,
                                          new_height=max_height)
        elif max_width:
            new_size = downsize_by_width(width=width, height=height,
                                         new_width=max_width)
        (img.resize(new_size, resample=PIL.Image.ANTIALIAS)
            .save(jpg_path, quality=quality))

    else:
        img.save(jpg_path, quality=quality)


def main():
    """Parse arguments and process files passed to the script."""
    args = parse_args()

    output_originals = not args.no_originals
    output_resized = args.max_width or args.max_height

    if output_originals:
        mkdir(args.original_folder)
    if output_resized:
        mkdir(args.resized_folder)

    for input_path in args.files:
        old_filename = os.path.basename(input_path)
        new_filename = os.path.splitext(old_filename)[0] + JPG_EXTENSION

        if output_originals:
            output_path = os.path.join(args.original_folder, new_filename)
            convert_psd_to_jpg(input_path, output_path, quality=args.quality)

        if output_resized:
            output_path = os.path.join(args.resized_folder, new_filename)
            convert_psd_to_jpg(input_path, output_path,
                               quality=args.quality,
                               max_width=args.max_width,
                               max_height=args.max_height)

    if args.optimize:
        if output_originals:
            subprocess.call(IMAGEOPTIM_CMD % args.original_folder, shell=True)
        if output_resized:
            subprocess.call(IMAGEOPTIM_CMD % args.resized_folder, shell=True)

if __name__ == '__main__':
    main()
