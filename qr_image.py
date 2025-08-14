#!/usr/bin/env python3

from datetime import datetime
from mimetypes import guess_type
from PIL import Image, ImageDraw

import argparse
import os
import qrcode
import sys

def generate_qr_image(image, text, output_filename):
    mime = guess_type(image)[0]
    if mime not in ["image/jpeg", "image/png"]:
        print(f"[!!] Invalid image MIME type.")
        sys.exit(1)

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    inserted_image = Image.open(image)
    inserted_image = inserted_image.resize((60, 60))

    draw = ImageDraw.Draw(qr_image)
    center_x = qr_image.size[0] // 2
    center_y = qr_image.size[1] // 2
    square_size = 70
    draw.rectangle(
        (center_x - square_size // 2, center_y - square_size // 2,
         center_x + square_size // 2, center_y + square_size // 2),
        fill="white"
    )

    qr_image.paste(inserted_image, ((qr_image.size[0] - inserted_image.size[0]) // 2, (qr_image.size[1] - inserted_image.size[1]) // 2), inserted_image)

    qr_image.save(output_filename)

def check_file(file):
    if not os.path.isfile(file):
        print(f"[!] {file} not such file.")
        sys.exit(1)

    if not os.access(file, os.R_OK):
        print(f"[!] {file} access denied.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate a QR code with an embedded image")
    parser.add_argument("image", help="Path to the image file to embed in the QR code")
    parser.add_argument("text", help="Text to encode in the QR code")
    parser.add_argument("-o", "--output", help="Output filename for the QR code image", default=None)
    args = parser.parse_args()

    # Check if the output filename is provided; if not, create a default one
    if args.output is None:
        current_time = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        output_filename = f"{current_time}-qr_image.png"
    else:
        output_filename = args.output

    check_file(args.image)

    generate_qr_image(args.image, args.text, output_filename)


if __name__ == "__main__":
    main()
