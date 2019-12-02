
import unittest
from utils.algorithm.coloring import Coloring


class TestColoring(unittest.TestCase):
    def test_one(self):
        # type: () -> None
        self.assertDictEqual(Coloring([[1, 1, 1, 2, 2, 2, 3, 3, 3]]).color(), {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (0, 3): 1,
            (0, 4): 1,
            (0, 5): 1,
            (0, 6): 2,
            (0, 7): 2,
            (0, 8): 2,
        })
    def test_two(self):
        # type: () -> None
        self.assertDictEqual(Coloring([
            [1, 1, 1, 2, 2, 2],
            [2, 2, 2, 1, 1, 1]
        ]).color(), {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (0, 3): 1,
            (0, 4): 1,
            (0, 5): 1,
            (1, 0): 3,
            (1, 1): 3,
            (1, 2): 3,
            (1, 3): 2,
            (1, 4): 2,
            (1, 5): 2,
        })

    def test_three(self):
        # type: () -> None
        self.assertDictEqual(Coloring([
            [1, 1, 1, 2, 2, 2, 1, 1, 1],
            [2, 2, 2, 1, 1, 1, 2, 2, 2]
        ]).color(), {
            (0, 0): 0,
            (0, 1): 0,
            (0, 2): 0,
            (0, 3): 1,
            (0, 4): 1,
            (0, 5): 1,
            (0, 6): 2,
            (0, 7): 2,
            (0, 8): 2,
            (1, 0): 5,
            (1, 1): 5,
            (1, 2): 5,
            (1, 3): 4,
            (1, 4): 4,
            (1, 5): 4,
            (1, 6): 3,
            (1, 7): 3,
            (1, 8): 3,
        })
