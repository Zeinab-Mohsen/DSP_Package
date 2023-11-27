import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Test.Task_6.Shift_Fold_Signal import Shift_Fold_Signal

import sys

sys.path.append("../")

folding_frame = tk.Frame(root)

folding_label = CustomLabel(folding_frame, text="Folding a signal")
folding_label.pack()


def browse_button_command(ax, canvas):
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plot_data(
        x=x,
        y=y,
        plot_type="continuous",
        title="Original Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )
    return x, y


def folding():
    x, y = browse_button_command(ax, canvas)

    y = y[::-1]

    print("Fold")
    Shift_Fold_Signal("Output\Task_6\Output_fold.txt", x, y)

    plot_data(
        x=x,
        y=y,
        plot_type="continuous",
        title=f"After folding",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


folding_button = CustomButton(
    folding_frame,
    command=folding,
    text="Folding a signal",
)
folding_button.pack(side=tk.TOP)


signals_generation_representation_frame = tk.Frame(folding_frame)
signals_generation_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)
signals_generation_representation_frame.grid_rowconfigure(0, weight=1)
signals_generation_representation_frame.grid_rowconfigure(1, weight=1)

# Add signal plot frame
signal_representation_frame = tk.Frame(signals_generation_representation_frame)
signal_representation_frame.grid(row=0, column=0)

# Add empty figure for continuous signal representation
fig, ax = plt.subplots()
fig.set_size_inches(20, 5)
canvas = FigureCanvasTkAgg(fig, signal_representation_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Add signal plot frame
resultant_signal_representation_frame = tk.Frame(
    signals_generation_representation_frame
)
resultant_signal_representation_frame.grid(row=1, column=0)

# Add empty figure for continuous signal representation
fig, ax_resultant = plt.subplots()
fig.set_size_inches(20, 5)
canvas_resultant = FigureCanvasTkAgg(fig, resultant_signal_representation_frame)
canvas_resultant.get_tk_widget().pack(fill=tk.BOTH, expand=True)
