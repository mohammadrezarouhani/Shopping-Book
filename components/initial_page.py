import tkinter as tk
from tkinter import ttk
from .main_frame import MainFrame
from database.models import Admin, Customer


class StartPage(MainFrame):
    def init(self):
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

        print(self.controller.user)
        if not self.controller.logged_in:
            # create continue as guest
            guest_button = tk.Button(
                self,
                text="Continue AS Guest",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("BookListPage"),
                width=25,
                background="white",
            )
            guest_button.grid(row=1, column=0, padx=10, pady=10)

            # create sign in button
            sign_in_button = tk.Button(
                self,
                text="SignIn",
                command=lambda: self.controller.show_frame("LoginPage"),
                font=("calibri", 12, "bold"),
                borderwidth=4,
                width=25,
                background="white",
            )
            sign_in_button.grid(row=2, column=0, padx=10, pady=10)

            # create signup button
            sign_up_button = tk.Button(
                self,
                text="SignUp",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("SignUpPage"),
                width=25,
                background="white",
            )
            sign_up_button.grid(row=3, column=0, padx=10, pady=10)
        elif isinstance(self.controller.user, Admin):
            # mange book
            manage_book_button = tk.Button(
                self,
                text="Manage Book Store",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("ManageBookPage"),
                width=25,
                background="white",
            )
            manage_book_button.grid(row=0, column=0, padx=10, pady=10)

            # manage orders
            manage_order_button = tk.Button(
                self,
                text="Manage Book Orders",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("BookOrderPage"),
                width=25,
                background="white",
            )
            manage_order_button.grid(row=1, column=0, padx=10, pady=10)

            # reports
            report_button = tk.Button(
                self,
                text="Report",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("ReportPage"),
                width=25,
                background="white",
            )
            report_button.grid(row=2, column=0, padx=10, pady=10)

            # system maintanance
            system_button = tk.Button(
                self,
                text="System Maintanace",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("SystemPage"),
                width=25,
                background="white",
            )
            system_button.grid(row=3, column=0, padx=10, pady=10)
        elif isinstance(self.controller.user, Customer):
            # create continue as guest
            shop_button = tk.Button(
                self,
                text="Order New Book",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("BookListPage"),
                width=25,
                background="white",
            )
            shop_button.grid(row=1, column=0, padx=10, pady=10)

            # create sign in button
            profile_button = tk.Button(
                self,
                text="Profile",
                command=lambda: self.controller.show_frame("UpdateProfile"),
                font=("calibri", 12, "bold"),
                borderwidth=4,
                width=25,
                background="white",
            )
            profile_button.grid(row=2, column=0, padx=10, pady=10)

            # create signup button
            sign_up_button = tk.Button(
                self,
                text="Goto Card",
                font=("calibri", 12, "bold"),
                borderwidth=4,
                command=lambda: self.controller.show_frame("ShoppingCardPage"),
                width=25,
                background="white",
            )
            sign_up_button.grid(row=3, column=0, padx=10, pady=10)
