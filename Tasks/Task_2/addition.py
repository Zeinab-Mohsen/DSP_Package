import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
import sys

sys.path.append("../")

addition_frame = tk.Frame(root)

addition_label = CustomLabel(addition_frame, text="Addition")
addition_label.pack()


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
    return data


def add_signals():
    data = browse_button_command("First Signal", ax_signal1, canvas_signal1)
    x1 = [point[0] for point in data]
    y1 = [point[1] for point in data]

    data = browse_button_command("Second Signal", ax_signal2, canvas_signal2)
    x2 = [point[0] for point in data]
    y2 = [point[1] for point in data]

    max_len = max(len(y1), len(y2))

    # Pad the shorter list with zeros to match the length of the longer list
    y1 = y1 + [0] * (max_len - len(y1))
    y2 = y2 + [0] * (max_len - len(y2))

    # Add the two lists together element-wise
    result = [x + y for x, y in zip(y1, y2)]

    print("Addition of signal 1 + signal 2")
    SignalSamplesAreEqual("Output\Task_2\Signal1+signal2.txt\n", 0, result)

    print("Addition of signal 1 + signal 3")
    SignalSamplesAreEqual("Output\Task_2\signal1+signal3.txt\n", 0, result)


    plot_data(
        x=x1,
        y=result,
        plot_type="continuous",
        title="Signal 1 + Signal 2",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


add_signals_button = CustomButton(
    addition_frame, command=add_signals, text="Add two signals"
)
add_signals_button.pack(side=tk.TOP, padx=250, pady=10)

# Add signal plot frame
signals_representation_frame = tk.Frame(addition_frame)
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
resultant_signal_representation_frame = tk.Frame(addition_frame)
resultant_signal_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_resultant = plt.subplots()
fig.set_size_inches(20, 5)
canvas_resultant = FigureCanvasTkAgg(fig, resultant_signal_representation_frame)
canvas_resultant.get_tk_widget().pack(fill=tk.BOTH, expand=True)
