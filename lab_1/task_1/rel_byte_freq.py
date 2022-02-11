from matplotlib import pyplot as plt


def get_bytes_map(path: str) -> dict[int, int]:
    result = {byte: 0 for byte in range(256)}
    with open(path, 'rb') as stream:
        byte_list = bytes(stream.read())
        for byte in byte_list:
            result[byte] += 1
        return result


def draw_distribution(distribution: dict[int, int]) -> None:
    plt.plot(distribution.keys(), distribution.values())
    plt.xlim(0, 255)
    plt.ylim(0, max(distribution.values()))
    plt.ylabel('ΔF')
    plt.xlabel('byte')
    plt.show()


if __name__ == '__main__':
    from argparse import ArgumentParser

    """
    Use example:
        > python rel_byte_freq.py --path ../task.pdf
    """

    parser = ArgumentParser()
    parser.add_argument('--path', required=True)
    args = parser.parse_args()
    bytes_map = get_bytes_map(args.path)
    bytes_len = sum(bytes_map.values())
    bytes_map = {byte: byte_freq / bytes_len for byte, byte_freq in bytes_map.items()}
    draw_distribution(bytes_map)
