import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from GUI.labeled_entry import LabeledEntry
from GUI.Utils.entry_validation import validate_num
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Test.Task_6.Shift_Fold_Signal import Shift_Fold_Signal

import sys

sys.path.append("../")

delaying_advancing_folding_frame = tk.Frame(root)

delaying_advancing_folding_label = CustomLabel(
    delaying_advancing_folding_frame, text="Delaying or advancing a folded signal"
)
delaying_advancing_folding_label.pack()

validate_func = delaying_advancing_folding_label.register(validate_num)

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


def delaying_advancing_folding():
    x, y = browse_button_command(ax, canvas)
    shifting_step = int(step_entry.get())

    x = [x[i] - shifting_step for i in range(len(x))]

    y = y[::-1]

    print("Fold by 500")
    Shift_Fold_Signal("Output\Task_6\Output_ShifFoldedby500.txt", x, y)

    print("Fold by -500")
    Shift_Fold_Signal("Output\Task_6\Output_ShiftFoldedby-500.txt", x, y)

    plot_data(
        x=x,
        y=y,
        plot_type="continuous",
        title=f"After Delaying or advancing a folded signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


entry_frame = tk.Frame(delaying_advancing_folding_frame)
entry_frame.pack(padx=20, pady=20)

delaying_advancing_folding_button = CustomButton(
    entry_frame,
    command=delaying_advancing_folding,
    text="Delaying or Advancing Folded Signal",
    width=40,
)
delaying_advancing_folding_button.pack(side=tk.LEFT, padx=300)

step_entry = LabeledEntry(entry_frame, "K Step", validatecommand=validate_func)
step_entry.pack(side=tk.LEFT, padx=10)


signals_generation_representation_frame = tk.Frame(delaying_advancing_folding_frame)
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
