import numpy as np
import tkinter as tk
from root import root
import matplotlib.pyplot as plt
from Utils.plot_graph import plot_data
from GUI.custom_label import CustomLabel
from GUI.custom_button import CustomButton
from Test.Task_8.CompareSignal import Compare_Signals
from Utils.read_signal_file import seperate_file_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

sys.path.append("../")

correlation_frame = tk.Frame(root)

correlation_label = CustomLabel(correlation_frame, text=" Normalized Cross-Correlation Of Two Signals")
correlation_label.pack()


def browse_button_command(title, ax, canvas):
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plot_data(
        x=x,
        y=y,
        plot_type="continuous",
        title=title,
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )
    return x, y


def correlation():
    indices1, values1 = browse_button_command("First Signal", ax_signal1, canvas_signal1)
    indices2, values2 = browse_button_command("First Signa2", ax_signal2, canvas_signal2)\
    
    # correlation logic

    CompareSignals("Output\Task_8\CorrOutput.txt", indices, values)

    plot_data(
        x=indices,
        y=values,
        plot_type="continuous",
        title="Correlation",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


correlation_button = CustomButton(
    correlation_frame, command=correlation, text="Convolve Two Signals"
)
correlation_button.pack(side=tk.TOP, padx=250, pady=10)

# Add signal plot frame
signals_representation_frame = tk.Frame(correlation_frame)
signals_representation_frame.pack(padx=15, pady=5)

# Add continuous signal representation frame
signal1_frame = tk.Frame(signals_representation_frame)
signal1_frame.pack(padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# Add discrete signal representation frame
signal2_frame = tk.Frame(signals_representation_frame)
signal2_frame.pack(padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_signal1 = plt.subplots()
canvas_signal1 = FigureCanvasTkAgg(fig, signal1_frame)
canvas_signal1.get_tk_widget().pack()

# Add empty figure for discrete signal representation
fig, ax_signal2 = plt.subplots()
canvas_signal2 = FigureCanvasTkAgg(fig, signal2_frame)
canvas_signal2.get_tk_widget().pack()


# Add signal plot frame
resultant_signal_representation_frame = tk.Frame(correlation_frame)
resultant_signal_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_resultant = plt.subplots()
fig.set_size_inches(20, 5)
canvas_resultant = FigureCanvasTkAgg(fig, resultant_signal_representation_frame)
canvas_resultant.get_tk_widget().pack(fill=tk.BOTH, expand=True)