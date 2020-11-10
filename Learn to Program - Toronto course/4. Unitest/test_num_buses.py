import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_fulfil_one_bus(self):
        """ A number of people expected to fulfil one single bus."""

        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)

    def test_enough_one_bus(self):
        """ A number of people expected to fit on a single bus
        but lower than the maximal capacity."""

        actual = a1.num_buses(30)
        expected = 1
        self.assertEqual(expected, actual)

    def test_greater_one_bus(self):
        """ A number of people expected to fit on more than a single bus."""

        actual = a1.num_buses(75)
        expected = 2
        self.assertEqual(expected, actual)

    def test_zero_bus(self):
        """ No people expected and so no bus."""

        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)
