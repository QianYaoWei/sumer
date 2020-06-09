# -*- coding:utf-8 -*-
from config import *
from ..util import *

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


def model(nos, oc):
    orig = nos.time.apply(lambda t: is_trading_time(t/10**9))
    sessions = [i for i in range(trading_phases()) if (orig == i).sum() > 0 ]

    for i in range(len(sessions)):
        ax = plt.subplot(1, len(sessions), i + 1)

        bf = (orig == sessions[i]) & (nos.side == 1)
        xl = nos.time[bf]
        yl = nos.price[bf]
        ax.scatter(xl, yl, s=1, c='r')

        sf = (orig == sessions[i]) & (nos.side == -1)
        xl = nos.time[sf]
        yl = nos.price[sf]
        ax.scatter(xl, yl, s=1, c='g')

        # plt.ylim(openPrice - spread, openPrice + spread)
        plt.xticks(rotation=270)

        if i != 0:
            #ax.set_yticks([])
            ax.get_yaxis().set_visible(False)
            ax.spines['left'].set_visible(False)

        # 只在最后一张图上加legend
        if i == len(sessions) - 1:
            ax.legend()

        # 调整刻度数据显示
        ax.xaxis.set_major_formatter(Timestamp2DateTime(10**9))
        ax.yaxis.set_major_formatter(Tick2Price(1))

    plt.show()

