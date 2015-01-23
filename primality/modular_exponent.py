
import power_of_twos


class ModularExponent:
    def __init__(self, base, modulus):
        self.base = base
        self.modulus = modulus
        self.cache = {
            0: 1,
            1: base % modulus
        }

    def compute(self, exponent):
        if exponent in self.cache:
            return self.cache[exponent]
        elif power_of_twos.is_power_of_two(exponent):
            h = self.compute(exponent / 2)
            return h * h % self.modulus
        else:
            power_of_twos_split = power_of_twos.split(exponent)
            result = 1
            for exp in power_of_twos_split:
                result *= self.compute(exp)
            return result % self.modulus

    @staticmethod
    def exp(base, exponent, modulus):
        instance = ModularExponent(base, modulus)
        return instance.compute(exponent)
