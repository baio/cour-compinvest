__author__ = 'baio'
import numpy as np
import datetime as dt
import pandas as pa

def generate_strategy(df_events):
    """
    df_events.AAPL[len(df_events) - 3] = 1
    df_events.AAPL[len(df_events) - 4] = 1
    df_events.AAPL[len(df_events) - 6] = 1
    """
    buy = df_events * 100
    sell = buy * -1
    sell = sell.shift(5)
    sell.ix[len(sell) - 1] = sell.ix[len(sell) - 1].fillna(0) - 1 * buy.tail(5).sum()

    return buy, sell

    """
    if i+5 >= len(ldt_timestamps)
    use len(ldt_timestamps) - 1 as sell date.

    print buy.combine_first(sell).tail()
    print buy.tail()
    print sell.tail()
    """


