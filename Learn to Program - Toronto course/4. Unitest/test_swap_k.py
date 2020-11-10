import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_one_item_swapped(self):
        """ Swapping 1/3 of an even array."""

        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 1)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(expected, actual)

    def test_half_item_swapped(self):
        """ Swapping half of an even array."""

        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(expected, actual)

    def test_zero_item_swapped(self):
        """ None swapping."""

        actual = [1, 2, 3, 4, 5, 6]
        a1.swap_k(actual, 0)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, actual)

    def test_one_item_list(self):
        """ None swapping on one item list."""

        actual = [1]
        a1.swap_k(actual, 0)
        expected = [1]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
