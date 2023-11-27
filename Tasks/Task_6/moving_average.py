import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from GUI.labeled_entry import LabeledEntry
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.Utils.entry_validation import validate_num
from Test.Task_6.comparesignals import SignalSamplesAreEqual


import sys

sys.path.append("../")

moving_average_frame = tk.Frame(root)

moving_average_label = CustomLabel(moving_average_frame, text="Moving Average")
moving_average_label.pack()

validate_func = moving_average_frame.register(validate_num)

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


def moving_average():
    x, y = browse_button_command(ax, canvas)
    window_size = int(moving_average_entry.get())

    output_length = len(y) - window_size + 1
    result = [0] * output_length

    for i in range(output_length):
        result[i] = sum(y[i : i + window_size]) / window_size

    x = x[:output_length]

    print("Signal 1")
    SignalSamplesAreEqual("Output\Task_6\OutMovAvgTest1.txt", 0, result)

    print("Signal 2")
    SignalSamplesAreEqual("Output\Task_6\OutMovAvgTest2.txt", 0, result)

    plot_data(
        x=x,
        y=result,
        plot_type="continuous",
        title=f"After Moving Average with window size {window_size}",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


entry_frame = tk.Frame(moving_average_frame)
entry_frame.pack(padx=20, pady=20)

moving_average_button = CustomButton(
    entry_frame, command=moving_average, text="Smooth Signal"
)
moving_average_button.pack(side=tk.LEFT, padx=300)

moving_average_entry = LabeledEntry(
    entry_frame, "Window Size", validatecommand=validate_func
)
moving_average_entry.pack(side=tk.LEFT, padx=10)


signals_generation_representation_frame = tk.Frame(moving_average_frame)
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
