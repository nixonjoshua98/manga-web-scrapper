import tkinter as tk

from tkinter import ttk


class Dropdown(ttk.Combobox):

    def __init__(self, master, values, command):
        super().__init__(master=master, state="readonly")
        
        self["values"] = values

        if len(values) == 0:
            raise Exception("Dropdown values cannot be of length 0")

        self.current(0)  # Current value index

        self.command = command
        self.prev_val = self["values"][0]

        self.bind("<<ComboboxSelected>>", self.on_selected)

    def on_selected(self, event=None):
        # Stops the callback from being called if the value is the same previously
        if self.get() != self.prev_val:
            self.prev_val = self.get()
            self.command()

    # Returns the index of the current value
    def get_index(self):
        return self["values"].index(self.get())