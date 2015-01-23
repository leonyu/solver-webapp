#!/usr/bin/python

import sys

from primality.fermat_primality import FermatPrimality


def main(argv):
    if len(argv) == 0:
        print 'Please submit a number'
    else:
        test_target = long(argv[0])
        if FermatPrimality.is_prime(test_target):
            print '{num} is a prime number'.format(num=test_target)
        else:
            print '{num} is NOT a prime number'.format(num=test_target)


if __name__ == '__main__':
    main(sys.argv[1:])
