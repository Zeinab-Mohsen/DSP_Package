from Tasks.Task_1.read_and_draw_signals import read_signal_file_frame
from Tasks.Task_1.generate_signals import generate_signal_frame

from Tasks.Task_2.accumulation import accumulation_frame
from Tasks.Task_2.addition import addition_frame
from Tasks.Task_2.multiplication import multiplication_frame
from Tasks.Task_2.normalization import normalization_frame
from Tasks.Task_2.shifting import shifting_frame
from Tasks.Task_2.squaring import squaring_frame
from Tasks.Task_2.subtraction import subtraction_frame

from Tasks.Task_3.quantization import quantization_frame

import sys

sys.path.append("../")

def show_read_signal_file_frame():
    # Show the read signal file frame
    read_signal_file_frame.pack()

    # Hide other frames
    # Task 1 frames
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()


def show_generate_signal_frame():
    # Show the generate signal frame
    generate_signal_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_accumulation_frame():
    # Show the accumulation frame
    accumulation_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()
    
    # Task 3 frames
    quantization_frame.pack_forget()

def show_addition_frame():
    # Show the addition frame
    addition_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_multiplication_frame():
    # Show the multiplication frame
    multiplication_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_normalization_frame():
    # Show the normalization frame
    normalization_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_shifting_frame():
    # Show the shifting frame
    shifting_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_squaring_frame():
    # Show the squaring frame
    squaring_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    subtraction_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()

def show_subtraction_frame():
    # Show the subtraction frame
    subtraction_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()

    # Task 3 frames
    quantization_frame.pack_forget()
    
def show_quantization_frame():
    # Show the read signal file frame
    quantization_frame.pack()

    # Hide other frames
    # Task 1 frames
    read_signal_file_frame.pack_forget()
    generate_signal_frame.pack_forget()
    # Task 2 frames
    accumulation_frame.pack_forget()
    addition_frame.pack_forget()
    multiplication_frame.pack_forget()
    normalization_frame.pack_forget()
    shifting_frame.pack_forget()
    squaring_frame.pack_forget()
    subtraction_frame.pack_forget()