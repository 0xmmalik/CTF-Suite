###########################
### IMAGE STEGANOGRAPHY ###
###########################
from PIL import Image


def getPixels(filepath):
    return Image.open(filepath).load()


def get_lsb(filepath):
    extracted_bin = []
    with Image.open(filepath) as img:
        width, height = img.size
        byte = []
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    extracted_bin.append(pixel[n] & 1)

    extracted_bin = "".join([str(x) for x in extracted_bin])
    return ''.join(chr(int(extracted_bin[i:i + 8], 2)) for i in range(0, len(extracted_bin), 8))


def encode_lsb(filepath, message, outputfile):
    bin_message = ''.join('{:08b}'.format(ord(c)) for c in message)
    i = 0
    with Image.open(filepath) as img:
        width, height = img.size
        for x in range(0, width):
            for y in range(0, height):
                pixel = list(img.getpixel((x, y)))
                for n in range(0, 3):
                    if i < len(bin_message):
                        pixel[n] = pixel[n] & ~1 | int(bin_message[i])
                        i += 1
                img.putpixel((x, y), tuple(pixel))
        img.save(outputfile, "PNG")
