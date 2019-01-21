
import unittest
from primality.fermat_primality import FermatPrimality


class TestFermatPrimality(unittest.TestCase):
    def test_fermat_primality_with_primes(self):
        primes = [
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 101,
            1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 3571, 17977, 10619863,
            6620830889, 80630964769, 228204732751, 1171432692373, 1398341745571, 10963707205259,
            15285151248481, 10657331232548839, 790738119649411319, 18987964267331664557
        ]
        for n in primes:
            result, reason = FermatPrimality.is_prime(n)
            self.assertTrue(
                result, "{} should be prime ({})".format(n, reason)
            )

    def test_fermat_primality_with_non_primes(self):
        non_primes = [
            -1, 0, 1, 4, 6, 8, 9, 10, 12, 49, 60,
            100, 561, 3570, 1105, 1729, 2465, 2821, 6601, 8911
        ]
        for n in non_primes:
            result, reason = FermatPrimality.is_prime(n)
            self.assertFalse(
                result, "{} should be non-prime ({})".format(n, reason)
            )
