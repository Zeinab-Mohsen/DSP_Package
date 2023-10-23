import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Utils.generate_signals import generate_sin_signal, generate_cos_signal
from Test.Sin_Cos.comparesignals import SignalSamplesAreEqual
import matplotlib.pyplot as plt
from GUI.labeled_entry import LabeledEntry
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from GUI.Utils.entry_validation import validate_num
from root import root


generate_signal_frame = tk.Frame(root)

validate_func = generate_signal_frame.register(validate_num)
label = CustomLabel(generate_signal_frame, text="Generate Signal")
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

amplitude = LabeledEntry(data_frame, "Amplitude", validatecommand=validate_func)
amplitude.grid(row=0, column=0, sticky=tk.W + tk.E, padx=15)

phase_shift = LabeledEntry(data_frame, "Phase Shift", validatecommand=validate_func)
phase_shift.grid(row=0, column=1, sticky=tk.W + tk.E, padx=15)

analog_frequency = LabeledEntry(
    data_frame, "Analog Frequency", validatecommand=validate_func
)
analog_frequency.grid(row=0, column=2, sticky=tk.W + tk.E, padx=15)

sampling_frequency = LabeledEntry(
    data_frame, "Sampling Frequency", validatecommand=validate_func
)
sampling_frequency.grid(row=0, column=3, sticky=tk.W + tk.E, padx=15)

def call_generate_signals():
    generate_signals(
        ax_generation_continuous, canvas_generation_continuous, "continuous"
    )
    generate_signals(ax_generation_discrete, canvas_generation_discrete, "discrete")


button = CustomButton(data_frame, text="Generate", command=call_generate_signals)
button.grid(row=0, column=4, sticky=tk.W + tk.E, pady=15, padx=30)


def get_values():
    try:
        amplitude_value = int(amplitude.get())
        phase_shift_value = float(phase_shift.get())
        analog_frequency_value = int(analog_frequency.get())
        sampling_frequency_value = int(sampling_frequency.get())
        print(
            amplitude_value,
            phase_shift_value,
            analog_frequency_value,
            sampling_frequency_value,
        )
    except Exception as e:
        tk.messagebox.showerror("Error", f"All values must be filled.")
        return

    return (
        amplitude_value,
        phase_shift_value,
        analog_frequency_value,
        sampling_frequency_value,
    )


# Add signal plot frame
signals_generation_representation_frame = tk.Frame(generate_signal_frame)
signals_generation_representation_frame.pack(padx=2, pady=10, expand=True, fill=tk.BOTH)
signals_generation_representation_frame.grid_rowconfigure(0, weight=1)
signals_generation_representation_frame.grid_rowconfigure(1, weight=1)

# Add continuous signal representation frame
continuous_generation_signal_representation_frame = tk.Frame(
    signals_generation_representation_frame, pady=5
)
continuous_generation_signal_representation_frame.grid(row=0, column=0)

# Add discrete signal representation frame
discrete_generation_signal_representation_frame = tk.Frame(
    signals_generation_representation_frame, pady=5
)
discrete_generation_signal_representation_frame.grid(row=1, column=0)

# Add empty figure for continuous signal representation
fig, ax_generation_continuous = plt.subplots()
fig.set_size_inches(20, 5)
canvas_generation_continuous = FigureCanvasTkAgg(
    fig, continuous_generation_signal_representation_frame
)
canvas_generation_continuous.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Add empty figure for discrete signal representation
fig, ax_generation_discrete = plt.subplots()
fig.set_size_inches(20, 5)
canvas_generation_discrete = FigureCanvasTkAgg(
    fig, discrete_generation_signal_representation_frame
)
canvas_generation_discrete.get_tk_widget().pack(fill=tk.BOTH, expand=True)


def generate_signals(ax, canvas, plot_type):
    (
        amplitude_value,
        phase_shift_value,
        analog_frequency_value,
        sampling_frequency_value,
    ) = get_values()

    if sampling_frequency_value >= (2 * analog_frequency_value):
        sin_or_cos = get_selected_option()

        if sin_or_cos == 1:
            sin_signal = generate_sin_signal(
                amplitude_value,
                sampling_frequency_value,
                analog_frequency_value,
                phase_shift_value,
                plot_type,
                ax=ax,
                canvas=canvas,
            )
            SignalSamplesAreEqual("Output\Sin_Cos\SinOutput.txt", 0, sin_signal)
        elif sin_or_cos == 2:
            cos_signal = generate_cos_signal(
                amplitude_value,
                sampling_frequency_value,
                analog_frequency_value,
                phase_shift_value,
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
