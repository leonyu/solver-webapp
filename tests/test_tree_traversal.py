import unittest
from utils.algorithm.tree_traversal import TreeTraversal


class TestTreeTraversal(unittest.TestCase):
    def test_bfs(self):
        # type: () -> None
        self.assertListEqual(
            TreeTraversal(range(0, 10)).bfs(),
            [i * 1 for i in range(0, 10)]
        )

    def test_pre_order(self):
        # type: () -> None
        self.assertListEqual(
            TreeTraversal(range(0, 10)).pre_order(),
            [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
        )

    def test_in_order(self):
        # type: () -> None
        self.assertListEqual(
            TreeTraversal(range(0, 10)).in_order(),
            [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
        )

    def test_post_order(self):
        # type: () -> None
        self.assertListEqual(
            TreeTraversal(range(0, 10)).post_order(),
            [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
        )
