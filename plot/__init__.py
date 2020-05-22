# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter
import numpy as np
import pandas as pd
import datetime as dt
import util


class XFormatter(Formatter):
    def __init__(self):
        pass

    def __call__(self, x, pos=0):
        td = dt.datetime.fromtimestamp(x/1000)
        t = dt.time(td.hour, td.minute, td.second)
        return t.strftime("%H:%M:%S.%s")


class YFormatter(Formatter):
    def __init__(self, incr):
        self.incr = incr


    def __call__(self, x, pos=0):
        return x * self.incr


def single_plot(sec, yList, incrPrice=1, rate=None):
    '''
    usage example:
        single_plot(sec, ['bid0', 'wmp', 'ask0'])
    '''
    orig = sec.origtime.apply(lambda t: util.is_trading_time(t))
    sessions = [i for i in range(util.trading_phases()) if (orig == i).sum() > 0 ]

    fig = plt.figure()
    plt.subplots_adjust(wspace=0, hspace=0)

    openPrice = sec.wmp[pd.notnull(sec.wmp)].iloc[0]
    spread = 0
    if rate is None:
        low = sec.wmp.min()

        upper = sec.wmp.max()

        spread = np.maximum(np.abs(openPrice - low), np.abs(openPrice - upper)) * 1.1
    else:
        spread = (openPrice * rate)

    for i in range(len(sessions)):
        ax = plt.subplot(1, len(sessions), i + 1)
        xl = sec.origtime[orig == sessions[i]]

        for f in yList:
            #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
            line, = ax.plot(xl, sec[f][orig == sessions[i]])

            line.set_label(f)

        plt.ylim(openPrice - spread, openPrice + spread)
        plt.xticks(rotation=270)

        if i != 0:
            #ax.set_yticks([])
            ax.get_yaxis().set_visible(False)
            ax.spines['left'].set_visible(False)


        # 只在最后一张图上加legend
        if i == len(sessions) - 1:
            ax.legend()

        # 调整刻度数据显示
        ax.xaxis.set_major_formatter(XFormatter())
        ax.yaxis.set_major_formatter(YFormatter(incrPrice))

    plt.show()


#def multi_plot(secList, yList, secNames=None):
#    if secNames is None:
#        secNames = [str(s.secid.iloc[0]) for s in secList]
#
#    if len(secList) != len(secNames):
#        return
#
#    fig, ax = plt.subplots()
#    for i, s in enumerate(secList):
#        for f in yList:
#            #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
#            line, = ax.plot(s.origtime, s[f])
#            line.set_label(secNames[i] + '_' + f)
#    ax.legend()
#    plt.show()


if __name__ == "__main__":
    print(util.is_trading_time(1589765734000))
