#!/usr/bin/python

import sys

from primality import Primality


def main(argv):
    if len(argv) == 0:
        print 'Please submit a number'
    else:
        test_target = int(argv[0])
        primality = Primality()
        if primality.test(test_target):
            print '{num} is a prime number'.format(num=test_target)
        else:
            print '{num} is not a prime number'.format(num=test_target)


if __name__ == '__main__':
    main(sys.argv[1:])
