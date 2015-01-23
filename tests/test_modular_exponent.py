
from primality.modular_exponent import ModularExponent
import unittest

class TestModularExponent(unittest.TestCase):
    def test_modular_exponent(self):
        self.assertEqual(ModularExponent.exp(5, 117, 19), 1)
        self.assertEqual(ModularExponent.exp(98765, 1234, 123557), 70506)
