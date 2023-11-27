from root import root
from GUI.Utils.main_frames_manipulation import (
    show_read_signal_file_frame,
    show_addition_frame,
    show_quantization_frame,
    show_dc_frame,
    show_moving_average_frame,
)
import GUI.menu

show_moving_average_frame()

root.mainloop()
