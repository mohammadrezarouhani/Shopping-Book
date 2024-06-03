from email.mime import image
import tkinter as tk
from tkinter import BOTH, E, N, S, W, Button, Frame, PhotoImage, ttk
from components import *

frame_list = [StartPage, LoginPage, SignUpPage, BookListPage, ShoppingCardPage,ReportPage]


class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Book Online Shop")
        self.geometry("650x500")
        self.resizable(0, 0)

        # setting global Treeview style
        style = ttk.Style()
        style.configure("Treeview", rowheight=40)
        style.configure("Button", font=("Arial", 18))

        # Create a container frame
        container = Frame(self)
        container.pack(fill="both", expand=True)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=0)
        container.rowconfigure(1, weight=1)

        # tool bar
        toolbar = Frame(container, height=5)
        toolbar.grid(row=0, column=0, sticky=W + N, padx=2, pady=2)

        initil_page_button = Button(
            toolbar,
            text="Initial Page",
            background="white",
            foreground="green",
            command=lambda: self.show_frame("StartPage"),
        )
        initil_page_button.grid(row=0, column=0, sticky=W)

        search_page_button = Button(
            toolbar,
            text="Search Page",
            background="white",
            foreground="green",
            command=lambda: self.show_frame("BookListPage"),
        )
        search_page_button.grid(row=0, column=1, sticky=W)

        # Dictionary to hold the different frames
        self.frames = {}

        # Initialize and store each frame
        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=1, column=0, sticky=N + W + E + S)

        # Show the initial frame
        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
