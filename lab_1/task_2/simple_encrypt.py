import random
from os import path


keypath = path.join(path.split(__file__)[0], 'key.txt')
chunk = 1024 * 4  # 4КБ - средняя страница в памяти


def generate_key_file():
    with open(keypath, 'wb') as f:
        byte_array = bytearray(random.sample(range(0, 256), 256))
        f.write(byte_array)


def read_key_file() -> dict[int, int]:
    with open(keypath, 'rb') as f:
        return {i: x for i, x in enumerate(bytearray(f.read()))}


def encrypt(source: str, destination: str) -> None:
    encrypt_map = read_key_file()
    with open(source, 'rb') as f_source, open(destination, 'wb') as f_dest:
        while byte_chunk := f_source.read(chunk):
            bytes_str = bytes(encrypt_map[byte] for byte in bytes(byte_chunk))
            f_dest.write(bytes_str)


def decrypt(source: str, destination: str) -> None:
    decrypt_map = {x2: x1 for x1, x2 in read_key_file().items()}
    with open(source, 'rb') as f_source, open(destination, 'wb') as f_dest:
        while byte_chunk := f_source.read(chunk):
            bytes_str = bytes(decrypt_map[byte] for byte in bytes(byte_chunk))
            f_dest.write(bytes_str)


if __name__ == '__main__':
    from argparse import ArgumentParser
    from sys import exit, stderr

    parser = ArgumentParser()
    parser.add_argument('-S', '--source')
    parser.add_argument('-D', '--destination')
    parser.add_argument('--generate', action='store_true')
    parser.add_argument('--encrypt', action='store_true')
    parser.add_argument('--decrypt', action='store_true')
    args = parser.parse_args()

    if (args.generate, args.encrypt, args.decrypt).count(True) != 1:
        print('use only one flag of this: --generate, --encrypt, --decrypt', file=stderr)
        exit()

    if args.generate:
        if args.source or args.destination:
            print('not available use in generation flags: --source, --destination', file=stderr)
            exit()
        generate_key_file()

    elif args.encrypt:
        encrypt(args.source, args.destination)
    else:
        decrypt(args.source, args.destination)

