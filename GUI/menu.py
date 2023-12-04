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
    show_task4_frame,
    show_dc_frame,
    show_dct_frame,
    show_moving_average_frame,
    show_sharpening_frame,
    show_folding_frame,
    show_delaying_advancing_frame,
    show_delaying_advancing_folding_frame,
    show_remove_dc_frame,
    show_convolution_frame,
    show_correlation_frame,
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

Task_4_menu = tk.Menu(menubar, tearoff=0)
Task_4_menu.add_command(label="DFT&IDFT", command=show_task4_frame, font=item_font)
menubar.add_cascade(label="Task 4", menu=Task_4_menu, font=menu_font)

Task_5_menu = tk.Menu(menubar, tearoff=0)
Task_5_menu.add_command(label="DCT", command=show_dct_frame, font=item_font)
Task_5_menu.add_command(label="Remove DC", command=show_dc_frame, font=item_font)
menubar.add_cascade(label="Task 5", menu=Task_5_menu, font=menu_font)

Task_6_menu = tk.Menu(menubar, tearoff=0)
Task_6_menu.add_command(
    label="Moving Average", command=show_moving_average_frame, font=item_font
)
Task_6_menu.add_command(
    label="Sharpening", command=show_sharpening_frame, font=item_font
)
Task_6_menu.add_command(
    label="Delaying or advancing a signal ",
    command=show_delaying_advancing_frame,
    font=item_font,
)
Task_6_menu.add_command(label="Folding", command=show_folding_frame, font=item_font)
Task_6_menu.add_command(
    label="Delaying or advancing a folded signal",
    command=show_delaying_advancing_folding_frame,
    font=item_font,
)
Task_6_menu.add_command(label="Remove DC", command=show_remove_dc_frame, font=item_font)
menubar.add_cascade(label="Task 6", menu=Task_6_menu, font=menu_font)

Task_7_menu = tk.Menu(menubar, tearoff=0)
Task_7_menu.add_command(label="Convolution", command=show_convolution_frame, font=item_font)
menubar.add_cascade(label="Task 7", menu=Task_7_menu, font=menu_font)

Task_8_menu = tk.Menu(menubar, tearoff=0)
Task_8_menu.add_command(label="Correlation", command=show_correlation_frame, font=item_font)
menubar.add_cascade(label="Task 8", menu=Task_8_menu, font=menu_font)


root.config(menu=menubar)
