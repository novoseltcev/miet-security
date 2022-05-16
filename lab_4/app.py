from argparse import ArgumentParser

from blowfish import Blowfish

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-K', '--keyfile')
    parser.add_argument('-M', '--message')
    parser.add_argument('-E', '--encrypt', action='store_true')
    parser.add_argument('-D', '--decrypt', action='store_true')
    parser.add_argument('-O', '--output', default='result.txt')

    args = parser.parse_args()
    print(f'{args=}')
    with open(args.keyfile, 'rb') as fd:
        bf = Blowfish(fd.read())

    with open(args.message, 'rb') as fd:
        msg = fd.read()


    match (args.encrypt, args.decrypt):
        case (1, 0):
            result = bf.encode(msg)

        case (0, 1):
            result = bf.decode(msg)

        case _:
            raise RuntimeError()

    with open(args.output, 'wb') as fd:
        fd.write(result)

