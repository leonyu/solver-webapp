
import sys

from utils.primality.fermat_primality import FermatPrimality


def main(argv):
    if len(argv) == 0:
        print('Please provide a number as argument')
        return

    test_target = int(argv[0])
    result, reason = FermatPrimality.is_prime(test_target)
    if result:
        print('{num} is a prime number'.format(num=test_target))
    else:
        print('{num} is NOT a prime number'.format(num=test_target))


if __name__ == '__main__':
    main(sys.argv[1:])
