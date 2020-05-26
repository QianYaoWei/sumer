# -*- coding:utf-8 -*-
from config import *
from .util import *

import util
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


def pt(sec, yList, incrPrice=1, rate=None):
    '''
    usage example:
        pt(sec, ['bid0', 'wmp', 'ask0'])
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
        ax.xaxis.set_major_formatter(Timestamp2DateTime())
        ax.yaxis.set_major_formatter(Tick2Price(incrPrice))

    plt.show()


def lastsz_totalvol(sec, interval=500):
    '''
    interval->milli second
    '''
    index = sec['origtime'].apply(lambda t: util.is_trading_time(t) != -1)
    orig = sec['origtime'][index]

    min = orig.min()
    max = orig.max()
    ticks = pd.Series(np.linspace(min, max, (max - min + interval)/interval))

    t0 = ticks.iloc[0:-1]
    t1 = ticks.iloc[1:]
    sum = np.zeros(ticks.size)

    curIndex = 0
    for index, row in sec.iterrows():
        for i in range(curIndex, ticks.size - 1):
            if t0.iloc[i] <= row['origtime'] < t1.iloc[i]:
                sum[i + 1] += row.lastsz
                curIndex = i

    #for i in range(0, sum.size - 1):
    #    # index = (sec.origtime >= t0.iloc[i]) & (sec.origtime < t1.iloc[i])
    #    sum[i + 1] = sec.loc[t0.iloc[i] : t1.iloc[i]].lastsz.sum()


    ax = plt.subplot(1, 2, 1)
    #line, = ax.plot(ticks, sum)
    ax.scatter(ticks, sum, s=1, label='lastsz')
    ax.xaxis.set_major_formatter(Timestamp2DateTime())
    ax.legend()
    print(ticks)

    print(sec.loc[ticks].ttvol)
    # ==================
    ax = plt.subplot(1, 2, 2)
    ax.scatter(ticks, sec.loc[ticks].ttvol, s=1, label='ttvol')
    ax.xaxis.set_major_formatter(Timestamp2DateTime())
    ax.legend()
    # ==================

    plt.xticks(rotation=270)
    plt.show()
    return sum


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


if __name__ == '__main__':
    print(util.is_trading_time(1589765734000))

