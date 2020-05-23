# -*- coding:utf-8 -*-
import qt

import sdm

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

