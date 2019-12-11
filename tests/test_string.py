import unittest
from utils.algorithm.string import create_lps, find_string


class TestString(unittest.TestCase):
    def test_lps(self):
        # type: () -> None
        self.assertListEqual(create_lps('AAAA'), [0, 1, 2, 3])
        self.assertListEqual(create_lps('ABCDE'), [0, 0, 0, 0, 0])
        self.assertListEqual(
            create_lps('AABAACAABAA'),
            [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
        )
        self.assertListEqual(
            create_lps('AAACAAAAAC'),
            [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
        )
        self.assertListEqual(create_lps('AAABAAA'), [0, 1, 2, 0, 1, 2, 3])
        self.assertListEqual(create_lps('ABCDABC'), [0, 0, 0, 0, 1, 2, 3])
        self.assertListEqual(create_lps('BAAAAAA'), [0, 0, 0, 0, 0, 0, 0])
        self.assertListEqual(create_lps('ABABABA'), [0, 0, 1, 2, 3, 4, 5])

    def test_find_string(self):
        # type: () -> None
        self.assertEqual(find_string('AAA', 'A'), 0)
        self.assertEqual(find_string('BAA', 'A'), 1)
        self.assertEqual(find_string('BBA', 'A'), 2)
        self.assertEqual(find_string('AAAA', 'AA'), 0)
        self.assertEqual(find_string('BAAA', 'AA'), 1)
        self.assertEqual(find_string('BBAA', 'AA'), 2)
        self.assertEqual(find_string('hello world', 'world'), 6)
        self.assertEqual(find_string('hello world!!!', 'world'), 6)
