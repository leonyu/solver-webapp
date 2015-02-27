
from primality.fermat_primality import FermatPrimality
import unittest

class TestFermatPrimality(unittest.TestCase):
    def test_fermat_primality(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 3571, 18987964267331664557]
        non_primes = [-1, 0, 1, 4, 6, 8, 9, 10, 12, 49, 60, 100, 561, 3570, 1105, 1729, 2465, 2821, 6601, 8911]
        for n in primes:
            self.assertTrue(FermatPrimality.is_prime(n))

        for n in non_primes:
            self.assertFalse(FermatPrimality.is_prime(n))
