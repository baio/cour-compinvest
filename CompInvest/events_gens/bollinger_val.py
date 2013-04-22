__author__ = 'baio'

import numpy as np
import copy
import CompInvest as ci

def find_events(d_data, ndays=20):

    df_close = d_data['close']
    vals = ci.tech_analizer.bollinger_df(df_close, ndays)

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    """
    Here should define what the gap between pervious and next event should be.
    For example if yestoday we made sell event, today we should ignore sell event.
    Or should we ignore sell event till after next buy event?
    """
    df_events[vals >= 1] = 1
    df_events[vals <= -1] = -1

    return df_events, vals
