# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter
import pandas as pd
import datetime as dt


_tradingTime = [
        [dt.time(21, 00, 0), dt.time(23, 00, 0)],
        [dt.time( 9,  0, 0), dt.time(10, 15, 0)],
        [dt.time(10, 30, 0), dt.time(11, 30, 0)],
        [dt.time(13,  0, 0), dt.time(15, 00, 0)],


        #[dt.time( 9, 0, 0), dt.time(9, 1, 0)],
        #[dt.time( 9, 1, 0), dt.time(9,  2, 0)],
]


def is_trading_time(x):
    td = dt.datetime.fromtimestamp(x/1000)
    t = dt.time(td.hour, td.minute, td.second)

    for i, v in enumerate(_tradingTime):
        if t >= v[0] and t < v[1] :
            return i

    return -1



class formatter(Formatter):
    def __init__(self):
        pass

    def __call__(self, x, pos=0):
        td = dt.datetime.fromtimestamp(x/1000)
        t = dt.time(td.hour, td.minute, td.second)
        return t.strftime("%H:%M:%S.%s")


def single_plot(sec, yList):
    '''
    usage example:
        single_plot(sec, ['bid0', 'wmp', 'ask0'])
    '''
    orig = sec.origtime.apply(lambda t: is_trading_time(t))
    sessions = [i for i in range(len(_tradingTime)) if (orig == i).sum() > 0 ]

    fig = plt.figure()
    plt.subplots_adjust(wspace=0, hspace=0)

    firstPrice = sec.wmp[pd.notnull(sec.wmp)].iloc[0]
    for i in range(len(sessions)):
        ax = plt.subplot(1, len(sessions), i + 1)
        xl = sec.origtime[orig == sessions[i]]
        # ax.set_xlim(xl[0])
        for f in yList:
            #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
            line, = ax.plot(xl, sec[f][orig == sessions[i]])

            line.set_label(f)

        plt.ylim(firstPrice * 0.9, firstPrice * 1.1)
        plt.xticks(rotation=270)

        if i != 0:
            #ax.set_yticks([])
            ax.get_yaxis().set_visible(False)
            ax.spines['left'].set_visible(False)


        # 只在最后一张图上加legend
        if i == len(sessions) - 1:
            ax.legend()
        ax.xaxis.set_major_formatter(formatter())

    plt.show()


def multi_plot(secList, yList, secNames=None):
    if secNames is None:
        secNames = [str(s.secid.iloc[0]) for s in secList]

    if len(secList) != len(secNames):
        return

    fig, ax = plt.subplots()
    for i, s in enumerate(secList):
        for f in yList:
            #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
            line, = ax.plot(s.origtime, s[f])
            line.set_label(secNames[i] + '_' + f)
    ax.legend()
    plt.show()


if __name__ == "__main__":
    print(is_trading_time(1589765734000))

