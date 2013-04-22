__author__ = 'baio'

import datetime as dt
import math
import QSTK.qstkutil.tsutil as tsu
import numpy as np
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import matplotlib.pyplot as plt
import pandas as pd

def bollinger(dt_start, dt_end, ls_symbols, ndays):

    #rolling statistic

    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    dataobj = da.DataAccess('Yahoo')
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ['close'])
    df_close = ldf_data[0]

    rolling_mean = pd.rolling_mean(df_close, ndays)
    rolling_std = pd.rolling_std(df_close, ndays)

    upper = rolling_mean + rolling_std
    lower = rolling_mean - rolling_std

    bollinger_val = (df_close - rolling_mean) / (rolling_std)

    plt.clf()
    plt.plot(df_close)
    plt.plot(bollinger_val)
    plt.plot(upper)
    plt.plot(lower)
    #plt.plot(rolling_mean)
    plt.savefig("tst.png", format='png')

    return bollinger_val, df_close, rolling_mean, rolling_std










