# -*- coding:utf-8 -*-
from config import *
from ..util import *

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


def sdm_scatter(sec, y):
    sessions = np.unique(sec.ssid)

    fig = plt.figure()
    plt.subplots_adjust(wspace=0, hspace=0)
    for i in range(len(sessions)):
        ax = plt.subplot(1, len(sessions), i + 1)
        xl = sec.tms[sec.ssid == sessions[i]]
        ax.scatter(xl, sec[y][xl], s=1, label=y)
        ax.set_label(y)

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
        # ax.yaxis.set_major_formatter(Tick2Price(incrPrice))
    plt.show()
