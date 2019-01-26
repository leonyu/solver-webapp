
from .power_of_twos import split_by_powers_of_two, is_power_of_two


class ModularExponent:
    def __init__(self, base, modulus):
        # type: (int, int) -> None
        self.base = base
        self.modulus = modulus
        self.cache = {
            0: 1,
            1: base % modulus
        }

    def compute(self, exponent):
        # type: (int) -> int
        if exponent in self.cache:
            return self.cache[exponent]
        if is_power_of_two(exponent):
            h = self.compute(exponent // 2)
            return h * h % self.modulus

        power_of_twos_split = split_by_powers_of_two(exponent)
        result = 1
        for exp in power_of_twos_split:
            result *= self.compute(exp)
        return result % self.modulus

    @staticmethod
    def exp(base, exponent, modulus):
        # type: (int, int, int) -> int
        instance = ModularExponent(base, modulus)
        return instance.compute(exponent)
