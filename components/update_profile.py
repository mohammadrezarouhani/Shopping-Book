from cgitb import text
from logging import PlaceHolder
from os import name
import tkinter as tk
from tkinter import  Button, Entry, Label, LabelFrame, StringVar, ttk

from .datetime_entry import DateEntry


class UpdateProfile(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        style = ttk.Style()
        style.configure(
            "W.Button",
            font=("calibri", 50, "bold"),
            foreground="black",
            borderwidth="1",
            padding="2",
        )

        # main label
        main_label = Label(self, text="Update Profile", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        credential_frame = LabelFrame(
            self, text="Credentials", font=("Arial", 14, "bold")
        )
        credential_frame.pack(fill="x", expand="yes")
        credential_frame.columnconfigure(0, weight=0)
        credential_frame.columnconfigure(1, weight=1)
        credential_frame.columnconfigure(2, weight=0)
        credential_frame.columnconfigure(3, weight=1)

        # username
        username_label = Label(credential_frame, text="username", width=10)
        username_entry = Entry(
            credential_frame,
        )
        username_label.grid(row=0, column=0)
        username_entry.grid(row=0, column=1, pady=5)

        # password
        pass_label = Label(credential_frame, text="password", width=10)
        pass_entry = Entry(
            credential_frame,
        )
        pass_label.grid(row=1, column=0)
        pass_entry.grid(row=1, column=1, pady=5)

        # password retype
        re_pass_label = Label(credential_frame, text="password retype", width=15)
        re_pass_entry = Entry(
            credential_frame,
        )
        re_pass_label.grid(row=1, column=2)
        re_pass_entry.grid(row=1, column=3, pady=5)

        ## name frame
        name_frame = LabelFrame(self, text="FullName", font=("Arial", 14, "bold"))
        name_frame.pack(expand="yes", fill="x")
        name_frame.columnconfigure(0, weight=0)
        name_frame.columnconfigure(1, weight=1)
        name_frame.columnconfigure(2, weight=0)
        name_frame.columnconfigure(3, weight=1)

        # first name
        firstname_label = Label(name_frame, text="firstname", width=10)
        firstname_entry = Entry(
            name_frame,
        )
        firstname_label.grid(row=0, column=0)
        firstname_entry.grid(row=0, column=1, pady=5)

        # last name
        lastname_label = Label(name_frame, text="lastname", width=10)
        lastname_entry = Entry(
            name_frame,
        )
        lastname_label.grid(row=0, column=2)
        lastname_entry.grid(row=0, column=3, pady=5)

        # address frame
        address_frame = LabelFrame(
            self, text="Addres Detail", font=("Arial", 14, "bold")
        )
        address_frame.pack(fill="x", expand="yes")
        address_frame.columnconfigure(0, weight=0)
        address_frame.columnconfigure(1, weight=1)
        address_frame.columnconfigure(2, weight=0)
        address_frame.columnconfigure(3, weight=1)

        # address
        address_label = Label(address_frame, text="address", width=10)
        address_entry = Entry(
            address_frame,
        )
        address_label.grid(row=0, column=0)
        address_entry.grid(row=0, column=1, pady=5)

        # city
        city_label = Label(address_frame, text="city", width=10)
        city_entry = Entry(
            address_frame,
        )
        city_label.grid(row=0, column=2)
        city_entry.grid(row=0, column=3, pady=5)

        # state
        state_label = Label(address_frame, text="state", width=10)
        state_entry = Entry(
            address_frame,
        )
        state_label.grid(row=1, column=0)
        state_entry.grid(row=1, column=1, pady=5)

        # zip code
        zip_label = Label(address_frame, text="Credit Card", width=10)
        zip_entry = Entry(
            address_frame,
        )
        zip_label.grid(row=1, column=2)
        zip_entry.grid(row=1, column=3, pady=5)

        # credit card frame
        credit_frame = LabelFrame(
            self, text="Credit Card Detail", font=("Arial", 14, "bold")
        )
        credit_frame.pack(fill="x", expand="yes")
        credit_frame.columnconfigure(0, weight=0)
        credit_frame.columnconfigure(1, weight=1)
        credit_frame.columnconfigure(2, weight=0)
        credit_frame.columnconfigure(3, weight=1)

        # credit card type
        type_label = Label(credit_frame, text="Card Type")
        type_var = tk.StringVar()
        type_select = ttk.Combobox(credit_frame, width=15, textvariable=type_var)
        type_label.grid(row=0, column=0)
        type_select.grid(row=0, column=1, pady=5)

        # zip code
        card_num_label = Label(credit_frame, text="Credit Number", width=12)
        card_num_entry = Entry(credit_frame)
        card_num_label.grid(row=0, column=2)
        card_num_entry.grid(row=0, column=3, pady=5)

        datetime_entry = DateEntry(credit_frame)
        datetime_entry.grid(row=0, column=4)

        submit_button = Button(
            self, text="Update", background="white", foreground="green",command=self.update
        )
        submit_button.pack(fill="x", expand="yes", padx=200)


    def update(self):
        pass