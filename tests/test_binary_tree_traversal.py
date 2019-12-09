import unittest
from utils.algorithm.binary_tree_traversal import BinaryTreeTraversal


class TestBinaryTreeTraversal(unittest.TestCase):
    def test_to_bft(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal(range(0, 10)).to_bft(),
            list(range(0, 10))
        )

    def test_from_bft(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal.from_bft(list(range(0, 10))),
            list(range(0, 10))
        )

    def test_to_pre_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal(range(0, 10)).to_pre_order(),
            [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
        )

    def test_from_pre_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal.from_pre_order([0, 1, 3, 7, 8, 4, 9, 2, 5, 6]),
            list(range(0, 10))
        )

    def test_to_in_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal(range(0, 10)).to_in_order(),
            [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
        )

    def test_from_in_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal.from_in_order([7, 3, 8, 1, 9, 4, 0, 5, 2, 6]),
            list(range(0, 10))
        )

    def test_to_post_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal(range(0, 10)).to_post_order(),
            [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
        )

    def test_from_post_order(self):
        # type: () -> None
        self.assertListEqual(
            BinaryTreeTraversal.from_post_order([7, 8, 3, 9, 4, 1, 5, 6, 2, 0]),
            list(range(0, 10))
        )
