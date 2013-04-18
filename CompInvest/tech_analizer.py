__author__ = 'baio'

import datetime as dt
import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.DataAccess as da
import matplotlib.pyplot as plt
import pandas as pd

def bollinger_df(df_close, ndays, plot_file=None):

    rolling_mean = pd.rolling_mean(df_close, ndays)
    rolling_std = pd.rolling_std(df_close, ndays)

    upper = rolling_mean + rolling_std
    lower = rolling_mean - rolling_std

    bollinger_val = (df_close - rolling_mean) / (rolling_std)

    if plot_file is not None:
        plt.clf()
        plt.plot(df_close)
        plt.plot(upper)
        plt.plot(lower)
        plt.plot(rolling_mean)
        #locs, labels = plt.xticks()
        #plt.xticks(locs, df_close.index, rotation=30)
        plt.xticks(rotation=30)
        plt.legend(["close", "mean", "upper", "lower"])
        plt.ylabel("Value")
        plt.xlabel("Date")
        plt.savefig(plot_file, format='png')

    return bollinger_val


def bollinger(dt_start, dt_end, ls_symbols, ndays, plot_file=None):

    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    dataobj = da.DataAccess('Yahoo')
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ['close'])

    return bollinger_df(ldf_data[0], ndays, plot_file)







