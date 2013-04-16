__author__ = 'baio'

__author__ = 'baio'


import unittest

from w6.events_gens.equity_9_dollars_actual_close import  find_events as evt_9_dollars_actual_close
from w6.strategy_gens.event_date_buy_100_sell_5_days_later import generate_strategy as strat
from w6.market_simulator import build_market
from w6 import strategy_maker
from w6 import market_analyser
import datetime as dt

import QSTK.qstkstudy.EventProfiler as ep

import QSTK.qstkutil.DataAccess as da

import numpy as np

class TestSequenceFunctions(unittest.TestCase):

    def test_equity_sp_9_dollars_actual_close(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        dataobj = da.DataAccess('Yahoo')
        ls_symbols = dataobj.get_symbols_from_list('sp5002012')
        df_events, d_data = strategy_maker.find_events(dt_start, dt_end, 'SPY', ls_symbols, evt_9_dollars_actual_close)
        strategy_maker.write_strategy("../data/orders_9_dollar_events.csv", df_events, strat)
        build_market(50000, "../data/orders_9_dollar_events.csv", "../data/values_9_dollar_events.csv")
        market_analyser.analise_market("../data/values_9_dollar_events.csv", "SPY", "../data/9_dollar_events.png")


if __name__ == '__main__':
    unittest.main()