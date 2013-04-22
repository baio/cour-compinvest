__author__ = 'baio'

import unittest

from CompInvest import tech_analizer, data_access
import datetime as dt
from CompInvest.events_gens import bollinger_val

class TestTechAnalisers(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_bollinger_aapl(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        tech_analizer.bollinger(dt_start, dt_end, ["AAPL"], 20, "appl_bollinger_20.png")

    @unittest.skip("demonstrating skipping")
    def test_bollinger_goog(self):
        dt_start = dt.datetime(2010, 1, 1)
        dt_end = dt.datetime(2010, 12, 31)
        tech_analizer.bollinger(dt_start, dt_end, ["GOOG"], 20, "goog_bollinger_20.png")

    def test_bollinger_goog_strategy(self):
        symbols = ["AAPL", "MSFT"]
        keys = ["close"]
        d_data = data_access.load("2010-04-01", "2010-05-22", 16, symbols, keys)
        events, vals = bollinger_val.find_events(d_data)
        print vals["AAPL"].tail()
        print vals["MSFT"].tail()

if __name__ == '__main__':
    unittest.main()