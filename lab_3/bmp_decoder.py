import sys

from pixel import Pixel


def decrypt(data: bytes):
    result = [pixel.get_hidden() for pixel in Pixel.iterator(data)]
    end_index = result.index(0xFF)
    return bytes(result[:end_index])


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('source')
    parser.add_argument('destination', default='decoded.msg')
    args = parser.parse_args()
    source = args.source
    destination = args.destination
    with open(source, 'rb') as fd:
        image_data = bytes(fd.read())

    image_header, image_body = image_data[:54], image_data[54:]
    result = decrypt(image_body)
    with open(destination, 'wb') as fd:
        fd.write(result)

    print('Successful decrypted message.')
    sys.exit(0)
