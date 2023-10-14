import matplotlib.pyplot as plt

import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import matplotlib.pyplot as plt


def plot_data(
    x,
    y,
    plot_type="continuous",
    title="",
    x_label="",
    y_label="",
    fig_size=[20, 4],
    sub_plot=[1, 2, 1],
    ax=None,
    canvas=None,
):
    ax.clear()
    # Set plot parameters
    ax.figure.set_size_inches(fig_size[0], fig_size[1])
    # plt.subplot(sub_plot[0], sub_plot[1], sub_plot[2])

    # Create plot based on plot type
    if plot_type == "continuous":
        ax.plot(x, y)
    elif plot_type == "discrete":
        ax.scatter(x, y)
        ax.stem(x, y)

    # Add labels and title
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)

    canvas.draw()
