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
        line.set_label(f)

    ax.legend()
    plt.show()


def multi_plot(secList, x, yList, secNames=None):
    if secNames is None:
        secNames = [str(s.secid.iloc[0]) for s in secList]

    if len(secList) != len(secNames):
        return

    fig, ax = plt.subplots()
    for i, s in enumerate(secList):
        for f in yList:
            #pd.to_datetime(orig, unit='ms').dt.strftime('%H:%M:%S,%f')
            line, = ax.plot(s[x], s[f])
            line.set_label(secNames[i] + '_' + f)
    ax.legend()
    plt.show()
