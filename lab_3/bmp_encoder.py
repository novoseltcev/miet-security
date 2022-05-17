import sys

from pixel import Pixel


def encrypt(b_image: bytes, b_hide: bytes) -> bytes:
    pixels = Pixel.iterator(b_image)
    encrypted_pixels = [next(pixels).hide_byte(byte) for byte in (*b_hide, 0xFF)]
    result = ()
    for pixel in encrypted_pixels:
        result += pixel.tuple()

    return bytes(result) + b_image[len(result):]


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('source', default='encoded.msg')
    parser.add_argument('destination')
    args = parser.parse_args()
    source = args.source
    destination = args.destination

    with open(source, 'rb') as fd:
        hide_data = bytes(fd.read())

    with open(destination, 'rb') as fd:
        image_data = bytes(fd.read())

    image_header, image_body = image_data[:54], image_data[54:]
    with open(destination, 'wb') as fd:
        fd.write(image_header)
        fd.write(encrypt(image_body, hide_data))

    print('Successful encrypted message.')
    sys.exit(0)
