import string
import sys


def text_to_digits(text: str) -> list[int, ...]:
    pool = string.printable
    return list(pool.index(char) for char in text)


def encrypt(container: list[int], public_key: int, base: int) -> list[int, ...]:
    return list((digit ** public_key) % base for digit in container)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('msg_file')
    parser.add_argument('--key_file', default='public.key')
    parser.add_argument('--output', default='encoded.msg')
    args = parser.parse_args()
    msg_file = args.msg_file
    key_file = args.key_file
    output_file = args.output
    try:
        with open(msg_file, 'r') as fd:
            data = fd.read()
        with open(key_file, 'r') as fd:
            public_key, base = map(int, fd.read().split())
        result = encrypt(text_to_digits(data), public_key, base)
        with open(output_file, 'w') as fd:
            fd.write(' '.join(map(str, result)))
        print('Successful encrypted message.')
    except Exception as e:
        print(e)
        print('\n\nError arisen when encrypting message!', file=sys.stderr)
        sys.exit(-1)
