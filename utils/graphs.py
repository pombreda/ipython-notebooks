# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


def barh(x, y, filename, figsize=(10, 10), title=None, footer=None):
    plt.figure(figsize=figsize)
    R = range(len(x))

    rects = plt.barh(
        R,
        y,
        height=.8,
        color='#4682B4',
        alpha=.8)

    for i, rect in enumerate(rects):
        width = rect.get_width()
        label = '  ' + str(y[i])
        plt.text(width + 0.25,
                 rect.get_y() + rect.get_height() / 2.,
                 label,
                 va='center',
                 fontsize=13,
                 color='#666666')

    # Move y ticks down a bit to align with the bars.
    ypos = [r + 0.35 for r in R]

    # Fix possible problems with unicode chars.
    labels = [l.decode('utf-8') for l in x]

    plt.yticks(ypos, labels)

    # Hide x tick labels.
    plt.xticks(np.arange(0, 5, 1), [''])

    # Hide borders around plot.
    ax = plt.axes()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    if title:
        plt.title(title.decode('utf-8'), color='#444444')

    if footer:
        ax.text(
            max(y) / 2,
            -.2,
            footer.decode('utf-8'),
            fontsize=12.5,
            va='top',
            color='#444444')

    plt.savefig(filename, bbox_inches='tight')