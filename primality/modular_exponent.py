
import bitwise_utility


class ModularExponent:
    def compute(base, exponent, modulus):
        exp_mods = [1, base % modulus]
        while (2 ** (len(exp_mods) - 1)) < base:
            modded = exp_mods[-1]
            exp_mods.append(modded * modded % modulus)
        return exp_mods

    def __init__(self, base, modulus):
        self.base = base
        self.modulus = modulus

    def power(self, exponent):
      