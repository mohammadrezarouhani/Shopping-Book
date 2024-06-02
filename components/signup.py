from cgitb import text
from logging import PlaceHolder
import tkinter as tk
from tkinter import E, W, StringVar, ttk
from traceback import print_tb


class SignUp(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        style = ttk.Style()
        style.configure(
            "W.TButton",
            font=("calibri", 10, "bold"),
            foreground="black",
            borderwidth="1",
        )

        label = ttk.Label(
            self,
            text="SignUp",
            font=("arial", 14),
        )
        label.grid(row=0, column=0, padx=10, pady=30)

        # username label
        label = ttk.Label(
            self,
            text="username",
            font=("arial", 12),
        )
        label.grid(row=1, column=0, padx=10, pady=30)

        # username entry
        self.username_state = StringVar()
        username_input = ttk.Entry(
            self,
            textvariable=self.username_state,
            style="W.TButton",
        )

        username_input.grid(row=1, column=1, padx=10, pady=10)

        ### password label
        label = ttk.Label(
            self,
            text="password",
            font=("arial", 12),
        )
        label.grid(row=2, column=0, padx=10, pady=30)

        # password input
        self.password_state = StringVar()
        pass_input = ttk.Entry(
            self,
            textvariable=self.password_state,
            style="W.TButton",
        )
        pass_input.grid(row=2, column=1, padx=10, pady=10)

        # password label
        label = ttk.Label(
            self,
            text="password Retype",
            font=("arial", 12),
        )
        label.grid(row=2, column=2, padx=10, pady=30)

        # password input
        self.password_retype_state = StringVar()
        pass_input = ttk.Entry(
            self,
            textvariable=self.password_retype_state,
            style="W.TButton",
        )
        pass_input.grid(row=2, column=2, padx=10, pady=10)

        # password label
        label = ttk.Label(
            self,
            text="password",
            font=("arial", 14),
        )
        label.grid(row=2, column=0, padx=10, pady=30)

        # password input
        self.password_state = StringVar()
        pass_input = ttk.Entry(
            self,
            textvariable=self.password_state,
            style="W.TButton",
        )
        pass_input.grid(row=2, column=1, padx=10, pady=10)

        # signin button
        button2 = ttk.Button(
            self, text="SignIn", style="W.TButton", command=self.sign_in
        )
        button2.grid(row=3, column=0, padx=10, pady=10)

        # sign up button
        button2 = ttk.Button(
            self,
            text="SignUp",
            style="W.TButton",
            command=lambda: controller.show_frame("SignUp"),
        )
        button2.grid(row=4, column=0, padx=10, pady=10)

    def sign_in(self):
        print("signed in ...")
