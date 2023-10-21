from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Utils.generate_signals import generate_sin_signal, generate_cos_signal
from Utils.plot_graph import plot_data
from Utils.read_signal_file import *
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
import matplotlib.pyplot as plt
import tkinter as tk
import sys

sys.path.append("../")

label_font = ("Times New Roman", 25)
button_font = ("Times New Roman", 18)
entry_font = ("Times New Roman", 15)


def show_read_signal_file_frame():
    # Show the read signal file frame
    read_signal_file_frame.pack()
    # Hide other frames
    generate_signal_frame.pack_forget()


def show_generate_signal_frame():
    # Show the generate signal frame
    generate_signal_frame.pack()
    # Hide other frames
    read_signal_file_frame.pack_forget()


def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_date()
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
generate_button = tk.Button(
    brows_frame,
    text="Read File",
    font=button_font,
    width=20,
    command=browse_button_command,
)
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


def validate_num(P):
    if P == "" or P == "-":
        return True

    try:
        float(P)
        return True
    except ValueError:
        return False


validate_func = generate_signal_frame.register(validate_num)
label = tk.Label(
    generate_signal_frame, text="Signals Generation", font=("Times New Roman", 25)
)
label.pack()
radio_button_frame = tk.Frame(generate_signal_frame)
radio_button_frame.pack()

selected_option = tk.IntVar()

sinusoidal_signal_button = tk.Radiobutton(
    radio_button_frame,
    text="Generate Sinusoidal Signal",
    font=("Times New Roman", 18),
    variable=selected_option,
    value=1,
)
sinusoidal_signal_button.grid(row=0, column=0, padx=15)

cosinusoidal_signal_button = tk.Radiobutton(
    radio_button_frame,
    text="Generate Cosinusoidal Signal",
    font=("Times New Roman", 18),
    variable=selected_option,
    value=2,
)
cosinusoidal_signal_button.grid(row=0, column=1, padx=15)


def get_selected_option():
    selected = selected_option.get()
    print("Selected option:", selected)
    return selected


data_frame = tk.Frame(generate_signal_frame)
data_frame.pack(padx=10, side=tk.TOP)


amplitude_label = tk.Label(data_frame, text="Amplitude", font=("Times New Roman", 18))
amplitude_label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=15)
amplitude_textbox = tk.Entry(
    data_frame,
    font=("Times New Roman", 15),
    width=25,
    validate="key",
    validatecommand=(validate_func, "%P"),
)
amplitude_textbox.grid(row=1, column=0, sticky=tk.W + tk.E, padx=15)


phase_shift_label = tk.Label(
    data_frame, text="Phase Shift", font=("Times New Roman", 18)
)
phase_shift_label.grid(row=0, column=1, sticky=tk.W + tk.E, padx=15)
phase_shift_textbox = tk.Entry(
    data_frame,
    font=("Times New Roman", 15),
    width=25,
    validate="key",
    validatecommand=(validate_func, "%P"),
)
phase_shift_textbox.grid(row=1, column=1, sticky=tk.W + tk.E, padx=15)


analog_frequency_label = tk.Label(
    data_frame, text="Analog Frequency", font=("Times New Roman", 18)
)
analog_frequency_label.grid(row=0, column=2, sticky=tk.W + tk.E, padx=15)
analog_frequency_textbox = tk.Entry(
    data_frame,
    font=("Times New Roman", 15),
    width=25,
    validate="key",
    validatecommand=(validate_func, "%P"),
)
analog_frequency_textbox.grid(row=1, column=2, sticky=tk.W + tk.E, padx=15)


sampling_frequency_label = tk.Label(
    data_frame, text="Sampling Frequency", font=("Times New Roman", 18)
)
sampling_frequency_label.grid(row=0, column=3, sticky=tk.W + tk.E, padx=15)
sampling_frequency_textbox = tk.Entry(
    data_frame,
    font=("Times New Roman", 15),
    width=25,
    validate="key",
    validatecommand=(validate_func, "%P"),
)
sampling_frequency_textbox.grid(row=1, column=3, sticky=tk.W + tk.E, padx=15)


