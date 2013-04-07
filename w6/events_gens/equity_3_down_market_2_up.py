__author__ = 'baio'

import numpy as np
import copy

def find_events(s_maket_symbol, ls_symbols, d_data):
    """ Finding the event dataframe """
    df_close = d_data['close']
    ts_market = df_close[s_maket_symbol]

    print "Finding Events"

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    # Time stamps for the event range
    ldt_timestamps = df_close.index

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            f_symprice_today = df_close[s_sym].ix[ldt_timestamps[i]]
            f_symprice_yest = df_close[s_sym].ix[ldt_timestamps[i - 1]]
            f_marketprice_today = ts_market.ix[ldt_timestamps[i]]
            f_marketprice_yest = ts_market.ix[ldt_timestamps[i - 1]]
            f_symreturn_today = (f_symprice_today / f_symprice_yest) - 1
            f_marketreturn_today = (f_marketprice_today / f_marketprice_yest) - 1

            # Event is found if the symbol is down more then 3% while the
            # market is up more then 2%
            if f_symreturn_today <= -0.03 and f_marketreturn_today >= 0.02:
                df_events[s_sym].ix[ldt_timestamps[i]] = 1

    return df_events


