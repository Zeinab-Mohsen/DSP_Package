import tkinter as tk
from root import root
from GUI.custom_button import CustomButton
from GUI.custom_label import CustomLabel
from Utils.plot_graph import plot_data
from Utils.read_signal_file import seperate_file_data
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.labeled_entry import LabeledEntry
from GUI.Utils.entry_validation import validate_num
from Test.Task_4.signalcompare import SignalComapreAmplitude, SignalComaprePhaseShift
from tkinter import filedialog
import numpy as np


import sys

sys.path.append("../")

task4_frame = tk.Frame(root)


DFT_label = CustomLabel(task4_frame, text="DFT")
DFT_label.pack()

validate_func = task4_frame.register(validate_num)


def browse_button_command():
    data, signal_type, is_periodic, n_samples = seperate_file_data()
    # Extract x and y values from data
    x = [point[0] for point in data]
    y = [point[1] for point in data]

    print(data)

    return x, y


def get_values():
    frequency = frequncy_entry.get()
    amplitude = amplitude_entry.get()
    phase = phase_entry.get()

    return frequency, amplitude, phase


def calculate_magnitude(X_k):
    magnitude = np.sqrt(X_k.real**2 + X_k.imag**2)
    return magnitude


def calculate_phase(X_k):
    phases = np.arctan2(np.imag(X_k), np.real(X_k))
    return phases


def save_file(X, omit_phase=False):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            for k, X_k in enumerate(X):
                magnitude = calculate_magnitude(X_k)
                if omit_phase:
                    file.write(f"X({k}) = {magnitude:.4f}\n")
                else:
                    phase = calculate_phase(X_k)
                    file.write(f"X({k}) = {magnitude:.4f},{phase:.4f} degrees\n")


def plot_frequency_domain(signal, sampling_frequency):
    N = len(signal)
    frequencies = np.arange(N) * sampling_frequency / N
    X = dft(signal)

    amplitudes = [calculate_magnitude(X_k) for X_k in X]
    phases = [calculate_phase(X_k) for X_k in X]

    for k, X_k in enumerate(X):
        magnitude = calculate_magnitude(X_k)
        phase = calculate_phase(X_k)

        print(f"X({k}) = {X_k}")
        print(f"Magnitude (A) = {magnitude}")
        print(f"Phase (Phi) = {phase} degrees")

    plot_data(
        x=frequencies,
        y=amplitudes,
        plot_type="discrete",
        title="Frequency vs. Amplitude",
        x_label="Frequency",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )
    plot_data(
        x=frequencies,
        y=phases,
        plot_type="discrete",
        title="Frequency vs. Phase",
        x_label="Frequency",
        y_label="Phase",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


def dft(signal):
    length = len(signal)
    res = np.zeros(length, dtype=complex)
    for k in range(length):
        res[k] = 0
        for n in range(length):
            res[k] += signal[n] * np.exp(-2j * np.pi * k * n / length)
    return res


def call_dft():
    # x, y = browse_button_command()
    frequncy, amplitude, phase = get_values()

    file = filedialog.askopenfile(mode="r")
    filepath = file.name
    with open(file.name, "r") as file:
        lines = file.readlines()
        signal = [
            float(line.strip().split()[1])
            for line in lines[3:]
            if len(line.strip().split()) == 2
        ]

    frequency = float(frequncy)

    if amplitude and phase:
        amplitude = float(amplitude)
        phase_degrees = float(phase)
        phase_radians = np.radians(phase_degrees)  # Convert degrees to radians

        signal_component = amplitude * np.exp(1j * phase_radians)
        frequency_component_index = 0
        signal[frequency_component_index] = signal_component.real

    res = dft(signal)
    save_file(res)
    plot_frequency_domain(signal, frequency)


def idft(X):
    N = len(X)
    signal = np.zeros(N, dtype=complex)

    for n in range(N):
        signal[n] = 0
        for k in range(N):
            angle = 2 * np.pi * n * k / N
            real_part = np.cos(angle)
            imaginary_part = np.sin(angle)
            signal[n] += (X[k].real * real_part) - (X[k].imag * imaginary_part)

        signal[n] /= N

    return np.asarray(signal, float)


def plot_time_domain(signal):
    N = len(signal)
    time = np.arange(N)

    plot_data(
        x=time,
        y=signal,
        plot_type="continuous",
        title="Time Domain Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )
    plot_data(
        x=time,
        y=signal,
        plot_type="continuous",
        title="Time Domain Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax_resultant,
        canvas=canvas_resultant,
    )


def display_results(results):
    if results:
        x_n = "{" + ", ".join([f"{result:.4f}" for result in results]) + "}"
        print(f"x(n) = {x_n}")


def save_file2(X, omit_phase=False):
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt", filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as file:
            for k, X_k in enumerate(X):
                magnitude = calculate_magnitude(X_k)
                if omit_phase:
                    file.write(f"X({k}) = {magnitude:.4f}\n")
                else:
                    phase = calculate_phase(X_k)
                    file.write(f"X({k}) = {magnitude:.4f}")


def call_idft():
    # x, y = browse_button_command()
    file = filedialog.askopenfile(mode="r")
    filepath = file.name

    X = []
    with open(file.name, "r") as file:
        lines = file.readlines()
        for line in lines[3:]:
            values = line.strip().replace(",", " ").split()
            if len(values) == 2:
                amplitude_str = values[0].replace("f", "")
                phase_str = values[1].replace("f", "")
                amplitude = float(amplitude_str)
                phase = float(phase_str)
                complex_value = amplitude * (np.cos(phase) + 1j * np.sin(phase))
                print(complex_value)
                X.append(complex_value)

    frequncy, amplitude, phase = get_values()

    # X = []
    # for i in range(len(x)):
    #     print(x[i])

    #     complex_value = x[i] * (np.cos(y) + 1j * np.sin(y[i]))
    #     print(complex_value)
    #     X.append(complex_value)

    if amplitude and phase:
        amplitude = float(amplitude)
        phase_degrees = float(phase)
        phase_radians = np.radians(phase_degrees)

        modified_component = amplitude * np.exp(1j * phase_radians)
        frequency_component_index = 0
        X[frequency_component_index] = modified_component

    signal = idft(X)
    plot_time_domain(signal)
    res = signal.tolist()

    display_results(res)

    save_file2(res)


entry_frame = tk.Frame(task4_frame)
entry_frame.pack(padx=10, side=tk.TOP)

dft_button = CustomButton(entry_frame, command=call_dft, text="DFT")
dft_button.pack(side=tk.LEFT, padx=50, pady=10)

dft_button = CustomButton(entry_frame, command=call_idft, text="IDFT")
dft_button.pack(side=tk.LEFT, padx=50, pady=10)

frequncy_entry = LabeledEntry(entry_frame, "Frequency", validatecommand=validate_func)
frequncy_entry.pack(side=tk.LEFT, padx=50, pady=10)

amplitude_entry = LabeledEntry(entry_frame, "Amptliude", validatecommand=validate_func)
amplitude_entry.pack(side=tk.LEFT, padx=50, pady=10)

phase_entry = LabeledEntry(entry_frame, "Phase Shift", validatecommand=validate_func)
phase_entry.pack(side=tk.LEFT, padx=50, pady=10)

signals_generation_representation_frame = tk.Frame(task4_frame)
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
