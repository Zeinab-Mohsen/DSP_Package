import numpy as np
import tkinter as tk
from root import root
import matplotlib.pyplot as plt
from Utils.plot_graph import plot_data
from GUI.custom_label import CustomLabel
from GUI.custom_button import CustomButton
from Test.Task_9.CompareSignal import Compare_Signals
from Utils.read_signal_file import seperate_file_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Tasks.Task_4.DFT_IDFT import dft, idft
import sys

sys.path.append("../")

fast_correlation_frame = tk.Frame(root)

fast_correlation_label = CustomLabel(fast_correlation_frame, text="Fast Correlation")
fast_correlation_label.pack()


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


def fast_correlation():
    input_indices1, input_samples1 = browse_button_command(
        "First Signal", ax_signal1, canvas_signal1
    )
    input_indices2, input_samples2 = browse_button_command(
        "Second Signal", ax_signal2, canvas_signal2
    )

    if len(input_samples1) != len(input_samples2):
        output_length = len(input_samples1) + len(input_samples2) - 1

        input_samples1 = np.pad(
            input_samples1, (0, output_length - len(input_samples1)), mode="constant"
        )
        input_samples2 = np.pad(
            input_samples2, (0, output_length - len(input_samples2)), mode="constant"
        )

    result_samples = []

    input_samples1 = dft(input_samples1)
    input_samples2 = dft(input_samples2)

    input_samples1 = np.conjugate(input_samples1)

    for i in range(len(input_samples1)):
        result_samples.append(input_samples1[i] * input_samples2[i])

    result_samples = idft(result_samples)

    if sorted(input_samples1) != sorted(input_samples2):
        for i in range(len(result_samples)):
            result_samples[i] = result_samples[i] / len(result_samples)

    Compare_Signals("Output\Task_9\Corr_Output.txt", input_indices1, result_samples)

    plot_data(
        x=input_indices1,
        y=result_samples,
        plot_type="continuous",
        title="Correlation",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


fast_correlation_button = CustomButton(
    fast_correlation_frame, command=fast_correlation, text="Fast Correlate Two Signals"
)
fast_correlation_button.pack(side=tk.TOP, padx=250, pady=10)

# Add signal plot frame
signals_representation_frame = tk.Frame(fast_correlation_frame)
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
resultant_signal_representation_frame = tk.Frame(fast_correlation_frame)
resultant_signal_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_resultant = plt.subplots()
fig.set_size_inches(20, 5)
canvas_resultant = FigureCanvasTkAgg(fig, resultant_signal_representation_frame)
canvas_resultant.get_tk_widget().pack(fill=tk.BOTH, expand=True)
