import random
from modular_exponent import ModularExponent

ITERATIONS = 80


class FermatPrimality:
    @staticmethod
    def fermat(p, a):
        mod_exp = ModularExponent(base=a, modulus=p)
        lhs =  mod_exp.compute(p - 1)
        return lhs

    @staticmethod
    def is_prime(p):
        if p < 2:
            return False
        if p == 2:
            return True

        for i in xrange(0, ITERATIONS):
            a = random.randint(2, p - 1)
            if FermatPrimality.fermat(p, a) != 1:
                return False
        return True
