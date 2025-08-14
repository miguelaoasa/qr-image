# qr-image
This Python script generates a QR code that encodes a specified text and embeds a small image at its center. It utilizes the qrcode library for QR code generation and the Pillow library for image manipulation.

## Usage
```
usage: qr_image.py [-h] [-o OUTPUT] image text

Generate a QR code with an embedded image

positional arguments:
  image                Path to the image file to embed in the QR code
  text                 Text to encode in the QR code

options:
  -h, --help           show this help message and exit
  -o, --output OUTPUT  Output filename for the QR code image
```
