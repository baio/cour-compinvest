__author__ = 'baio'

import numpy as np
import math as math

import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.tsutil as tsu

def simulate(dt_start, dt_end, ls_symbols, allocation):

    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    #noramlize and accumulate
    values = d_data['close'].values
    values = values / values[0, :]
    values = values * allocation

    # sum per day
    cum_day = values.sum(axis=1)

    na_rets = cum_day.copy()

    # diff between current & perv date
    tsu.returnize0(na_rets)

    std_dev = np.std(na_rets)
    mean = np.mean(na_rets)
    sharpe = math.sqrt(252) * mean / std_dev
    # perv val * current val
    cum_daily = np.cumprod(1 + na_rets, axis=0, dtype=float)


    return std_dev, mean, sharpe, cum_daily[len(cum_daily) -1]


