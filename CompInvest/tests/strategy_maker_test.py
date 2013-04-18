__author__ = 'baio'


import unittest
from CompInvest.events_gens.equity_3_down_market_2_up import find_events as evt
from CompInvest.events_gens.equity_5_dollars_actual_close import  find_events as evt_5_dollars_actual_close
from CompInvest.strategy_gens.event_date_buy_100_sell_5_days_later import generate_strategy as strat
from CompInvest.market_simulator import build_market
from CompInvest import strategy_maker
from CompInvest import market_analyzer
import datetime as dt

import QSTK.qstkstudy.EventProfiler as ep

import QSTK.qstkutil.DataAccess as da

import numpy as np

class TestSequenceFunctions(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_analise_market_sim(self):
        market_analyzer.analise_market("../data/values_5_dollar_events.csv", "SPY", "../data/5_dollar_events.png")

    @unittest.skip("demonstrating skipping")
    def test_build_market_sim(self):
        build_market(50000, "../data/orders_5_dollar_events.csv", "../data/values_5_dollar_events.csv")

    def test_write_strategy_equity_3_down_market_2_up_buy_100_aapl(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        df_events, d_data = strategy_maker.find_events(dt_start, dt_end, 'SPY', ['AAPL'], evt)
        strategy_maker.write_strategy("orders1.csv", df_events, strat)

    @unittest.skip("demonstrating skipping")
    def test_equity_sp_5_dollars_actual_close(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        dataobj = da.DataAccess('Yahoo')
        ls_symbols = dataobj.get_symbols_from_list('sp5002012')
        df_events, d_data = strategy_maker.find_events(dt_start, dt_end, 'SPY', ls_symbols, evt_5_dollars_actual_close)
        strategy_maker.write_strategy("../data/orders_5_dollar_events.csv", df_events, strat)

    @unittest.skip("demonstrating skipping")
    def test_gen_strategy_equity_3_down_market_2_up_aapl(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        df_events, d_data = strategy_maker.find_events(dt_start, dt_end, 'SPY', ['AAPL'], evt)
        strategy_maker.generate_strategy(df_events, strat)

    @unittest.skip("demonstrating skipping")
    def test_equity_3_down_market_2_up_aapl(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        df_events, d_data = strategy_maker.find_events(dt_start, dt_end, 'SPY', ['AAPL'], evt)
        ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                         s_filename='test_equity_3_down_market_2_up_aapl_fast.pdf', b_market_neutral=True, b_errorbars=True,
                         s_market_sym='SPY')


    @unittest.skip("demonstrating skipping")
    def test_equity_3_down_market_2_up(self):
        dt_start = dt.datetime(2008, 1, 1)
        dt_end = dt.datetime(2009, 12, 31)
        dataobj = da.DataAccess('Yahoo')
        ls_symbols = dataobj.get_symbols_from_list('sp5002012')
        strategy_maker.find_events(dt_start, dt_end, 'SPY', ls_symbols, evt)
        ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                         s_filename='test_equity_3_down_market_2_up.pdf', b_market_neutral=True, b_errorbars=True,
                         s_market_sym='SPY')

if __name__ == '__main__':
    unittest.main()