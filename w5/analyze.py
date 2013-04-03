__author__ = 'baio'

import sys
import datetime as dt
import math
import QSTK.qstkutil.tsutil as tsu
import pandas as pa
import numpy as np

if __name__ == '__main__':

    ls_values_file = sys.argv[1]
    ls_symbol = sys.argv[2]

    na_data = np.loadtxt(ls_values_file, delimiter=',')

    na_data = np.array([(dt.datetime(int(t[0]), int(t[1]), int(t[2])), t[3]) for t in na_data])

    print "Final value of portfolio : ", na_data[len(na_data) - 1]
    print "Date range : ", na_data[0][0], " - ", na_data[len(na_data) - 1][0]

    na_data = na_data[:, 1]

    # diff between current & perv date
    tsu.returnize0(na_data)

    std_dev = np.std(na_data)
    mean = np.mean(na_data)
    sharpe = math.sqrt(252) * mean / std_dev
    cum_daily = np.cumprod([t + 1 for t in na_data], axis=0, dtype=float)


    print "Sharpe ratio of fund : ", sharpe
    print "Total return of fund : ", cum_daily[len(cum_daily) - 1]
    print "Std deviation : ", std_dev
    print "Daily return : ", mean

