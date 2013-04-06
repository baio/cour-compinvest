__author__ = 'baio'

import sys
import datetime as dt
import math
import QSTK.qstkutil.tsutil as tsu
import pandas as pa
import numpy as np
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import matplotlib.pyplot as plt

def analize(na_data):
    tsu.returnize0(na_data)

    std_dev = np.std(na_data)
    mean = np.mean(na_data)
    sharpe = math.sqrt(252) * mean / std_dev
    cum_daily = np.cumprod([t + 1 for t in na_data], axis=0, dtype=float)

    return sharpe, cum_daily[len(cum_daily) - 1], std_dev, mean

if __name__ == '__main__':

    ls_values_file = sys.argv[1]
    ls_symbol = sys.argv[2]

    na_data = np.loadtxt(ls_values_file, delimiter=',')

    na_data = np.array([(dt.datetime(int(t[0]), int(t[1]), int(t[2])), t[3]) for t in na_data])

    print "Final value of portfolio : ", na_data[len(na_data) - 1]
    dt_start = na_data[0][0]
    dt_end = na_data[len(na_data) - 1][0]
    print "Date range : ", dt_start, " - ", dt_end

    values = na_data[:, 1]

    sharpe, cum, std, mean = analize(values.copy())

    print "For portfolio "

    print "Sharpe ratio of fund : ", sharpe
    print "Total return of fund : ", cum
    print "Std deviation : ", std
    print "Daily return : ", mean

    #same for symbol
    dataobj = da.DataAccess('Yahoo')
    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end + dt.timedelta(days=1), dt_timeofday)

    ldf_data = dataobj.get_data(ldt_timestamps, [ls_symbol], ['actual_close'])

    symbol_values = ldf_data[0][ls_symbol].values
    sym_sharpe, sym_cum, sym_std, sym_mean = analize(symbol_values.copy())

    print "For benchmark symbol " + ls_symbol

    print "Sharpe ratio of fund : ", sym_sharpe
    print "Total return of fund : ", sym_cum
    print "Std deviation : ", sym_std
    print "Daily return : ", sym_mean

    #first_symbol_value = symbol_values[0]
    symbol_values = [t / symbol_values[0] * values[0] for t in symbol_values]
    plt.clf()
    plt.xticks(rotation=30)
    plt.plot(ldt_timestamps, values)
    plt.plot(ldt_timestamps, symbol_values)
    plt.legend(["Portfolio", ls_symbol])
    plt.ylabel("Daily Value")
    plt.xlabel("Date")
    plt.savefig('graph.png', format='png')
