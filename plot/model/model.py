# -*- coding:utf-8 -*-
from config import *
from ..util import *

import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


_marker = ('.','1','2','3','4','+','x','|','^','v','<','>')

def model(nosmx, ocmx, ptmx=None):
    nosTime = nosmx.time.apply(lambda t: is_trading_time(t/10**9))
    nosSessions = [i for i in range(trading_phases()) if (nosTime == i).sum() > 0 ]

    ocTime = ocmx.time.apply(lambda t: is_trading_time(t/10**9))

    ptTime = ptmx.time.apply(lambda t: is_trading_time(t/10**9)) \
            if ptmx is not None else None
    # ptSessions = [i for i in range(trading_phases()) if (nosTime == i).sum() > 0] \
    #         if ptmx is not None else []

    # N = max(len(nosSessions), len(ptSessions))
    N = len(nosSessions)
    for i in range(N):
        ax = plt.subplot(1, N, i + 1)

        obf = (nosTime == nosSessions[i]) & (nosmx.side == 1) & (nosmx.poseff == 'O')
        for j in range(len(_marker)):
            mf = (nosmx.ordid % len(_marker) == j)
            xl = nosmx.time[obf & mf]
            yl = nosmx.price[obf & mf]
            ax.scatter(xl, yl, s=20, c='r', marker=_marker[j])

        fbf = (nosTime == nosSessions[i]) & (nosmx.side == 1) & (nosmx.poseff == 'T')
        for j in range(len(_marker)):
            mf = (nosmx.ordid % len(_marker) == j)
            xl = nosmx.time[fbf & mf]
            yl = nosmx.price[fbf & mf]
            ax.scatter(xl, yl, s=20, c='y', marker=_marker[j])

        osf = (nosTime == nosSessions[i]) & (nosmx.side == -1) & (nosmx.poseff == 'O')
        for j in range(len(_marker)):
            mf = (nosmx.ordid % len(_marker) == j)
            xl = nosmx.time[osf & mf]
            yl = nosmx.price[osf & mf]
            ax.scatter(xl, yl, s=20, c='g', marker=_marker[j])

        fsf = (nosTime == nosSessions[i]) & (nosmx.side == -1) & (nosmx.poseff == 'T')
        for j in range(len(_marker)):
            mf = (nosmx.ordid % len(_marker) == j)
            xl = nosmx.time[fsf & mf]
            yl = nosmx.price[fsf & mf]
            ax.scatter(xl, yl, s=20, c='k', marker=_marker[j])

        cf = (ocTime == nosSessions[i])
        for j in range(len(_marker)):
            mf = (ocmx.ordid % len(_marker) == j)
            xl = ocmx.time[cf & mf]
            yl = ocmx.wmp[cf & mf]
            ax.scatter(xl, yl, s=20, c='m', marker=_marker[j])

        f = ptTime == nosSessions[i]
        xl = ptmx.time[f]
        yl = ptmx.wmp[f]
        # ax.scatter(xl, yl, s=1, c='b')
        ax.plot(xl, yl, markersize=1)

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

