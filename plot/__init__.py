# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt


def single_plot(sec, x, yList):
    '''
    usage example:
        single_plot(sec, 'origtime', ['bid0', 'wmp', 'ask0'])
    '''
    fig, ax = plt.subplots()
    for f in yList:
        #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
        line, = ax.plot(sec[x], sec[f])
        line.label = f

    ax.legend()
    plt.show()
