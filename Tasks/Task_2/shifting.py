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

shifting_frame = tk.Frame(root)

shifting_label = CustomLabel(shifting_frame, text="Shifting")
shifting_label.pack()

validate_func = shifting_frame.register(validate_num)


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


def get_values():
    try:
        shifter = int(shifting_entry.get())
    except Exception as e:
        tk.messagebox.showerror("Error", f"Shifting Factor must be filled.")
        return

    return shifter


def shifting_signals():
    shifter = get_values()
    if shifter is None:
        return

    data = browse_button_command("Signal", ax, canvas)
    x1 = [point[0] for point in data]
    y1 = [point[1] for point in data]

    result = [x + shifter for x in x1]

    print("Shifting signal by 500")
    SignalSamplesAreEqual("Output\Task_2\output shifting by add 500.txt", 0, y1)

    print("Shifting signal by -500")
    SignalSamplesAreEqual("Output\Task_2\output shifting by minus 500.txt", 0, y1)

    plot_data(
        x=result,
        y=y1,
        plot_type="continuous",
        title=f"Signal shifted by {shifter}",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


entry_frame = tk.Frame(shifting_frame)
entry_frame.pack(padx=10, side=tk.TOP)

shifting_signal_button = CustomButton(
    entry_frame, command=shifting_signals, text="Shift by a number"
)
shifting_signal_button.pack(side=tk.LEFT, padx=250, pady=10)

shifting_entry = LabeledEntry(
    entry_frame, "Shifting Factor", validatecommand=validate_func
)
shifting_entry.pack(side=tk.LEFT, padx=250, pady=10)

signals_generation_representation_frame = tk.Frame(shifting_frame)
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
