import tkinter as tk
from tkinter import ttk
from components import *

frame_list = [StartPage]


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create a container frame
        container = ttk.Frame(self)
        container.grid(row=0, column=0, sticky="nsew")

        # Configure grid layout to expand
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=1)

        # Dictionary to hold the different frames
        self.frames = {}

        # Initialize and store each frame
        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the initial frame
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
