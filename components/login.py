import tkinter as tk
from tkinter import Button, Entry, Frame, Label, StringVar
from tkinter import messagebox
from tkinter.ttk import Combobox

from database import *
from .main_frame import MainFrame


class LoginPage(MainFrame):
    def init(self):
        self.columnconfigure(0, weight=1)

        label = Label(
            self,
            text="Sign In",
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
        button2.grid(row=3, column=0, padx=100)

    def sign_in(self):
        username = self.username_state.get()
        password = self.password_state.get()

        old_user: Customer | Admin = self.controller.user

        new_user = get_user(username, password)

        if (
            type(new_user) == Customer
            and old_user
            and old_user.card
            and old_user.card.card_items
        ):
            card_items = old_user.card.card_items

            for item in card_items:
                if card_item := get_card_item(item.product_id, new_user.card.id):
                    update_card_item(
                        item.product_id,
                        new_user.card.id,
                        item.quantity + card_item.quantity,
                    )
                else:
                    create_card_item(new_user.card.id, item.product.id, item.quantity)

            new_user.card = get_card(new_user.id)

        if new_user:
            self.controller.logged_in = True
            self.controller.user = new_user
            prev = self.controller.history[-2]
            self.controller.show_frame(prev)
        else:
            messagebox.showerror('error','no account with this username and password!')