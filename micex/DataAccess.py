__author__ = 'baio'

import glob
import pandas as pa
from datetime import datetime as dt

daily_hist_path = "micex-equity-per-day"

def get_data(timestamps, symbols, keys):

    if any(t.time().hour + t.time().minute + t.time().second != 0 for t in timestamps):
        raise Exception("Data available only at daily basis. You only can use time = 0 in your timestamps parameter.")

    res = [pa.DataFrame(index=timestamps) for i in xrange(len(keys))]

    for symbol in symbols:
        path = glob.glob("../{}/{}_*.txt".format(daily_hist_path, symbol))

        if len(path) != 1:
            raise Exception("Can't find data for symbol {}.".format(symbol))
        df = pa.read_csv(path[0], header=0)
        df = df.rename(columns={"<TICKER>": "symbol", "<PER>": "per", "<DATE>": "date",
                           "<TIME>": "time", "<OPEN>": "open", "<HIGH>": "high", "<LOW>": "low",
                           "<CLOSE>": "close", "<VOL>": "vol"})
        df.index = pa.Series(map(lambda x: dt.strptime(str(x), "%Y%m%d"), df.pop("date").values))
        df = df[keys]
        df = df.reindex(timestamps)
        for key_index, key in enumerate(keys):
            res[key_index][symbol] = df[key]

    return res








