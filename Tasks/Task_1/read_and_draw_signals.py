import tkinter as tk
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from root import root
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys

sys.path.append("../")


def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plot_data(
        x=x,
        y=y,
        plot_type="continuous",
        title="Continuous Representation",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_continuous,
        canvas=canvas_continuous,
    )

    plot_data(
        x=x,
        y=y,
        plot_type="discrete",
        title="Discrete Representation",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_discrete,
        canvas=canvas_discrete,
    )

# Create frames
read_signal_file_frame = tk.Frame(root)


# Add Label
label = CustomLabel(read_signal_file_frame, text="Read Signal File")
label.pack(padx=15, pady=15)

# Add brows frame
brows_frame = tk.Frame(read_signal_file_frame)

# Add button read file
generate_button = CustomButton(brows_frame, text="Read File", command=browse_button_command)
generate_button.grid(padx=10, pady=10, row=1, column=1)

brows_frame.pack(padx=15, pady=5)

# Add signal plot frame
signals_representation_frame = tk.Frame(read_signal_file_frame)
signals_representation_frame.pack(padx=15, pady=5)

# Add continuous signal representation frame
continuous_signal_representation_frame = tk.Frame(signals_representation_frame)
continuous_signal_representation_frame.pack(
    padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH
)

# Add discrete signal representation frame
discrete_signal_representation_frame = tk.Frame(signals_representation_frame)
discrete_signal_representation_frame.pack(
    padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH
)

# Add empty figure for continuous signal representation
fig, ax_continuous = plt.subplots()
canvas_continuous = FigureCanvasTkAgg(fig, continuous_signal_representation_frame)
canvas_continuous.get_tk_widget().pack()

# Add empty figure for discrete signal representation
fig, ax_discrete = plt.subplots()
canvas_discrete = FigureCanvasTkAgg(fig, discrete_signal_representation_frame)
canvas_discrete.get_tk_widget().pack()
