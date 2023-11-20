import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.labeled_entry import LabeledEntry
from GUI.Utils.entry_validation import validate_num
from Test.Task_4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift
from tkinter import filedialog
import numpy as np
from Test.Task_5.comparesignal2 import SignalSamplesAreEqual

import sys

sys.path.append("../")

dct_frame = tk.Frame(root)

dct_label = CustomLabel(dct_frame, text="DCT")
dct_label.pack()

validate_func = dct_frame.register(validate_num)


def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    return x, y


def dct():
    x, y = browse_button_command()

    N = len(y)
    result = []

    for k in range(N):
        sum = 0
        for n in range(N):
            sum += y[n] * np.cos((np.pi / (4 * N)) * ((2 * n) - 1) * ((2 * k) - 1))

        result.append(np.sqrt(2 / N) * sum)

    print("DCT Component")
    SignalSamplesAreEqual("Output\Task_5\DCT_output.txt", result)

    m_coefficients = dct_entry.get()
    if m_coefficients:
        m_coefficients = int(m_coefficients)
        y_result = result[:m_coefficients]
        x_result = x[:m_coefficients]
        file_result = list(zip(x_result, y_result))
        np.savetxt("output.txt", file_result)
        print(file_result)

    plot_data(
        x=x,
        y=result,
        plot_type="continuous",
        title=f"DCT",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )


entry_frame = tk.Frame(dct_frame)
entry_frame.pack(padx=10, side=tk.TOP)

dct_button = CustomButton(entry_frame, command=dct, text="Compute DCT")
dct_button.pack(padx=250, side=tk.LEFT)

dct_entry = LabeledEntry(entry_frame, "m coefficients ", validatecommand=validate_func)
dct_entry.pack(side=tk.LEFT, pady=40)


# Add signal plot frame
signal_representation_frame = tk.Frame(dct_frame)
signal_representation_frame.pack()

# Add empty figure for continuous signal representation
fig, ax = plt.subplots()
fig.set_size_inches(20, 5)
canvas = FigureCanvasTkAgg(fig, signal_representation_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
