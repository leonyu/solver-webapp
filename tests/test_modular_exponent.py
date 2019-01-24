
import unittest
from primality.modular_exponent import ModularExponent


class TestModularExponent(unittest.TestCase):
    def test_modular_exponent(self) -> None:
        self.assertEqual(ModularExponent.exp(5, 117, 19), 1)
        self.assertEqual(ModularExponent.exp(98765, 1234, 123557), 70506)
