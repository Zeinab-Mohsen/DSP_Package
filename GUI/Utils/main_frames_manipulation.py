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

from Tasks.Task_4.DFT_IDFT import task4_frame

from Tasks.Task_5.DC import dc_frame
from Tasks.Task_5.DCT import dct_frame

from Tasks.Task_6.delaying_advancing_folding import delaying_advancing_folding_frame
from Tasks.Task_6.delaying_advancing import delaying_advancing_frame
from Tasks.Task_6.folding import folding_frame
from Tasks.Task_6.moving_average import moving_average_frame
from Tasks.Task_6.remove_dc import remove_dc_frame
from Tasks.Task_6.sharpening import sharpening_frame

from Tasks.Task_7.convolution import convolution_frame

from Tasks.Task_8.correlation import correlation_frame

from Tasks.Task_9.fast_convolution import fast_convolution_frame
from Tasks.Task_9.fast_correlation import fast_correlation_frame

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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_quantization_frame():
    # Show quantization frame
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
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_task4_frame():
    # Show dft frame
    task4_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_dc_frame():
    # Show dc frame
    dc_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_dct_frame():
    # Show dct frame
    dct_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_delaying_advancing_folding_frame():
    # Show delaying_advancing_folding frame
    delaying_advancing_folding_frame.pack()

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

    # Task 3 frames
    quantization_frame.pack_forget()

    # task 4 frames
    task4_frame.pack_forget()

    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()

    # task 6 frames
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_delaying_advancing_frame():
    # Show delaying_advancing frame
    delaying_advancing_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_folding_frame():
    # Show folding frame
    folding_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_moving_average_frame():
    # Show moving_average frame
    moving_average_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_remove_dc_frame():
    # Show remove_dc frame
    remove_dc_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_sharpening_frame():
    # Show sharpening frame
    sharpening_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_convolution_frame():
    # Show convolution frame
    convolution_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_correlation_frame():
    # Show correlation frame
    correlation_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()
    fast_correlation_frame.pack_forget()


def show_fast_correlation_frame():
    # Show fast_correlation frame
    fast_correlation_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_convolution_frame.pack_forget()


def show_fast_convolution_frame():
    # Show fast_convolution frame
    fast_convolution_frame.pack()

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
    # Task 3 frames
    quantization_frame.pack_forget()
    # task 4 frames
    task4_frame.pack_forget()
    # task 5 frames
    dct_frame.pack_forget()
    dc_frame.pack_forget()
    # task 6 frames
    delaying_advancing_folding_frame.pack_forget()
    delaying_advancing_frame.pack_forget()
    folding_frame.pack_forget()
    moving_average_frame.pack_forget()
    remove_dc_frame.pack_forget()
    sharpening_frame.pack_forget()
    # task 7 frames
    convolution_frame.pack_forget()
    # task 8 frames
    correlation_frame.pack_forget()
    # task 9 frames
    fast_correlation_frame.pack_forget()