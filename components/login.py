from cgitb import text
from logging import PlaceHolder
import tkinter as tk
from tkinter import E, W, Button, Entry, Frame, Label, StringVar, ttk
from traceback import print_tb


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)

        label = Label(
            self,
            text="SignIn",
            font=("arial", 16, "bold"),
        )
        label.grid(row=0, column=0, pady=20)

        cred_frame = Frame(self)
        cred_frame.grid(row=1, column=0)

        # username
        label = Label(cred_frame, text="username", font=("arial", 12, "bold"))
        label.grid(row=0, column=0, pady=20)
        self.username_state = StringVar()
        username_input = Entry(
            cred_frame, textvariable=self.username_state, width=25, font=("arial", 12)
        )
        username_input.grid(row=0, column=1, padx=10, pady=10)

        # password
        label = Label(cred_frame, text="password", font=("arial", 12, "bold"))
        label.grid(row=1, column=0, pady=20)
        self.password_state = StringVar()
        pass_input = Entry(
            cred_frame, textvariable=self.password_state, width=25, font=("arial", 12)
        )
        pass_input.grid(row=1, column=1, padx=10, pady=10)

        # signin button
        button2 = Button(
            self,
            text="SignIn",
            command=self.sign_in,
            width=15,
            background="white",
            font=("arial", 12),
        )
        button2.grid(row=3, column=0, padx=200, pady=10,sticky="e")

        # sign up button
        # button2 = Button(
        #     self,
        #     text="SignUp",
        #     command=lambda: controller.show_frame("SignUpPage"),
        #     width=15,
        #     background="white",
        #     font=("arial", 10),
        # )
        # button2.grid(row=4, column=0, padx=10, pady=10)

    def sign_in(self):
        print("signed in ...")
