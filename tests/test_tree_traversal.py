import unittest
from typing import List, Optional
from utils.algorithm.tree_traversal import from_bft, to_bft
from utils.algorithm.tree_traversal import from_pre_order, to_pre_order
from utils.algorithm.tree_traversal import from_post_order, to_post_order


class TestTreeTraversal(unittest.TestCase):
    def test_bft(self):
        # type: () -> None
        TEST_CASES = [
            [None],
            [1, None, None],
            [0, 1, 2, 3, 4, None, None, None, None, None, None],
            [1, 2, 4, None, 3, None, None, None, None],
        ]  # type: List[List[Optional[int]]]
        for case in TEST_CASES:
            self.assertListEqual(to_bft(from_bft(case)), case)

    def test_pre_order(self):
        # type: () -> None
        TEST_CASES = [
            [None],
            [1, None, None],
            [1, 2, None, 3, None, None, 4, None, None],
        ]  # type: List[List[Optional[int]]]
        for case in TEST_CASES:
            self.assertListEqual(to_pre_order(from_pre_order(case)), case)

    def test_post_order(self):
        # type: () -> None
        TEST_CASES = [
            [None],
            [None, None, 1],
            [None, None, None, 3, 2, None, None, 4, 1],
        ]  # type: List[List[Optional[int]]]
        for case in TEST_CASES:
            self.assertListEqual(to_post_order(from_post_order(case)), case)
