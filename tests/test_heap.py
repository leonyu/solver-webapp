import unittest
import random
from utils.algorithm.heap import MaxHeap


class TestMaxHeap(unittest.TestCase):
    def assertIsHeap(self, array):
        # type: (List[int]) -> bool
        length = len(array)
        if length > 0:
            self.assertEqual(array[0], max(array))
        for i in range(1, length):
            parent = int((i - 1) / 2)
            self.assertLessEqual(array[i], array[parent])

    def test_data(self):
        # type: () -> None
        self.assertListEqual(MaxHeap([]).data, [])
        self.assertListEqual(MaxHeap([1]).data, [1])
        self.assertIsHeap(MaxHeap([7, 4, 5, 3]).data)
        self.assertIsHeap(MaxHeap([7, 4, 5, 3, 1, 0]).data)
        self.assertIsHeap(MaxHeap([7, 4, 5, 3, 1, 0, 2]).data)
        self.assertIsHeap(MaxHeap([7, 4, 5, 3, 1, 0, 2, 6]).data)
        self.assertIsHeap(MaxHeap([7, 4, 5, 3, 1, 0, 2, 6, 8]).data)
        self.assertListEqual(MaxHeap([7, 4, 5, 3, 1, 0, 2, 6, 8]).data, [8, 7, 5, 6, 1, 0, 2, 4, 3])

    def test_no_data(self):
        # type: () -> None
        self.assertIsHeap(MaxHeap([]).data)
        self.assertIsHeap(MaxHeap([1]).data)

    def test_not_comparable(self):
        # type: () -> None
        for i in range(1, 10):
            self.assertIsHeap(MaxHeap([1] * i).data)

    def test_sorted(self):
        # type: () -> None
        for i in range(1, 10):
            data = range(0, i)
            self.assertIsHeap(MaxHeap(data).data)

    def test_reverse(self):
        # type: () -> None
        for i in range(1, 10):
            data = range(0, i)
            self.assertIsHeap(MaxHeap(reversed(data)).data)

    def test_random(self):
        # type: () -> None
        random_sample = [int(x / 2) for x in range(0, 100)]
        random.shuffle(random_sample)
        self.assertIsHeap(MaxHeap(random_sample).data)
