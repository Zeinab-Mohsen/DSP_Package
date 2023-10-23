import tkinter as tk


class CustomLabel(tk.Label):
    def __init__(self, master, text, font=("Times New Roman", 25), **kwargs):
        super().__init__(master, text=text, font=font, **kwargs)
