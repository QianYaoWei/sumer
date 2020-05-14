import numpy as np
import matplotlib.pyplot as plt


def single_plot(sec, fields):
    fig, ax = plt.subplots()
    for f in fields:
        line = ax.plot(sec.origtime, sec[f])
        line

    ax.legend()

    plt.show()
