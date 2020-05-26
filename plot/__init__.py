# -*- coding:utf-8 -*-
from .pt import pt

from .sdm import sdm

from config import *
from .util import *

import util
import matplotlib.pyplot as plt
from matplotlib.ticker import Formatter


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
