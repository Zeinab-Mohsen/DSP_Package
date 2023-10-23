import tkinter as tk


class LabeledEntry(tk.Frame):
    def __init__(
        self,
        master,
        label_text,
        label_font=("Times New Roman", 18),
        entry_font=("Times New Roman", 15),
        entry_width=25,
        validatecommand=None,
        **kwargs
    ):
        super().__init__(master)

        label = tk.Label(self, text=label_text, font=label_font)
        entry = tk.Entry(
            self,
            validatecommand=(validatecommand, "%P"),
            validate="key",
            width=entry_width,
            font=entry_font,
        )

        label.grid(row=0, column=0, sticky=tk.W + tk.E, padx=15)
        entry.grid(row=1, column=0, sticky=tk.W + tk.E, padx=15)

    # To access the values
    def get(self):
        return self.children["!entry"].get()

    def set(self, value):
        self.children["!entry"].delete(0, tk.END)
        self.children["!entry"].insert(0, value)
