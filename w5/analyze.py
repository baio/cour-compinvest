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

    na_rets = na_data[:, 1].copy()

    # diff between current & perv date
    tsu.returnize0(na_rets)

    print na_rets

    std_dev = np.std(na_rets)
    mean = np.mean(na_rets)
    sharpe = math.sqrt(252) * mean / std_dev
    # perv val * current val
    cum_daily = np.cumprod(1 + na_rets, axis=0, dtype=float)

