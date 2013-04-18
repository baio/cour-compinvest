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
        symbols = ["AAPL", "GOOG"]
        keys = ["close"]
        d_data = data_access.load("2009-01-01", "2010-12-31", 16, symbols, keys)
        events = bollinger_val.find_events(d_data)
        print events[events["AAPL"] == 1].head()

if __name__ == '__main__':
    unittest.main()