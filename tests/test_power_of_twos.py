
import unittest
import util.primality.power_of_twos as power_of_twos


class TestPowerOfTwos(unittest.TestCase):
    def test_split_by_powers_of_two(self):
        # type: () -> None
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(-1), [])
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(0), [])
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(1), [1])
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(2), [2])
        self.assertSequenceEqual(
            power_of_twos.split_by_powers_of_two(3), [1, 2])
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(4), [4])
        self.assertSequenceEqual(
            power_of_twos.split_by_powers_of_two(7), [1, 2, 4])
        self.assertSequenceEqual(power_of_twos.split_by_powers_of_two(8), [8])
        self.assertSequenceEqual(
            power_of_twos.split_by_powers_of_two(117), [1, 4, 16, 32, 64])
        self.assertSequenceEqual(
            power_of_twos.split_by_powers_of_two(1024), [1024])

    def test_is_power_of_two(self):
        # type: () -> None
        self.assertTrue(power_of_twos.is_power_of_two(1))
        self.assertTrue(power_of_twos.is_power_of_two(2))
        self.assertTrue(power_of_twos.is_power_of_two(4))
        self.assertTrue(power_of_twos.is_power_of_two(8))
        self.assertTrue(power_of_twos.is_power_of_two(16))
        self.assertTrue(power_of_twos.is_power_of_two(32))
        self.assertTrue(power_of_twos.is_power_of_two(64))
        self.assertTrue(power_of_twos.is_power_of_two(1024))
        self.assertTrue(power_of_twos.is_power_of_two(2 ** 50))
        self.assertFalse(power_of_twos.is_power_of_two(-1))
        self.assertFalse(power_of_twos.is_power_of_two(0))
        self.assertFalse(power_of_twos.is_power_of_two(10))
        self.assertFalse(power_of_twos.is_power_of_two(9))
        self.assertFalse(power_of_twos.is_power_of_two(2 ** 50 - 1))
