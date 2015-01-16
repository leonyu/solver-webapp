import random
from modular_exponent import ModularExponent

ITERATIONS = 80


class Primality:
    def lhs(self, p, a):
        mod_exp = ModularExponent()
        return mod_exp.compute(a, p - 1, p)

    def fermat(self, p, a):
        lhs = self.lhs(p, a)
        print 'a = {a}, p = {p} lhs = {lhs}'.format(a=a, p=p, lhs=lhs)
        return lhs == 1

    def test(self, p):
        if p < 2:
            return False
        if p == 2:
            return True

        for i in xrange(0, ITERATIONS):
            a = random.randint(2, p - 1)
            if not self.fermat(p, a):
                return False
        return True
