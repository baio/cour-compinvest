__author__ = 'baio'


import unittest
from micex import DataAccess
import pandas as pa
import datetime as dt


class TestDataAccessFunctions(unittest.TestCase):

    def test_DataAccess(self):
        stamps = pa.DateRange('2012-2-10', periods=5)
        data = DataAccess.get_data(stamps, ["GAZP", "TGKI"], ["close", "vol"])
        for a in data:
            print a.head()

if __name__ == '__main__':
    unittest.main()
