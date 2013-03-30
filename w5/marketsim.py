__author__ = 'baio'
import sys
import numpy as np
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du

if __name__ == '__main__':

    i_amount = float(sys.argv[1])
    ls_orders_file = sys.argv[2]
    ls_values_file = sys.argv[3]

    na_data = np.loadtxt(ls_orders_file,
                         dtype={'names': ('year', 'month', 'day', 'symbol', 'buysell', 'amount'), 'formats': ('i4', 'i4', 'i4', 'S10', 'S10', 'i4')},
                         delimiter=',')

    ls_symbols = set([t['symbol'] for t in na_data])
    ldt_dates = [dt.datetime(t['year'], t['month'], t['day']) for t in na_data]
    dt_min = min(ldt_dates)
    dt_max = max(ldt_dates) + dt.timedelta(days=1)

    ldt_timestamps = du.getNYSEdays(dt_min, dt_max, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['close', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    with open(ls_values_file, "w+") as f_out:
        for timestamp in ldt_timestamps:
            date = timestamp.date()
            found_orders = [t for t in na_data if dt.datetime(t['year'], t['month'], t['day']).date() == date]
            i_order_amount = 0
            for order in found_orders:
                d_actual_close = d_data['actual_close'][order['symbol']]
                price_actual = d_actual_close[timestamp] 
                i_order_amount = price_actual * order["amount"]
                if order["buysell"] == "Buy":
                    i_order_amount *= -1
            f_out.write("{0}, {1}, {2}, {3}\n".format(date.year, date.month, date.day, i_amount))
            i_amount += i_order_amount
        f_out.write("{0}, {1}, {2}, {3}\n".format(dt_max.year, dt_max.month, dt_max.day, i_amount))


#find all symbols
    #find min, max date
    #load all symbols dt min - max
    #loop

    """
    dt_start = dt.datetime(2008, 1, 1)
    dt_end = dt.datetime(2009, 12, 31)
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_symbols = dataobj.get_symbols_from_list('sp5002012')
    ls_symbols.append('SPY')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    df_events = find_events(ls_symbols, d_data)
    print "Creating Study"
    ep.eventprofiler(df_events, d_data, i_lookback=20, i_lookforward=20,
                     s_filename='MyEventStudy.pdf', b_market_neutral=True, b_errorbars=True,
                     s_market_sym='SPY')
    """
