__author__ = 'baio'

import unittest

from CompInvest.events_gens.bollinger_minus_2_spy_1 import  find_events
from CompInvest import data_access
import QSTK.qstkutil.DataAccess as da
from CompInvest.strategy_maker import  write_strategy
from CompInvest.strategy_gens.event_date_buy_100_sell_5_days_later import generate_strategy as strategy
from  CompInvest.market_simulator import build_market
from CompInvest.market_analyzer import analise_market

class TestW8Functions(unittest.TestCase):

    def test_experiment(self):
        """
        http://wiki.quantsoftware.org/index.php?title=CompInvesti_Homework_7
        """
        """
        dataobj = da.DataAccess('Yahoo')
        symbols = dataobj.get_symbols_from_list('sp5002012')
        symbols = symbols + ["SPY"]
        keys = ["close"]
        data = data_access.load("2008-01-01", "2009-12-31", 16, symbols, keys)
        events = find_events(data)
        write_strategy("data/orders_bollinger.csv", events, strategy)
        """
        #build_market(100000, "data/orders_bollinger.csv", "data/market_sim_bollinger.csv")
        analise_market("data/market_sim_bollinger.csv", "$SPX", "data/market_sim_bollinger.png")

if __name__ == '__main__':
    unittest.main()
