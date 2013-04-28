__author__ = 'baio'

import numpy as np
import copy
from CompInvest.tech_analizer import bollinger_df
import pandas as pd

def find_events(d_data, ndays=20):

    df_close = d_data['close']
    vals = bollinger_df(df_close, ndays)
    vals_merged = pd.merge(vals, vals.shift(1), left_index=True, right_index=True)

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    for symbol in vals.columns:
        df_events.ix[(vals_merged["%s.x" % symbol] <= -2) & (vals_merged["%s.y" % symbol] >= -2) & (vals_merged["SPY.x"] >= 1), symbol] = 1

    return df_events


def find_events_h6(d_data, ndays=20):

    df_close = d_data['close']
    vals = bollinger_df(df_close, ndays)
    vals_merged = pd.merge(vals, vals.shift(1), left_index=True, right_index=True)

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    for symbol in vals.columns:
        df_events.ix[(vals_merged["%s.x" % symbol] < -2) & (vals_merged["%s.y" % symbol] >= -2) & (vals_merged["SPY.x"] >= 1.5), symbol] = 1

    return df_events

def find_events_h7(d_data, ndays=20):

    df_close = d_data['close']
    vals = bollinger_df(df_close, ndays)
    vals_merged = pd.merge(vals, vals.shift(1), left_index=True, right_index=True)

    # Creating an empty dataframe
    df_events = copy.deepcopy(df_close)
    df_events = df_events * np.NAN

    for symbol in vals.columns:
        df_events.ix[(vals_merged["%s.x" % symbol] < -2) & (vals_merged["%s.y" % symbol] >= -2) & (vals_merged["SPY.x"] >= 1.4), symbol] = 1

    return df_events
