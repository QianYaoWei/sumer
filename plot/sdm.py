# -*- coding:utf-8 -*-
from config import *
from .util import *

import util
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


def sdm(sec, yList, incrPrice=1, rate=None):
    '''
    usage example:
        sdm(sec, ['bid0', 'wmp', 'ask0'])
    '''
    sessions = np.unique(sec.ssid)

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
        xl = sec.tms[sec.ssid == sessions[i]]

        for f in yList:
            line, = ax.plot(xl, sec[f][xl])

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


#def sdm_scatter(sec, y):
#    sessions = np.unique(sec.ssid)
#
#    fig = plt.figure()
#    plt.subplots_adjust(wspace=0, hspace=0)
#    for i in range(len(sessions)):
#        ax = plt.subplot(1, len(sessions), i + 1)
#        xl = sec.tms[sec.ssid == sessions[i]]
#
#        line, = ax.scatter(xl, sec[y][xl])
#
#        line.set_label(y)
#
#        plt.xticks(rotation=270)
#
#        if i != 0:
#            #ax.set_yticks([])
#            ax.get_yaxis().set_visible(False)
#            ax.spines['left'].set_visible(False)
#
#
#        # 只在最后一张图上加legend
#        if i == len(sessions) - 1:
#            ax.legend()
#
#        # 调整刻度数据显示
#        ax.xaxis.set_major_formatter(Timestamp2DateTime())
#        # ax.yaxis.set_major_formatter(Tick2Price(incrPrice))
#
#    plt.show()
#
#
#
#
#
#
#
#    index = sec['origtime'].apply(lambda t: util.is_trading_time(t) != -1)
#    orig = sec['origtime'][index]
#
#    min = sec.tms.min()
#    max = sec.tms.max()
#    ticks = pd.Series(np.linspace(min, max, (max - min + interval)/interval))
#
#    t0 = ticks.iloc[0:-1]
#    t1 = ticks.iloc[1:]
#    sum = np.zeros(ticks.size)
#
#    curIndex = 0
#    for index, row in sec.iterrows():
#        for i in range(curIndex, ticks.size - 1):
#            if t0.iloc[i] <= row['origtime'] < t1.iloc[i]:
#                sum[i + 1] += row.lastsz
#                curIndex = i
#
#    #for i in range(0, sum.size - 1):
#    #    # index = (sec.origtime >= t0.iloc[i]) & (sec.origtime < t1.iloc[i])
#    #    sum[i + 1] = sec.loc[t0.iloc[i] : t1.iloc[i]].lastsz.sum()
#
#
#    ax = plt.subplot(1, 2, 1)
#    #line, = ax.plot(ticks, sum)
#    ax.scatter(ticks, sum, s=1, label='lastsz')
#    ax.xaxis.set_major_formatter(Timestamp2DateTime())
#    ax.legend()
#    print(ticks)
#
#    print(sec.loc[ticks].ttvol)
#    # ==================
#    ax = plt.subplot(1, 2, 2)
#    ax.scatter(ticks, sec.loc[ticks].ttvol, s=1, label='ttvol')
#    ax.xaxis.set_major_formatter(Timestamp2DateTime())
#    ax.legend()
#    # ==================
#
#    plt.xticks(rotation=270)
#    plt.show()
#    return sum
