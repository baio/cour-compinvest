__author__ = 'baio'

import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da

def load_with_func(start, end, time, symbols, keys,  func_get_data, func_get_days):
    dt_start = dt.datetime.strptime(start, "%Y-%m-%d")
    dt_end = dt.datetime.strptime(end, "%Y-%m-%d")
    ldt_timestamps = func_get_days(dt_start, dt_end, dt.timedelta(hours=time))
    return func_get_data(ldt_timestamps, symbols, keys)

def load(start, end, time, symbols, keys,  data_provider_name="Yahoo", dates_provider_name="NYC"):

    func_get_data = {
        "Yahoo": da.DataAccess('Yahoo').get_data
    }.get(data_provider_name, None)

    func_get_dates = {
        "NYC": du.getNYSEdays
    }.get(dates_provider_name, None)

    if func_get_data is None: raise Exception("data provider not found")
    if func_get_dates is None: raise Exception("dates provider not found")

    return dict(zip(keys, load_with_func(start, end, time, symbols, keys, func_get_data, func_get_dates)))
