# psdtojpg

*Version 0.1.0*

Convert one or more PSD files to JPG format. Thumbnail and optimize them, or don't.

I keep many of the assets I use for web development in PSD format. This lets me perform non-destructive edits and crops in Photoshop and come back to edit the originals later. I built `psdtojpg` to make it easier to generate, downsize, and optimize JPGs from my asset PSDs.

# Installation

This is a Python 3 script, so use `pip3` to install:

```
pip3 install psdtojpg
```

After this, run `psdtojpg --help` from your terminal to verify it's installed properly.

# Usage

## Basic Conversion

```
psdtojpg my_file.psd
```

* `my_file.psd ➔ Converted/Original/my_file.jpg` (original size, default quality: 80)

## Downsizing Images

```
psdtojpg -w 640 -t 480 my_file.psd
```

* `my_file.psd ➔ Converted/Original/my_file.jpg` (original size)
* `my_file.psd ➔ Converted/Resized/my_file.jpg` (max size: 640x480 px)

---

```
psdtojpg -w 640 -t 480 -n my_file.psd
```

* `my_file.psd ➔ Converted/Resized/my_file.jpg` (max size: 640x480 px)

## Quality and Optimization

```
psdtojpg -q 60 my_file.psd
```

* `my_file.psd ➔ Converted/Original/my_file.jpg` (original size, quality: 60)

---

```
psdtojpg -o my_file.psd
```

* `my_file.psd ➔ Converted/Original/my_file.jpg` (original size, optimized with [ImageOptim](https://imageoptim.com/))

## Custom Output Folders

```
psdtojpg -w 800 -t 600 -g orig -r thumb/sm my_file.psd
```

* `my_file.psd ➔ orig/my_file.jpg` (original size)
* `my_file.psd ➔ thumb/sm/my_file.jpg` (max size: 800x600 px)

# Requirements

Python 3. (Tested with Python 3.4.1 on Mac OS X 10.9.3.)

Relies on the following packages:

* [Pillow](http://python-pillow.github.io/), the Python 3 PIL fork
* [psd-tools](https://github.com/kmike/psd-tools)

Optional dependencies:

* For image optimization on OS X: [ImageOptim CLI](https://github.com/JamieMason/ImageOptim-CLI)—install with `npm install -g imageoptim-cli`

# Help

Command: `psdtojpg --help`

```
usage: psdtojpg [-h] [-w MAX_WIDTH] [-t MAX_HEIGHT] [-q QUALITY] [-o] [-n]
                [-g ORIGINAL_FOLDER] [-r RESIZED_FOLDER]
                psd_file [psd_file ...]

Convert PSD files to JPG images.

positional arguments:
  psd_file              One or more PSD files to be converted

optional arguments:
  -h, --help            show this help message and exit
  -w MAX_WIDTH, --max-width MAX_WIDTH
                        The maximum width of resized output files in pixels.
  -t MAX_HEIGHT, --max-height MAX_HEIGHT
                        The maximum height of resized output files in pixels.
  -q QUALITY, --quality QUALITY
                        The output quality of JPG files. Default is 80.
  -o, --optimize        Optimize output files with ImageOptim after
                        conversion. Requires the imageOptim CLI to be
                        installed.
  -n, --no-originals    Do not output original-size JPGs.
  -g ORIGINAL_FOLDER, --original-folder ORIGINAL_FOLDER
                        The name of the output folder for original-size JPGs.
                        Can be nested.
  -r RESIZED_FOLDER, --resized-folder RESIZED_FOLDER
                        The name of the output folder for resized JPGs. Can be
                        nested.
```

# Contributions

Bug reports, fixes, or features? Feel free to open an issue or pull request any time. You can also tweet me at [mplewis](http://twitter.com/mplewis) or email me at [matt@mplewis.com](mailto:matt@mplewis.com).

# License

Copyright (c) 2014 Matthew Lewis. Licensed under [the MIT License](http://opensource.org/licenses/MIT).