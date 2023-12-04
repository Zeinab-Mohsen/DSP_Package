import tkinter as tk
from root import root
import matplotlib.pyplot as plt
from Utils.plot_graph import plot_data
from GUI.custom_label import CustomLabel
from Test.Task_7.ConvTest import ConvTest
from GUI.custom_button import CustomButton
from Utils.read_signal_file import seperate_file_data
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

sys.path.append("../")

convolution_frame = tk.Frame(root)

convolution_label = CustomLabel(convolution_frame, text="Convolve Two Signals")
convolution_label.pack()


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


def convolution():
    input_indices1 , input_samples1 = browse_button_command("First Signal", ax_signal1, canvas_signal1)
    input_indices2 , input_samples2 = browse_button_command("Second Signal", ax_signal2, canvas_signal2)
    # Initialize result arrays with zeros
    result_indices = []
    result_samples = [0] * (len(input_samples1) + len(input_samples2) - 1)

    # Iterate through each element in the first signal
    for i in range(len(input_samples1)):
        # Multiply and accumulate the product into the result array
        for j in range(len(input_samples2)):
            result_samples[i + j] += input_samples1[i] * input_samples2[j]

    # Generate the result indices
    min_index = int( min(input_indices1[0] + input_indices2[0], input_indices1[-1] + input_indices2[-1]))
    max_index = int(max(input_indices1[0] + input_indices2[0], input_indices1[-1] + input_indices2[-1]))
    result_indices = range(min_index, max_index + 1)

    ConvTest(result_indices, result_samples)

    plot_data(
        x=result_indices,
        y=result_samples,
        plot_type="continuous",
        title="Convolution",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


convolution_button = CustomButton(
    convolution_frame, command=convolution, text="Convolve Two Signals"
)
convolution_button.pack(side=tk.TOP, padx=250, pady=10)

# Add signal plot frame
signals_representation_frame = tk.Frame(convolution_frame)
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
resultant_signal_representation_frame = tk.Frame(convolution_frame)
resultant_signal_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_resultant = plt.subplots()
fig.set_size_inches(20, 5)
canvas_resultant = FigureCanvasTkAgg(fig, resultant_signal_representation_frame)
canvas_resultant.get_tk_widget().pack(fill=tk.BOTH, expand=True)
