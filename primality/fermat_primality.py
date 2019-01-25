import random
from typing import Tuple
from .modular_exponent import ModularExponent

ITERATIONS = 100


class FermatPrimality:
    def __init__(self):
        # type: () -> None
        pass

    @staticmethod
    def fermat(p, a):
        # type: (int, int) -> int
        mod_exp = ModularExponent(base=a, modulus=p)
        lhs = mod_exp.compute(p - 1)
        return lhs

    @staticmethod
    def is_prime(p):
        # type: (int) -> Tuple[bool, str]
        if p < 2:
            return (False, 'Less than 2')
        if p == 2:
            return (True, 'Equals to 2')

        for _ in range(0, ITERATIONS):
            a = random.randint(2, p - 1)
            fermat = FermatPrimality.fermat(p, a)
            # print a, fermat
            if fermat != 1:
                return (False, 'fermat {}'.format(a))
        return (True, 'OK after {} iterations of fermat test'.format(ITERATIONS))
