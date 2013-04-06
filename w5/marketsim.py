__author__ = 'baio'
import sys
import numpy as np
import datetime as dt
import QSTK.qstkutil.DataAccess as da
import QSTK.qstkutil.qsdateutil as du
import copy
import pandas as pa

if __name__ == '__main__':

    d_value = float(sys.argv[1])
    ls_orders_file = sys.argv[2]
    ls_values_file = sys.argv[3]


    na_data = np.loadtxt(ls_orders_file, dtype=str, delimiter=',')
    na_data = [{"date": dt.datetime(int(t[0]), int(t[1]), int(t[2])), "symbol": t[3],
                "is_buy": t[4] == "Buy", "amount": int(t[5])} for t in na_data]

    ls_symbols = set([t["symbol"] for t in na_data])
    ldt_dates = sorted([t["date"] for t in na_data])
    dt_min = min(ldt_dates)
    dt_max = max(ldt_dates) + dt.timedelta(days=1)

    ldt_timestamps = du.getNYSEdays(dt_min, dt_max, dt.timedelta(hours=16))

    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['close', 'close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    dd_own = copy.deepcopy(d_data['close'])
    dd_own = dd_own * 0
    ld_cash = dict()
    perv_owns = dict()
    perv_val = d_value

    for timestamp in ldt_timestamps:
        "next date actually"
        "update current owns accordingly to pervious owns"
        for symbol in perv_owns.keys():
            dd_own[symbol][timestamp] = perv_owns[symbol]
        found_orders = [t for t in na_data if (t["date"] + dt.timedelta(hours=16)) == timestamp]
        for order in found_orders:
            symbol = order["symbol"]
            amt = order["amount"]
            d_actual_close = d_data["close"][symbol]
            price_actual = d_actual_close[timestamp]
            d_order_value = price_actual * amt
            if order["is_buy"]:
                d_order_value *= -1
            else:
                amt *= -1
            d_value += d_order_value
            dd_own[symbol][timestamp] += amt
            perv_owns[symbol] = dd_own[symbol][timestamp]
        #perv_val = d_value
        ld_cash[timestamp] = d_value
        #print timestamp, d_value

    print dd_own.head(10)
    print dd_own.tail(10)

    with open(ls_values_file, "w+") as f_out:
        for timestamp in ldt_timestamps:
            cash = ld_cash[timestamp]
            value = 0
            for symbol in ls_symbols:
                own = dd_own[symbol][timestamp]
                value +=  d_data["close"][symbol][timestamp] * own
            total = cash + value
            f_out.write("{0}, {1}, {2}, {3}\n".format(timestamp.year, timestamp.month, timestamp.day, int(total)))



        #f_out.write("{0}, {1}, {2}, {3}\n".format(date.year, date.month, date.day, i_amount))
        #f_out.write("{0}, {1}, {2}, {3}\n".format(dt_max.year, dt_max.month, dt_max.day, i_amount))
