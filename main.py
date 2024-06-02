import tkinter as tk
from tkinter import BOTH, E, N, S, W, ttk
from components import *

frame_list = [StartPage, LoginPage, SignUp]


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Book Online Shop")
        self.geometry("600x400")

        # Create a container frame
        container = ttk.Frame(self)
        container.place(relx=0.5, rely=0.5, anchor="center")

        # Dictionary to hold the different frames
        self.frames = {}

        # Initialize and store each frame
        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky=(N, W, E, S))

        # Show the initial frame
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
