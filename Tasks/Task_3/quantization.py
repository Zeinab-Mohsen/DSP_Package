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
import numpy as np
from Utils.round_numbers import round_with_exponent
from Test.Task_3.QuanTest1 import QuantizationTest1
from Test.Task_3.QuanTest2 import QuantizationTest2

import sys

sys.path.append("../")

quantization_frame = tk.Frame(root)

quantization_label = CustomLabel(quantization_frame, text="Quantization Signals")
quantization_label.pack()

validate_func = quantization_frame.register(validate_num)

def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    return data


def get_values():
    try:
        bits_or_levels = int(levels_or_bits_entry.get())
    except Exception as e:
        tk.messagebox.showerror("Error", f"The number of bits_or_levels must be filled.")
        return

    return bits_or_levels


def get_selected_option():
    selected = selected_option.get()
    return selected



def quantization_signals():
    bits_or_levels = get_values()

    selected_option = get_selected_option()

    data = browse_button_command()
    x = [point[0] for point in data]
    y = [point[1] for point in data]


    min_val = min(y)
    max_val = max(y)

    levels = 0
    bits = 0
    # Bits
    if selected_option == 1:
        bits = bits_or_levels
        levels = 2 ** bits_or_levels
    # Levels
    elif selected_option == 2:
        bits = int(np.log2(bits_or_levels))
        levels = bits_or_levels

    
    delta = (max_val - min_val) / levels

    intervals = [] 
    midpoints = []
    for i in range(levels):
        interval = []
        start = min_val + (delta * i)
        interval.append(round_with_exponent(start, 3))

        end = min_val + (delta * (i + 1)) 
        interval.append(round_with_exponent(end, 3))

        intervals.append(interval)

        mid_point = (start + end) / 2
        midpoints.append(round_with_exponent(mid_point, 3))
    
    result_quantization = []
    result_interval = []
    result_encoded = []
    result_quantization_error = []
    quantization_error = 0 
    for i in range(len(y)):
        for j in range(len(intervals)):
            if y[i] >= intervals[j][0] and y[i] <= intervals[j][1]:
                result_quantization.append(midpoints[j])
                result_interval.append(j + 1)
                result_encoded.append(format(j, f'0{bits}b'))
                result_quantization_error.append(midpoints[j] - y[i])
                quantization_error += (midpoints[j] - y[i]) ** 2
                break


    quantization_error /= len(y)

    print("Test 1")
    QuantizationTest1("Output/Task_3/Quan1_Out.txt",result_encoded,result_quantization)   
   
    print("Test 2")
    QuantizationTest2("Output/Task_3/Quan2_Out.txt",result_interval,result_encoded,result_quantization,result_quantization_error)

    plot_data(
        x=result_quantization,
        y=result_interval,
        plot_type="continuous",
        title="Quantized Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )


radio_button_frame = tk.Frame(quantization_frame)
radio_button_frame.pack(side=tk.TOP, pady=25)

selected_option = tk.IntVar()

bits_button = tk.Radiobutton(
    radio_button_frame,
    text="Bits",
    font=("Times New Roman", 18),
    variable=selected_option,
    value=1,
)
bits_button.grid(row=0, column=0, padx=40)

levels_button = tk.Radiobutton(
    radio_button_frame,
    text="Levels",
    font=("Times New Roman", 18),
    variable=selected_option,
    value=2,
)
levels_button.grid(row=0, column=1, padx=40)

levels_or_bits_entry = LabeledEntry(
    radio_button_frame, "Number of levels/Bits", validatecommand=validate_func
)
levels_or_bits_entry.grid(row=0, column=2, padx=40)


quantiz_button = CustomButton(
    radio_button_frame, command=quantization_signals, text="Quantize"
)
quantiz_button.grid(row=0, column=3, padx=40)


# Add empty figure for continuous signal representation
fig, ax = plt.subplots()
fig.set_size_inches(20, 5)
canvas = FigureCanvasTkAgg(fig, quantization_frame)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)   
