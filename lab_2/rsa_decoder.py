import string
import sys


def decrypt(container: list[int], private_key: int, base: int) -> list[int]:
    return list((digit ** private_key) % base for digit in container)


def digits_to_text(container: list[int]) -> str:
    pool = string.printable
    return ''.join(pool[digit] for digit in container)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('msg_file')
    parser.add_argument('--key_file', default='private.key')
    parser.add_argument('--output', default='decoded.msg')
    args = parser.parse_args()
    msg_file = args.msg_file
    key_file = args.key_file
    output_file = args.output
    try:
        with open(msg_file, 'r') as fd:
            data = list(map(int, fd.read().split()))
        with open(key_file, 'r') as fd:
            private_key, base = map(int, fd.read().split())
        result = digits_to_text(decrypt(data, private_key, base))

        with open(output_file, 'w') as fd:
            fd.write(''.join(map(str, result)))
        print('Successful decrypted message.')
    except Exception as e:
        print('\n\nError arisen when decrypting message!', file=sys.stderr)
        sys.exit(-1)