def call_generate_signals():
    generate_signals(ax_generation_continuous, canvas_generation_continuous, "continuous")
    generate_signals(ax_generation_discrete, canvas_generation_discrete, "discrete")


button = tk.Button(
    data_frame,
    text="Generate",
    font=("Times New Roman", 20),
    bg="white",
    fg="black",
    height=1,
    command=call_generate_signals,
)
# button.grid(padx=5, pady=5, sticky=tk.BOTTOM)
button.grid(row=0, column=4, sticky=tk.W + tk.E, pady=15, padx=30)


def get_values():
    try:
        amplitude = int(amplitude_textbox.get())
        phase_shift = float(phase_shift_textbox.get())
        analog_frequency = int(analog_frequency_textbox.get())
        sampling_frequency = int(sampling_frequency_textbox.get())
        print(amplitude, phase_shift, analog_frequency, sampling_frequency)
    except Exception as e:
        tk.messagebox.showerror("Error", f"All values must be filled.")
        return

    return amplitude, phase_shift, analog_frequency, sampling_frequency


# Add signal plot frame
signals_generation_representation_frame = tk.Frame(generate_signal_frame, width=50000)
signals_generation_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)
signals_generation_representation_frame.grid_rowconfigure(0, weight=1)
signals_generation_representation_frame.grid_rowconfigure(1, weight=1)

# Add continuous signal representation frame
continuous_generation_signal_representation_frame = tk.Frame(signals_generation_representation_frame, pady=5)
# continuous_signal_representation_frame.pack(
#     padx=2, pady=5, expand=True, fill=tk.BOTH
# )
continuous_generation_signal_representation_frame.grid(row=0, column=0)

# Add discrete signal representation frame
discrete_generation_signal_representation_frame = tk.Frame(signals_generation_representation_frame, pady=5)
# discrete_signal_representation_frame.pack(
#     padx=2, pady=5, expand=True, fill=tk.BOTH
# )
discrete_generation_signal_representation_frame.grid(row=1, column=0)

# Add empty figure for continuous signal representation
fig, ax_generation_continuous = plt.subplots()
fig.set_size_inches(20, 5)
canvas_generation_continuous = FigureCanvasTkAgg(fig, continuous_generation_signal_representation_frame)
canvas_generation_continuous.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Add empty figure for discrete signal representation
fig, ax_generation_discrete = plt.subplots()
fig.set_size_inches(20, 5)
canvas_generation_discrete = FigureCanvasTkAgg(fig, discrete_generation_signal_representation_frame)
canvas_generation_discrete.get_tk_widget().pack(fill=tk.BOTH, expand=True )


def generate_signals(ax, canvas, plot_type):
    amplitude, phase_shift, analog_frequency, sampling_frequency = get_values()

    if sampling_frequency >= (2 * analog_frequency):
        sin_or_cos = get_selected_option()

        if sin_or_cos == 1:
            sin_signal = generate_sin_signal(
                amplitude,
                sampling_frequency,
                analog_frequency,
                phase_shift,
                plot_type,
                ax=ax,
                canvas=canvas,
            )
            SignalSamplesAreEqual("Output\Sin_Cos\SinOutput.txt", 0, sin_signal)
        elif sin_or_cos == 2:
            cos_signal = generate_cos_signal(
                amplitude,
                sampling_frequency,
                analog_frequency,
                phase_shift,
                plot_type,
                ax=ax,
                canvas=canvas,
            )
            SignalSamplesAreEqual("Output\Sin_Cos\CosOutput.txt", 0, cos_signal)
        else:
            tk.messagebox.showerror("Error", f"Choose the signal type")
            return
    else:
        tk.messagebox.showerror(
            "Error",
            f"Wrong sampling frequency. Should be {2 * analog_frequency} atleast",
        )
        return


root.mainloop()
