import tkinter as tk
from root import root
from GUI.Utils.main_frames_manipulation import (
    show_read_signal_file_frame,
    show_generate_signal_frame,
    show_accumulation_frame,
    show_addition_frame,
    show_multiplication_frame,
    show_normalization_frame,
    show_shifting_frame,
    show_squaring_frame,
    show_subtraction_frame,
    show_quantization_frame,
)


menu_font = ("Times New Roman", 20)
item_font = ("Times New Roman", 15)

# Add menubar
menubar = tk.Menu(root)

Task_1_menu = tk.Menu(menubar, tearoff=0)
Task_1_menu.add_command(
    label="Read Signal File", command=show_read_signal_file_frame, font=item_font
)
Task_1_menu.add_command(
    label="Generate Signal", command=show_generate_signal_frame, font=item_font
)
menubar.add_cascade(label="Task 1", menu=Task_1_menu, font=menu_font)


Task_2_menu = tk.Menu(menubar, tearoff=0)
Task_2_menu.add_command(
    label="Accumulation", command=show_accumulation_frame, font=item_font
)
Task_2_menu.add_command(label="Addition", command=show_addition_frame, font=item_font)
Task_2_menu.add_command(
    label="Multiplication", command=show_multiplication_frame, font=item_font
)
Task_2_menu.add_command(
    label="Normalization", command=show_normalization_frame, font=item_font
)
Task_2_menu.add_command(label="Shifting", command=show_shifting_frame, font=item_font)
Task_2_menu.add_command(label="Squaring", command=show_squaring_frame, font=item_font)
Task_2_menu.add_command(
    label="Subtraction", command=show_subtraction_frame, font=item_font
)
menubar.add_cascade(label="Task 2", menu=Task_2_menu, font=menu_font)

Task_3_menu = tk.Menu(menubar, tearoff=0)
Task_3_menu.add_command(
    label="Quantizatng Sginal", command=show_quantization_frame, font=item_font
)
menubar.add_cascade(label="Task 3", menu=Task_3_menu, font=menu_font)


root.config(menu=menubar)
