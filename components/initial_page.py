import tkinter as tk
from tkinter import ttk


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,background='lightblue')
        self.controller = controller
        self.columnconfigure(0, weight=1)

        # create button style
        style = ttk.Style()
        style.configure(
            "W.TButton",
            font=("calibri", 10, "bold"),
            foreground="black",
            borderwidth="1",
        )

        label = ttk.Label(
            self, text="Welcome to Shopping Store", font=("calibri", 16, "bold")
        )
        label.grid(row=0, column=0, padx=10, pady=30)

        # create continue as guest
        guest_button = tk.Button(
            self,
            text="Continue AS Guest",
            font=("calibri", 12, "bold"),
            borderwidth=4,
            command=lambda: controller.show_frame("BookListPage"),
            width=25,
            background="white"
        )
        guest_button.grid(row=1, column=0, padx=10, pady=10)

        # create sign in button
        sign_in_button = tk.Button(
            self,
            text="SignIn",
            command=lambda: controller.show_frame("LoginPage"),
            font=("calibri", 12, "bold"),
            borderwidth=4,
            width=25,
            background="white"
        )
        sign_in_button.grid(row=2, column=0, padx=10, pady=10)

        # create signup button
        sign_up_button = tk.Button(
            self,
            text="SignUp",
            font=("calibri", 12, "bold"),
            borderwidth=4,
            command=lambda: controller.show_frame("SignUpPage"),
            width=25,
            background="white"
        )
        sign_up_button.grid(row=3, column=0, padx=10, pady=10)
