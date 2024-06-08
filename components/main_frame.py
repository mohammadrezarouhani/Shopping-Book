import tkinter as tk
from abc import abstractmethod


class MainFrame(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

    def update_data(self):
        self.init()

    def clean(self):
        for widget in self.winfo_children():
            widget.destroy()

        print("frame cleaned")

    @abstractmethod
    def init(self):
        pass
