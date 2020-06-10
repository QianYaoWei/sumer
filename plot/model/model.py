# -*- coding:utf-8 -*-
from config import *
from ..util import *

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


_marker = ('.','1','2','3','4','+','x','|','^','v','<','>')

def model(nosmx, ocmx, ptmx=None):
    nosTime = nosmx.time.apply(lambda t: is_trading_time(t/10**9))
    nosSessions = [i for i in range(trading_phases()) if (nosTime == i).sum() > 0 ]

    ptTime = ptmx.time.apply(lambda t: is_trading_time(t/10**9)) \
            if ptmx is not None else None

    ptSessions = [i for i in range(trading_phases()) if (nosTime == i).sum() > 0] \
            if ptmx is not None else []

    # N = max(len(nosSessions), len(ptSessions))
    N = len(nosSessions)
    for i in range(N):
        ax = plt.subplot(1, N, i + 1)
        if i < len(nosSessions):

            bf = (nosTime == nosSessions[i]) & (nosmx.side == 1)
            for j in range(len(_marker)):
                mf = (nosmx.ordid % len(_marker) == j)
                xl = nosmx.time[bf & mf]
                yl = nosmx.price[bf & mf]
                ax.scatter(xl, yl, s=10, c='r', marker=_marker[j])


            # sf = (nosTime == nosSessions[i]) & (nosmx.side == -1)
            # for j in range(len(_marker)):
            #     mf = (nosmx.ordid % len(_marker) == j)
            #     xl = nosmx.time[sf & mf]
            #     yl = nosmx.price[sf & mf]
            #     ax.scatter(xl, yl, s=3, c='g', marker=_marker[j])


        # if i < len(ptSessions):
        #     f = ptTime == ptSessions[i]
        #     xl = ptmx.time[f]
        #     yl = ptmx.wmp[f]
        #     ax.scatter(xl, yl, s=1, c='b')

        # plt.ylim(openPrice - spread, openPrice + spread)
        plt.xticks(rotation=270)

        if i != 0:
            #ax.set_yticks([])
            ax.get_yaxis().set_visible(False)
            ax.spines['left'].set_visible(False)

        # 只在最后一张图上加legend
        # if i == N - 1:
        #     ax.legend()

        # 调整刻度数据显示
        ax.xaxis.set_major_formatter(Timestamp2DateTime(10**9))
        ax.yaxis.set_major_formatter(Tick2Price(1))


    plt.show()

