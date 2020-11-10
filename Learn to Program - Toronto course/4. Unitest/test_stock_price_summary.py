import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_only_losses(self):
        """ Stock prices changes containing only decreasing trend
        leading to losses only."""

        actual = a1.stock_price_summary([-0.2])
        expected = (0, -0.2)
        self.assertEqual(expected, actual)

    def test_only_gains(self):
        """ Stock prices changes containing only increasing trend
        leading to gains only."""

        actual = a1.stock_price_summary([0.2])
        expected = (0.2, 0)
        self.assertEqual(expected, actual)

    def test_both_trends(self):
        """ Stock prices changes containing increasing and decreasing
        trends leading to gains and losses."""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

    def test_empty_trends(self):
        """ No stock prices changes leading to zero gains and losses."""

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_null_trends(self):
        """ No stock prices changes leading to zero gains and losses."""

        actual = a1.stock_price_summary([0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
