import tkinter as tk
from tkinter import messagebox
from tkinter import (
    CENTER,
    NO,
    RIGHT,
    Y,
    Button,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)

from database.models import Admin
from database import *

from .main_frame import MainFrame


class BookOrderPage(MainFrame):
    def init(self):

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Manage Book Order", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # Search Frame
        search_frame = LabelFrame(self, text="Input", font=("Arial", 12, "bold"))
        search_frame.pack(fill="x", expand="yes")

        search_frame.columnconfigure(0, weight=0)
        search_frame.columnconfigure(1, weight=0)
        search_frame.columnconfigure(2, weight=1)

        # search label
        search_label = Label(search_frame, text="search by customer name")
        search_label.grid(row=0, column=0, padx=5, pady=10)

        #  a entry label and biding text change event
        self.text_var = tk.StringVar()
        search_entry = Entry(
            search_frame, textvariable=self.text_var, width=15, font=("Arial", 10)
        )
        search_entry.grid(row=0, column=1, padx=5, pady=10)

        #  add button
        search_button = Button(
            search_frame,
            text="Search",
            background="white",
            width=15,
            command=self.search,
        )
        search_button.grid(row=0, column=2, padx=5, pady=10, sticky="e")

        # creating a tree view
        tree_frame = Frame(self)
        tree_frame.pack(pady=10, fill="both", expand="yes")

        # adding scroll bar to tree view
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # creating tree view
        self.order_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode="extended",
            show="headings",
            height=7,
        )
        self.order_tree.pack(fill="both", expand=True)

        # configure scrollbar
        tree_scroll.config(command=self.order_tree.yview)

        # set three headers
        self.order_tree["columns"] = (
            "Customer",
            "Credit Card",
            "Total Price",
            "Submit",
        )

        # set tree columns
        self.order_tree.column("#0", width=0, stretch=NO)
        self.order_tree.column("Customer", anchor=CENTER, width=100)
        self.order_tree.column("Credit Card", anchor=CENTER, width=130)
        self.order_tree.column("Total Price", anchor=CENTER, width=130)
        self.order_tree.column("Submit", anchor=CENTER, width=100)

        # set hedings
        self.order_tree.heading("Customer", text="Customer", anchor=CENTER)
        self.order_tree.heading("Credit Card", text="Credit Card", anchor=CENTER)
        self.order_tree.heading("Total Price", text="Total Price", anchor=CENTER)
        self.order_tree.heading("Submit", text="Submit", anchor=CENTER)

        # set tree tags
        self.order_tree.tag_configure("odd", background="white")
        self.order_tree.tag_configure("even", background="lightblue")

        # Order Frame
        card_frame = Frame(self)
        card_frame.pack(fill="x", expand="yes", padx=10)

        submit_button = Button(
            card_frame,
            text="Submit",
            command=self.submit_order,
            foreground="green",
            background="white",
        )
        submit_button.pack(expand=True, fill="x", padx=100)

        self.user: Admin = self.controller.user
        self.orders = get_all_orders()
        self.insert_book_item()

    def insert_book_item(self):
        for index, orders in enumerate(self.orders):
            if index % 2 == 0:
                self.order_tree.insert(
                    parent="",
                    index="end",
                    iid=orders.id,
                    text="",
                    values=(
                        orders.customer.username,
                        orders.credit_card,
                        orders.amount,
                        bool(orders.submitted == 1),
                    ),
                    tags="odd",
                )

            else:
                self.order_tree.insert(
                    parent="",
                    index="end",
                    iid=orders.id,
                    text="",
                    values=(
                        orders.customer.username,
                        orders.credit_card,
                        orders.amount,
                        bool(orders.submitted == 1),
                    ),
                    tags="even",
                )

    def search(self, *args):
        self.clean_table()
        self.orders = get_order_by_customer_username(self.text_var.get())
        self.insert_book_item()

    def clean_table(self):
        for item in self.order_tree.get_children():
            self.order_tree.delete(item)

    def submit_order(self):
        if (
            messagebox.askquestion(
                "submit", "are you sure about submitting selected products"
            )
            == "yes"
        ):
            for item in self.order_tree.selection():
                res = update_order(int(item), 1, self.user.user_id)
                if not res:
                    break
            else:
                messagebox.showinfo("success", "submitting was success!")
                self.clean_table()
                self.orders = get_all_orders()
                self.insert_book_item()
                return

            messagebox.showerror("error", "problem submitting orders")
