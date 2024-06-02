

import tkinter as tk
from tkinter import ttk


class StartPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        style = ttk.Style()
        style.configure(
            "W.TButton", font=("calibri", 10, "bold"), foreground="black", borderwidth = '1'
        )

        label = ttk.Label(self, text="Welcome to Shopping Store", font=("arial", 14))
        label.grid(row=0, column=0, padx=10, pady=30)

        button1 = ttk.Button(self, text="Continue AS Guest", style="W.TButton")
        button1.grid(row=1, column=0, padx=10, pady=10)

        button2 = ttk.Button(
            self,
            text="SignIn",
            command=lambda: controller.show_frame("LoginPage"),
            style="W.TButton",
        )
        button2.grid(row=2, column=0, padx=10, pady=10)

        button2 = ttk.Button(self, text="SignUp",style="W.TButton")
        button2.grid(row=3, column=0, padx=10, pady=10)

