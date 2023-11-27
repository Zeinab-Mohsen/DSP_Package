import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Test.Task_6.DerivativeSignal import DerivativeSignal


import sys

sys.path.append("../")

sharpening_frame = tk.Frame(root)

sharpening_label = CustomLabel(sharpening_frame, text="Sharpening")
sharpening_label.pack()


def sharpening():
    # x, y = browse_button_command()
    InputSignal = [
        1.0,
        2.0,
        3.0,
        4.0,
        5.0,
        6.0,
        7.0,
        8.0,
        9.0,
        10.0,
        11.0,
        12.0,
        13.0,
        14.0,
        15.0,
        16.0,
        17.0,
        18.0,
        19.0,
        20.0,
        21.0,
        22.0,
        23.0,
        24.0,
        25.0,
        26.0,
        27.0,
        28.0,
        29.0,
        30.0,
        31.0,
        32.0,
        33.0,
        34.0,
        35.0,
        36.0,
        37.0,
        38.0,
        39.0,
        40.0,
        41.0,
        42.0,
        43.0,
        44.0,
        45.0,
        46.0,
        47.0,
        48.0,
        49.0,
        50.0,
        51.0,
        52.0,
        53.0,
        54.0,
        55.0,
        56.0,
        57.0,
        58.0,
        59.0,
        60.0,
        61.0,
        62.0,
        63.0,
        64.0,
        65.0,
        66.0,
        67.0,
        68.0,
        69.0,
        70.0,
        71.0,
        72.0,
        73.0,
        74.0,
        75.0,
        76.0,
        77.0,
        78.0,
        79.0,
        80.0,
        81.0,
        82.0,
        83.0,
        84.0,
        85.0,
        86.0,
        87.0,
        88.0,
        89.0,
        90.0,
        91.0,
        92.0,
        93.0,
        94.0,
        95.0,
        96.0,
        97.0,
        98.0,
        99.0,
        100.0,
    ]

    first_derivative = []
    for i in range(1, len(InputSignal)):
        first_derivative.append(InputSignal[i] - InputSignal[i - 1])

    second_derivative = []
    for i in range(1, len(InputSignal) - 1):
        second_derivative.append(
            InputSignal[i + 1] - (2 * InputSignal[i]) + InputSignal[i - 1]
        )

    x = InputSignal[: len(InputSignal) - 1]
    plot_data(
        x=x,
        y=first_derivative,
        plot_type="continuous",
        title="First Derivative",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )

    x = InputSignal[: len(InputSignal) - 2]
    plot_data(
        x=x,
        y=second_derivative,
        plot_type="continuous",
        title=f"Second Derivative",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )

    second_derivative.append(0)
    DerivativeSignal(first_derivative, second_derivative)


sharpening_button = CustomButton(
    sharpening_frame, command=sharpening, text="Sharpening"
)
sharpening_button.pack(padx=20)


signals_generation_representation_frame = tk.Frame(sharpening_frame)
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
