from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Utils.generate_signals import generate_sin_signal, generate_cos_signal
from Utils.plot_graph import plot_data
from Utils.read_signal_file import *
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
import matplotlib.pyplot as plt
import tkinter as tk
import sys
sys.path.append('../')

label_font = ("Times New Roman", 25)
button_font = ("Times New Roman", 18)
entry_font = ("Times New Roman", 15)

def show_read_signal_file_frame():
    # Hide other frames
    generate_signal_frame.pack_forget()
    # Show the read signal file frame
    read_signal_file_frame.pack()

def show_generate_signal_frame():
    # Hide other frames
    read_signal_file_frame.pack_forget()
    # Show the generate signal frame
    generate_signal_frame.pack()

def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_date()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plot_data(x=x, y=y, plot_type="continuous", title="Continuous Representation",
              x_label="Time", y_label="Amplitude", ax=ax_continuous, canvas=canvas_continuous)

    plot_data(x=x, y=y, plot_type="discrete", title="Discrete Representation",
              x_label="Time", y_label="Amplitude", ax=ax_discrete, canvas=canvas_discrete)

# Create root window
root = tk.Tk()
root.title("DSP Package")
root.geometry("1400x800")

# Add menubar
menubar = tk.Menu(root)
Task_1_menu = tk.Menu(menubar, tearoff=0)
Task_1_menu.add_command(label="Read Signal File", command=show_read_signal_file_frame)
Task_1_menu.add_command(label="Generate Signal", command=show_generate_signal_frame)
menubar.add_cascade(label="Task 1", menu=Task_1_menu)
root.config(menu=menubar)

# Create frames
read_signal_file_frame = tk.Frame(root)
generate_signal_frame = tk.Frame(root)

# Initialize frames
show_read_signal_file_frame()

# Add Label
label = tk.Label(read_signal_file_frame, text="Read Signal File", font=label_font)
label.pack(padx=15, pady=15)

# Add brows frame
brows_frame = tk.Frame(read_signal_file_frame)

# Add button read file
generate_button = tk.Button(brows_frame, text="Read File", font=button_font, width=20, command=browse_button_command)
generate_button.grid(padx=10, pady=10, row=1, column=1)

brows_frame.pack(padx=15, pady=5)

# Add signal plot frame
signals_representation_frame = tk.Frame(read_signal_file_frame)
signals_representation_frame.pack(padx=15, pady=5)

# Add continuous signal representation frame
continuous_signal_representation_frame = tk.Frame(signals_representation_frame)
continuous_signal_representation_frame.pack(padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# Add discrete signal representation frame
discrete_signal_representation_frame = tk.Frame(signals_representation_frame)
discrete_signal_representation_frame.pack(padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH)

# Add empty figure for continuous signal representation
fig, ax_continuous = plt.subplots()
canvas_continuous = FigureCanvasTkAgg(fig, continuous_signal_representation_frame)
canvas_continuous.get_tk_widget().pack()

# Add empty figure for discrete signal representation
fig, ax_discrete = plt.subplots()
canvas_discrete = FigureCanvasTkAgg(fig, discrete_signal_representation_frame)
canvas_discrete.get_tk_widget().pack()

root.mainloop()