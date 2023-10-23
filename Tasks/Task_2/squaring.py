import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
from GUI.labeled_entry import LabeledEntry
from GUI.Utils.entry_validation import validate_num
import sys

sys.path.append("../")

squaring_frame = tk.Frame(root)

squaring_label = CustomLabel(squaring_frame, text="Squring")
squaring_label.pack()


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


def square_signals():
    data = browse_button_command("Signal", ax, canvas)
    x1 = [point[0] for point in data]
    y1 = [point[1] for point in data]

    result = [x**2 for x in y1]

    print("Squaring signal 1")
    SignalSamplesAreEqual("Output\Task_2\Output squaring signal 1.txt", 0, result)

    plot_data(
        x=x1,
        y=result,
        plot_type="continuous",
        title="Signal squared",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


squaring_signal_button = CustomButton(
    squaring_frame, command=square_signals, text="Square Signal"
)
squaring_signal_button.pack(side=tk.TOP, padx=250, pady=10)


signals_generation_representation_frame = tk.Frame(squaring_frame)
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
