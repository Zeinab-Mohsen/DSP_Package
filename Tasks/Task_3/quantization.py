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
        print(bits_or_levels)
    except Exception as e:
        tk.messagebox.showerror("Error", f"The number of bits_or_levels must be filled.")
        return

    return bits_or_levels


def get_selected_option():
    selected = selected_option.get()
    print("Selected option:", selected)
    return selected


def quantization_signals():
    bits_or_levels = get_values()

    selected_option = get_selected_option()

    # data = browse_button_command()
    # x1 = [point[0] for point in data]
    # y1 = [point[1] for point in data]

    y1 = [-1.22, 1.5, 3.24, 3.94, 2.20, -1.10, -2.26, -1.88, -1.2]

    min_val = min(y1)
    max_val = max(y1)

    levels = 0
    # Bits
    if selected_option == 1:
        levels = 2 ** bits_or_levels
    # Levels
    elif selected_option == 2:
        levels = bits_or_levels
    
    delta = (max_val - min_val) / levels

    intervals_midpoints = [] 
    start = min_val + (delta / 2)
    for i in range(levels):
        intervals_midpoints.append(start)
        start += delta
    
    print(intervals_midpoints)


 
    # # result = quantization.quantize(y1, bits_or_levels)

    # # print("Normalizing signal 1")
    # # SignalSamplesAreEqual("Output\Task_2\\normalize of signal 1 -- output.txt", 0, result)

    # # print("Normalizing signal 2")
    # # SignalSamplesAreEqual("Output\Task_2\\normlize signal 2 -- output.txt", 0, result)

    # plot_data(
    #     x=result,
    #     y=y1,
    #     plot_type="discrete",
    #     title="Quantized Signal",
    #     x_label="Time",
    #     y_label="Amplitude",
    #     ax=ax,
    #     canvas=canvas,
    # )


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