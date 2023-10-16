from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Utils.generate_signals import generate_sin_signal, generate_cos_signal
from Utils.plot_graph import plot_data
from Utils.read_signal_file import *
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
import matplotlib.pyplot as plt
import tkinter as tk
import sys
sys.path.append('../')

lable_font = "Times New Roman", 25
button_font = "Times New Roman", 18
entry_font = "Times New Roman", 15


def brows_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_date()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plot_data(x=x, y=y, plot_type="continuous", title="Continuous Representation",
              x_label="Time", y_label="Amplitude", ax=ax_continuous, canvas=canvas_continuous)

    plot_data(x=x, y=y, plot_type="discrete", title="Discrete Representation",
              x_label="Time", y_label="Amplitude", ax=ax_discrete, canvas=canvas_discrete)


# create root window
root = tk.Tk()
root.title("DSP Package")

# add Lable
label = tk.Label(root, text="Read Signal File", font=lable_font)
label.pack(padx=15, pady=15)

# add brows frame
brows_frame = tk.Frame(root)

# # location lable
# location_label = tk.Label(brows_frame, text="File location:", font=button_font)
# location_label.grid(padx=10, pady=10, row=0, column=0)

# # add location entry
# location_entry = tk.Entry(brows_frame, font=entry_font, width=50).grid(
#     padx=10, pady=10, row=0, column=1)

# # add brows button
# brows_button = tk.Button(brows_frame, text="Brows", font=(
#     "Times New Roman", 12)).grid(padx=10, pady=10, row=0, column=2)

# add button read file
generate_button = tk.Button(brows_frame, text="Read File", font=button_font,
                            width=20, command=brows_button_command).grid(padx=10, pady=10, row=1, column=1)

brows_frame.pack(padx=15, pady=5)

# add signal plot frame
signals_representation_frame = tk.Frame(root)
signals_representation_frame.pack(padx=15, pady=5)

# add continous signal representation frame
continous_signal_representation_frame = tk.Frame(signals_representation_frame)
continous_signal_representation_frame.pack(
    padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# add discrete signal representation frame
discrete_signal_representation_frame = tk.Frame(signals_representation_frame)
discrete_signal_representation_frame.pack(
    padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# add empty figure for continous signal representation
fig, ax_continuous = plt.subplots()
canvas_continuous = FigureCanvasTkAgg(
    fig, continous_signal_representation_frame)
canvas_continuous.get_tk_widget().pack()

# add empty figure for discrete signal representation
fig, ax_discrete = plt.subplots()
canvas_discrete = FigureCanvasTkAgg(fig, discrete_signal_representation_frame)
canvas_discrete.get_tk_widget().pack()


root.mainloop()
