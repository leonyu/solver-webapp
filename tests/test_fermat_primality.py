
from primality.fermat_primality import FermatPrimality
import unittest

class TestFermatPrimality(unittest.TestCase):
    def test_fermat_primality(self):
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 3571, 18987964267331664557]
        non_primes = [-1, 0, 1, 4, 6, 8, 9, 10, 12, 49, 60, 100, 3570]
        for n in primes:
            self.assertTrue(FermatPrimality.is_prime(n))

        for n in non_primes:
            self.assertFalse(FermatPrimality.is_prime(n))
