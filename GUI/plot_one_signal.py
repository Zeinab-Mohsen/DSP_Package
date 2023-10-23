import tkinter as tk
import matplotlib.pyplot as plt

class PlotOneSignal(tk.Frame):
    def __init__(
        self,
        parent,
        **kwargs
    ):
        super().__init__(parent)
        self.pack(padx=30, pady=2)

    plot = tk.Frame(master=self.master)
    plot.pack(
        padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH
    )

    fig, ax_continuous = plt.subplots()
    canvas_continuous = FigureCanvasTkAgg(fig, continuous_signal_representation_frame)
    canvas_continuous.get_tk_widget().pack()


# # Add signal plot frame
# signals_representation_frame = tk.Frame(read_signal_file_frame)
# signals_representation_frame.pack(padx=15, pady=5)

# Add continuous signal representation frame


# # Add discrete signal representation frame
# discrete_signal_representation_frame = tk.Frame(signals_representation_frame)
# discrete_signal_representation_frame.pack(
#     padx=30, pady=2, side=tk.LEFT, expand=True, fill=tk.BOTH
# )

# Add empty figure for continuous signal representation


# # Add empty figure for discrete signal representation
# fig, ax_discrete = plt.subplots()
# canvas_discrete = FigureCanvasTkAgg(fig, discrete_signal_representation_frame)
# canvas_discrete.get_tk_widget().pack()
