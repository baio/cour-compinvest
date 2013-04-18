__author__ = 'baio'

import numpy as np
import copy

def find_events(s_maket_symbol, ls_symbols, d_data):
    """ Finding the event dataframe """
    df_close = d_data['actual_close']

    print "Finding Events"

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    # Time stamps for the event range
    ldt_timestamps = df_close.index

    for s_sym in ls_symbols:
        for i in range(1, len(ldt_timestamps)):
            # Calculating the returns for this timestamp
            price_today = df_close[s_sym].ix[ldt_timestamps[i]]
            price_yest = df_close[s_sym].ix[ldt_timestamps[i - 1]]

            if price_yest >= 9 and price_today < 9:
                df_events[s_sym].ix[ldt_timestamps[i]] = 1

    return df_events


