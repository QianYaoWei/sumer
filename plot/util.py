from config import *

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter

class Timestamp2DateTime(Formatter):
    def __init__(self):
        pass

    def __call__(self, x, pos=0):
        td = dt.datetime.fromtimestamp(x/1000)
        t = dt.time(td.hour, td.minute, td.second)
        return t.strftime('%H:%M:%S.%s')


class Tick2Price(Formatter):
    def __init__(self, incr):
        self.incr = incr

    def __call__(self, x, pos=0):
        return x * self.incr


__tradingTime = [
        [dt.time(21, 00, 0), dt.time(23, 00, 0)],
        [dt.time( 9,  0, 0), dt.time(10, 15, 0)],
        [dt.time(10, 30, 0), dt.time(11, 30, 0)],
        [dt.time(13,  0, 0), dt.time(15, 00, 0)],


        #[dt.time( 9, 0, 0), dt.time(9, 1, 0)],
        #[dt.time( 9, 1, 0), dt.time(9,  2, 0)],
]

def trading_phases():
    return len(__tradingTime)


def is_trading_time(x):
    td = dt.datetime.fromtimestamp(x/1000)
    t = dt.time(td.hour, td.minute, td.second)

    for i, v in enumerate(__tradingTime):
        if t >= v[0] and t < v[1] :
            return i

    return -1
