import unittest
import random
from utils.quick_sort import QuickSort

class TestQuickSortMethods(unittest.TestCase):
    def test_no_data(self):
        self.assertListEqual(QuickSort([]).sort(), [])
        self.assertListEqual(QuickSort([1]).sort(), [1])

    def test_not_comparable(self):
        for i in range(1, 10):
            self.assertListEqual(QuickSort([1] * i).sort(), [1] * i)

    def test_sorted(self):
        for i in range(1, 10):
            data = range(0, i)
            self.assertListEqual(QuickSort(data).sort(), list(data))

    def test_reverse(self):
        for i in range(1, 10):
            data = range(0, i)
            self.assertListEqual(QuickSort(reversed(data)).sort(), list(data))

    def test_random(self):
        random_sample = list(map(lambda x: int(x / 2), range(0, 100)))
        expected = list(random_sample)
        random.shuffle(random_sample)
        self.assertListEqual(QuickSort(random_sample).sort(), expected)

    def test_select(self):
        r = random.randint(0, 99)
        random_sample = list(map(lambda x: int(x / 2), range(0, 100)))
        expected = list(random_sample)
        random.shuffle(random_sample)
        self.assertEqual(QuickSort(random_sample).select(r), expected[r])
