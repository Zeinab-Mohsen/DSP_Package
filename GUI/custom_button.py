import tkinter as tk


class CustomButton(tk.Button):
    def __init__(
        self,
        master,
        text,
        font=("Times New Roman", 18),
        command=None,
        width=20,
        **kwargs
    ):
        super().__init__(
            master, text=text, font=font, command=command, width=width, **kwargs
        )
