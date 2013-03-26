import datetime as dt
import unittest
from w3 import simulate

class TestSequenceFunctions(unittest.TestCase):


    def test_1(self):
        vol, daily_ret, sharpe, cum_ret = simulate.simulate(dt.datetime(2010, 1, 1), dt.datetime(2010, 12, 31), ['AXP', 'HPQ', 'IBM', 'HNZ'], [0.0, 0.0, 0.0, 1.0])
        self.assertAlmostEqual(vol, 0.00924299255937)
        self.assertAlmostEqual(daily_ret, 0.000756285585593)
        self.assertAlmostEqual(cum_ret, 1.1960583568)
        self.assertAlmostEqual(sharpe, 1.29889334008)


    #@unittest.skip("demonstrating skipping")
    def test_2(self):
        vol, daily_ret, sharpe, cum_ret = simulate.simulate(dt.datetime(2011, 1, 1), dt.datetime(2011, 12, 31), ['AAPL', 'GLD', 'GOOG', 'XOM'], [0.4, 0.4, 0.0, 0.2])
        self.assertAlmostEqual(vol, 0.0101467067654)
        self.assertAlmostEqual(daily_ret, 0.000657261102001)
        self.assertAlmostEqual(cum_ret, 1.16487261965)
        self.assertAlmostEqual(sharpe, 1.02828403099)

if __name__ == '__main__':
    unittest.main()