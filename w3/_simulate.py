__author__ = 'baio'

import numpy as np
import math as math

import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da

import matplotlib.pyplot as plt

def simulate(dt_start, dt_end, ls_symbols, allocation):

    dt_timeofday = dt.timedelta(hours=16)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

    c_dataobj = da.DataAccess('Yahoo', cachestalltime=0)
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    values = d_data['close'].values
    values = values / values[0, :]
    values = values * allocation

    """
    plt.clf()
    plt.plot(ldt_timestamps, values / values[0, :])
    plt.legend(ls_symbols)
    plt.savefig('simulate.pdf', format='pdf')
    """

    # current date
    values_c = np.array(values.copy())
    # perv date
    values_p = np.array(values.copy())

    values_c = np.vstack((values, values[len(values) - 1, :]))
    values_p = np.vstack((values[0, :], values))

    daily_rets = (values_c / values_p - 1)[0:len(values), :]


    std_metric = daily_rets.std(axis=0)
    mean_metric = daily_rets.mean(axis=0)

    sharpe = math.sqrt(252) * mean_metric / std_metric
    cum_ret = values[len(values) - 1, :] / values[0, :]

    return np.nansum(std_metric), np.nansum(mean_metric), np.nansum(sharpe), np.nansum(cum_ret)

