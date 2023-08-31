#!/usr/bin/python

import argparse
from PIL import Image

# Create argument Handler
parser = argparse.ArgumentParser("SIMPLE EXAMPLE")

# Define each argument
parser.add_argument("source_path", help="The file-path to the source image you want to resize", type=str)
parser.add_argument("target_size_x", help="The final dimension of the images x axis", type=int)
parser.add_argument("target_size_y", help="The final dimension of the images y axis", type=int)
parser.add_argument("output_name", help="The resize image's new filename", type=str)

# Capture arguments
args = parser.parse_args()

# Open the image
image = Image.open(args.source_path)

# Resize the image
new_image = image.resize((args.target_size_x, args.target_size_y))

# Save it in the calling directory
new_image.save(args.output_name)