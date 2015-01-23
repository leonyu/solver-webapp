
import primality.power_of_twos as power_of_twos
import unittest

class TestPowerOfTwos(unittest.TestCase):
    def test_split(self):
        self.assertSequenceEqual(power_of_twos.split(2), [2])
        self.assertSequenceEqual(power_of_twos.split(3), [1, 2])
        self.assertSequenceEqual(power_of_twos.split(4), [4])
        self.assertSequenceEqual(power_of_twos.split(7), [1, 2, 4])
        self.assertSequenceEqual(power_of_twos.split(8), [8])
        self.assertSequenceEqual(power_of_twos.split(117), [1, 4, 16, 32, 64])
        self.assertSequenceEqual(power_of_twos.split(1024), [1024])

    def test_is_power_of_two(self):
        self.assertTrue(power_of_twos.is_power_of_two(1))
        self.assertTrue(power_of_twos.is_power_of_two(2))
        self.assertTrue(power_of_twos.is_power_of_two(4))
        self.assertTrue(power_of_twos.is_power_of_two(8))
        self.assertTrue(power_of_twos.is_power_of_two(16))
        self.assertTrue(power_of_twos.is_power_of_two(32))
        self.assertTrue(power_of_twos.is_power_of_two(64))
        self.assertTrue(power_of_twos.is_power_of_two(1024))
        self.assertFalse(power_of_twos.is_power_of_two(-1))
        self.assertFalse(power_of_twos.is_power_of_two(0))
        self.assertFalse(power_of_twos.is_power_of_two(10))
        self.assertFalse(power_of_twos.is_power_of_two(9))
