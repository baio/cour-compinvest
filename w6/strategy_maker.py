__author__ = 'baio'

"Part 1: Revise your event analyzer to output a series of trades based on events;" \
" Instead of putting a 1 in the event matrix, output to a file"

import QSTK.qstkutil.qsdateutil as du
import datetime as dt
import QSTK.qstkutil.DataAccess as da

def find_events(dt_start, dt_end, s_market_symbol, ls_symbols, func_find_particular_events):
    """

    """
    ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt.timedelta(hours=16))
    if not s_market_symbol in ls_symbols: ls_symbols.append (s_market_symbol)
    dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data))

    df_events = func_find_particular_events(s_market_symbol, ls_symbols, d_data)

    return df_events, d_data

def generate_strategy(df_events, func_particular_strategy_gen):
    return func_particular_strategy_gen(df_events)

def write_strategy(out_file_name, df_events, func_particular_strategy_gen):
    buy, sell = generate_strategy(df_events, func_particular_strategy_gen)
    ls_symbols = buy.columns
    with open(out_file_name, "w") as f:
        for timestamp in buy.index:
            for symbol in ls_symbols:
                buy_amt = buy.ix[timestamp][symbol]
                sell_amt = sell.ix[timestamp][symbol]
                if buy_amt == buy_amt:
                    f.write("{},{},{},{},Buy,{:n}\n".format(timestamp.year, timestamp.month, timestamp.day, symbol, buy_amt))
                if sell_amt == sell_amt:
                    f.write("{},{},{},{},Sell,{:n}\n".format(timestamp.year, timestamp.month, timestamp.day, symbol, -1 * sell_amt))
