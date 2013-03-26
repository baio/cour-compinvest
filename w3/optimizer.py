__author__ = 'baio'
import datetime as dt
from w3 import simulate

def optimize(dt_start, dt_end, ls_symbols):
    max_sharpe = 0
    max_sharpe_alloc = []
    for i1 in range(0, 11):
        for i2 in range(0, 11):
            for i3 in range(0, 11):
                for i4 in range(0, 11):
                    k1 = float(i1) / 10
                    k2 = float(i2) / 10
                    k3 = float(i3) / 10
                    k4 = float(i4) / 10
                    if k1 + k2 + k3 + k4 == 1:
                        alloc = [k1, k2, k3, k4]
                        vol, daily_ret, sharpe, cum_ret = simulate.simulate(dt_start, dt_end, ls_symbols, alloc)
                        if sharpe > max_sharpe:
                            max_sharpe = sharpe
                            max_sharpe_alloc = alloc
    print max_sharpe
    print max_sharpe_alloc


optimize(dt.datetime(2010, 1, 1), dt.datetime(2010, 12, 31), ['AAPL', 'GOOG', 'IBM', 'MSFT'])