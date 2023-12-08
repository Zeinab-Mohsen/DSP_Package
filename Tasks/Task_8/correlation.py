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

correlation_label = CustomLabel(
    correlation_frame, text=" Normalized Cross-Correlation Of Two Signals"
)
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
    return x, y, is_periodic

def correlation():
    indices1, input_signal1, is_periodic = browse_button_command(
        "First Signal", ax_signal1, canvas_signal1
    )
    indices2, input_signal2, is_periodic = browse_button_command(
        "Second Signal", ax_signal2, canvas_signal2
    )
    
    # Cross-Correlation
    normalized_correlation = []
    
    sum_signal1 = np.sum(np.square(input_signal1))
    sum_signal2 = np.sum(np.square(input_signal2))
    input_signal2_samples = np.copy(input_signal2)
    print(input_signal2)
    print(input_signal2_samples)
    total = sum_signal1 * sum_signal2
    normalized_value = np.sqrt(total) / len(input_signal1)
    
    # Iterate over each element of the first signal
    for _ in range(len(input_signal1)):
        # Calculate the cross-correlation result
        result = np.sum(input_signal1 * input_signal2_samples)
        
        # Calculate the final result (divide by the length of the signal)
        final_result = result / len(input_signal1)
        
        # Calculate the normalized result (divide by the normalized value)
        normalized_result = final_result / normalized_value
        
        normalized_correlation.append(normalized_result)

        # Update the second signal samples for the next iteration
        if is_periodic:
            temp = input_signal2_samples[0]
            input_signal2_samples[:-1] = input_signal2_samples[1:]
            input_signal2_samples[-1] = temp
        else:
            input_signal2_samples[:-1] = input_signal2_samples[1:]
            input_signal2_samples[-1] = 0

    Compare_Signals("Output\Task_8\CorrOutput.txt", indices1, normalized_correlation)

    plot_data(
        x=indices1,
        y=normalized_correlation,
        plot_type="continuous",
        title="Correlation",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )



correlation_button = CustomButton(
    correlation_frame, command=correlation, text="Correlate Two Signals"
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
