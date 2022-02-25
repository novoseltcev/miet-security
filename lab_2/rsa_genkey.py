import sys
import random
from math import gcd


def check_prime(value: int) -> bool:
    if value % 2 == 0:
        return value == 2

    for der in range(3, value // 2, 2):
        if value % der == 0:
            return False

    return True


def euler_func(p: int, q: int):
    return (p - 1) * (q - 1)


def get_inter_prime_numbers_less_than(n: int) -> list[int]:
    result = []
    for i in range(2, n):
        if gcd(n, i) == 1:
            result.append(i)
    return result


def calculate_public_key(p: int, q: int) -> int:
    return random.choice(get_inter_prime_numbers_less_than(euler_func(p, q)))


def calculate_private_key(p: int, q: int, e: int) -> int:
    k = 0
    while True:
        result = ((k := k + 1) * euler_func(p, q) + 1) / e
        if result.is_integer():
            return int(result)


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('p')
    parser.add_argument('q')
    args = parser.parse_args()
    p, q = int(args.p), int(args.q)
    if not check_prime(p) or not check_prime(q):
        print(f'Pair: {p=}, {q=} does not contain both primes!', file=sys.stderr)
        sys.exit(-1)
    n = p * q
    e = calculate_public_key(p, q)
    while (d := calculate_private_key(p, q, e)) == e:
        pass

    try:
        with open('public.key', 'w') as fd:
            fd.write(f'{e} {n}')
        with open('private.key', 'w') as fd:
            fd.write(f'{d} {n}')
        print('Successful generated keys.')
    except Exception as e:
        print(e)
        print('\n\nError arisen when generating keys!', file=sys.stderr)
        sys.exit(-2)
