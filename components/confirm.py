from mimetypes import init
from operator import itemgetter
import tkinter as tk
from tkinter import (
    CENTER,
    E,
    NO,
    RIGHT,
    Y,
    Button,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)

from database import *

from .main_frame import MainFrame


class ConfirmPage(MainFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        # main label
        main_label = Label(self, text="Confirm Order", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        self.top_frame = LabelFrame(
            self, text="Customer Detail", font=("Arial", 12, "bold")
        )
        self.top_frame.pack(fill="x", expand=True)
        self.top_frame.columnconfigure(0, weight=1)
        self.top_frame.columnconfigure(1, weight=1)

    def init(self):
        if self.controller.logged_in:
            self.user: Customer = self.controller.user
            self.card_items: List[CardItem] = self.user.card.card_items
            self.sub_total_price = sum(
                [item.quantity * float(item.product.price) for item in self.card_items]
            )

            self.shipping_price = 4
            self.total_price = self.sub_total_price - self.shipping_price

            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)

            # address detail
            addr_frame = Frame(self.top_frame)
            addr_frame.grid(row=0, column=0)

            name_label = Label(
                addr_frame, text=self.user.firstname + "" + self.user.lastname
            )
            name_label.grid(row=1, column=0)

            address_label = Label(addr_frame, text=self.user.address)
            address_label.grid(row=2, column=0)

            city_label = Label(addr_frame, text=self.user.city)
            city_label.grid(row=3, column=0)

            state_label = Label(addr_frame, text=self.user.state)
            state_label.grid(row=4, column=0)

            zcode_label = Label(addr_frame, text="<<zip_code>>")
            zcode_label.grid(row=4, column=1)

            # address detail
            card_frame = Frame(self.top_frame)
            card_frame.grid(row=0, column=1)

            cname_label = Label(card_frame, text="credit card:")
            cname_label.grid(row=0, column=0)

            address_label = Label(card_frame, text="23423423423423")
            address_label.grid(row=0, column=1)

            # creating a tree view
            tree_frame = Frame(self)
            tree_frame.pack(pady=10, fill="both", expand="yes")

            # adding scroll bar to tree view
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # creating tree view
            self.book_tree = ttk.Treeview(
                tree_frame,
                yscrollcommand=tree_scroll.set,
                selectmode="extended",
                show="headings",
                height=5,
            )
            self.book_tree.pack(fill="both", expand=True)

            # configure scrollbar
            tree_scroll.config(command=self.book_tree.yview)

            # set three headers
            self.book_tree["columns"] = (
                "ISBN",
                "Title",
                "Publisher",
                "Price",
                "Quantity"
            )

            # set tree columns
            self.book_tree.column("#0", width=0, stretch=NO)
            self.book_tree.column("ISBN", anchor=CENTER, width=100)
            self.book_tree.column("Title", anchor=CENTER, width=130)
            self.book_tree.column("Publisher", anchor=CENTER, width=130)
            self.book_tree.column("Price", anchor=CENTER, width=100)
            self.book_tree.column("Quantity", anchor=CENTER, width=100)

            # set hedings
            self.book_tree.heading("ISBN", text="ISBN", anchor=CENTER)
            self.book_tree.heading("Title", text="Title", anchor=CENTER)
            self.book_tree.heading("Publisher", text="Publisher", anchor=CENTER)
            self.book_tree.heading("Price", text="Price", anchor=CENTER)
            self.book_tree.heading("Quantity", text="Quantity", anchor=CENTER)

            # set tree tags
            self.book_tree.tag_configure("odd", background="white")
            self.book_tree.tag_configure("even", background="lightblue")

            # insert inital data
            self.insert_book_item()

            # Search Frame
            card_frame = LabelFrame(self, text="Order Detail", font=("Arial", 12, "bold"))
            card_frame.pack(fill="x", expand="yes")
            card_frame.grid_columnconfigure(1, weight=1)

            # create card label
            self.card_label = Label(
                card_frame,
                text="the book will be delivered within 5 days",
                foreground="red",
                font=("Arial", 10, "bold"),
                background="lightblue",
            )
            self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

            # final price
            price_frame = Frame(card_frame, background="white")
            price_frame.grid(row=0, column=1, sticky="wnes")
            ##
            stotal_label = Label(price_frame, text="Sub Total Price:", background="white")
            stotal_label.grid(row=0, column=0)
            ##
            ship_label = Label(price_frame, text="Shipping Price:", background="white")
            ship_label.grid(row=1, column=0)
            ##
            total_label = Label(price_frame, text="Total Price:", background="white")
            total_label.grid(row=2, column=0)
            ##

            # price values
            stotal_label = Label(price_frame, text=self.sub_total_price, background="white")
            stotal_label.grid(row=0, column=1)
            ##
            ship_label = Label(price_frame, text=self.shipping_price, background="white")
            ship_label.grid(row=1, column=1)
            ##
            total_label = Label(price_frame, text=self.total_price, background="white")
            total_label.grid(row=2, column=1)
            ##

            # check Card
            update_button = Button(
                card_frame,
                text="Update Profile",
                background="white",
                command=lambda: self.controller.show_frame("UpdateProfile"),
            )
            update_button.grid(row=0, column=2, sticky=E, padx=6)

            # check Card
            checkout_button = Button(
                card_frame,
                text="Buy",
                background="white",
                command=lambda: self.controller.show_frame("FactorPage"),
            )
            checkout_button.grid(row=0, column=3, sticky=E, padx=6)

    def insert_book_item(self):

        for index, item in enumerate(self.card_items):
            if index % 2 == 0:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=item.id,
                    text="",
                    values=(
                        item.product.isbn,
                        item.product.title,
                        item.product.publisher,
                        item.product.price,
                        item.product.quantity,
                    ),
                    tags="odd",
                )

            else:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=item.id,
                    text="",
                    values=(
                        item.product.isbn,
                        item.product.title,
                        item.product.publisher,
                        item.product.price,
                        item.product.quantity,
                    ),
                    tags="even",
                )

    def search(self, *args):
        """query to data base for filtering"""
        print(f"Text changed to: {self.text_var.get()}")

    def add_to_card(self):
        for item in self.book_tree.selection():
            item_text = self.book_tree.item(item, "values")
            print(item_text)

    def remove_from_tree(self):
        for record in self.book_tree.get_children():
            self.book_tree.delete(record)
