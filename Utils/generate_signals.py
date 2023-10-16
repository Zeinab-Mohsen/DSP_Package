from Utils.plot_graph import plot_data
import numpy as np
import sys

sys.path.append("../")


def generate_sin_signal(
    amplitude,
    sampling_frequency,
    analog_frequency,
    phase_shift,
    plot_type,
    ax=None,
    canvas=None,
):
    # Generate the time axis
    if plot_type == "continuous":
        time = np.linspace(0, 1, sampling_frequency)
    elif plot_type == "discrete":
        time = np.arange(0, 1, 1 / sampling_frequency)

    # Generate the sine wave signal
    signal = amplitude * np.sin(2 * np.pi * analog_frequency * time + phase_shift)

    # plot signal
    plot_data(
        x=time,
        y=signal,
        plot_type=plot_type,
        title="Sin Wave Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )

    return signal


def generate_cos_signal(
    amplitude,
    sampling_frequency,
    analog_frequency,
    phase_shift,
    plot_type,
    ax=None,
    canvas=None,
):
    duration = 1.0

    # Generate the time axis
    time = np.arange(0, duration, 1 / sampling_frequency)

    # Generate the sine wave signal
    signal = amplitude * np.cos(2 * np.pi * analog_frequency * time + phase_shift)

    # Plot signal
    plot_data(
        x=time,
        y=signal,
        plot_type=plot_type,
        title="Cos Wave Signal",
        x_label="Time",
        y_label="Amplitude",
        ax=ax,
        canvas=canvas,
    )

    return signal
