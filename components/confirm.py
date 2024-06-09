from datetime import datetime, timedelta, timezone
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
from tkinter import messagebox

from database import *

from .main_frame import MainFrame


class ConfirmPage(MainFrame):
    def init(self):
        if self.controller.logged_in:
            # main label
            main_label = Label(self, text="Confirm Order", font=("Arial", 16, "bold"))
            main_label.pack(fill="x", expand=True)

            self.top_frame = LabelFrame(
                self, text="Customer Detail", font=("Arial", 10, "bold")
            )
            self.top_frame.pack(fill="x", expand=True)
            self.top_frame.columnconfigure(0, weight=1)
            self.top_frame.columnconfigure(1, weight=1)
            self.user: Customer = self.controller.user
            self.card_items: List[CardItem] = self.user.card.card_items
            self.sub_total_price = sum(
                [item.quantity * float(item.product.price) for item in self.card_items]
            )

            self.shipping_price = 4
            self.total_price = self.sub_total_price + self.shipping_price

            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=0)
            self.columnconfigure(1, weight=1)

            # address frame
            addr_frame = LabelFrame(self.top_frame, text="Address Detail")
            addr_frame.grid(row=0, column=0, padx=5, pady=2, sticky="wnes")

            ## fullname
            name_info_label = Label(addr_frame, text="Name:", font=("Arial", 10))
            name_info_label.grid(row=1, column=0, pady=2, sticky="wn")
            name_label = Label(
                addr_frame,
                text=self.user.firstname + " " + self.user.lastname,
                font=("Arial", 12, "bold"),
            )
            name_label.grid(row=1, column=1, pady=2, sticky="wn")

            ## address
            address_info_label = Label(addr_frame, text="Adrress:", font=("Arial", 10))
            address_info_label.grid(row=2, column=0, pady=2, sticky="wn")
            address_label = Label(addr_frame, text=self.user.address)
            address_label.grid(row=2, column=1, pady=2, sticky="wn")

            ## city
            city_info_label = Label(addr_frame, text="City:", font=("Arial", 10))
            city_info_label.grid(row=3, column=0, pady=2, sticky="wn")
            city_label = Label(addr_frame, text=self.user.city)
            city_label.grid(row=3, column=1, pady=2, sticky="wn")

            ## state
            state_info_label = Label(addr_frame, text="State:", font=("Arial", 10))
            state_info_label.grid(row=3, column=0, pady=2, sticky="wn")
            state_label = Label(addr_frame, text=self.user.state)
            state_label.grid(row=4, column=1, pady=2, sticky="wn")

            # credit frame
            card_frame = LabelFrame(self.top_frame, text="Credit Detail")
            card_frame.grid(row=0, column=1, padx=5, pady=2, sticky="wnes")

            ## credit type
            cname_info_label = Label(
                card_frame, text="Credit Type:", font=("Arial", 10)
            )
            cname_info_label.grid(row=0, column=0, pady=2, sticky="wn")
            cname_label = Label(card_frame, text=self.user.credit_type)
            cname_label.grid(row=0, column=1, sticky="w")

            ## credit number
            cname_num_info_label = Label(
                card_frame, text="Credit Number:", font=("Arial", 10)
            )
            cname_num_info_label.grid(row=1, column=0, pady=2, sticky="wn")
            cname_num_label = Label(card_frame, text=self.user.credit_card)
            cname_num_label.grid(row=1, column=1, pady=2, sticky="wn")

            ## credit expire date
            credit_expire_date_info_label = Label(
                card_frame, text="Expire Date:", font=("Arial", 10)
            )
            credit_expire_date_info_label.grid(row=2, column=0, pady=2, sticky="wn")
            credit_expire_date_label = Label(
                card_frame, text=self.user.credit_expire_date
            )
            credit_expire_date_label.grid(row=2, column=1, pady=2, sticky="wn")

            # creating a tree view
            tree_frame = Frame(self)
            tree_frame.pack(pady=10, fill="both", expand="yes")

            ## adding scroll bar to tree view
            tree_scroll = Scrollbar(tree_frame)
            tree_scroll.pack(side=RIGHT, fill=Y)

            ## creating tree view
            self.book_tree = ttk.Treeview(
                tree_frame,
                yscrollcommand=tree_scroll.set,
                selectmode="extended",
                show="headings",
                height=5,
            )
            self.book_tree.pack(fill="both", expand=True)

            ## configure scrollbar
            tree_scroll.config(command=self.book_tree.yview)

            ## set three headers
            self.book_tree["columns"] = (
                "ISBN",
                "Title",
                "Publisher",
                "Price",
                "Quantity",
            )

            ## set tree columns
            self.book_tree.column("#0", width=0, stretch=NO)
            self.book_tree.column("ISBN", anchor=CENTER, width=100)
            self.book_tree.column("Title", anchor=CENTER, width=130)
            self.book_tree.column("Publisher", anchor=CENTER, width=130)
            self.book_tree.column("Price", anchor=CENTER, width=100)
            self.book_tree.column("Quantity", anchor=CENTER, width=100)

            ## set hedings
            self.book_tree.heading("ISBN", text="ISBN", anchor=CENTER)
            self.book_tree.heading("Title", text="Title", anchor=CENTER)
            self.book_tree.heading("Publisher", text="Publisher", anchor=CENTER)
            self.book_tree.heading("Price", text="Price", anchor=CENTER)
            self.book_tree.heading("Quantity", text="Quantity", anchor=CENTER)

            ## set tree tags
            self.book_tree.tag_configure("odd", background="white")
            self.book_tree.tag_configure("even", background="lightblue")

            ## insert inital data
            self.insert_card_items()

            # Search Frame
            submit_frame = LabelFrame(
                self, text="Order Detail", font=("Arial", 12, "bold")
            )
            submit_frame.pack(fill="x", expand="yes")
            submit_frame.grid_columnconfigure(1, weight=1)

            ## create card label
            self.card_label = Label(
                submit_frame,
                text="the book will be delivered within 5 days",
                foreground="red",
                font=("Arial", 10, "bold"),
                background="lightblue",
            )
            self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

            ## final price
            price_frame = Frame(submit_frame, background="white")
            price_frame.grid(row=0, column=1, sticky="wnes")

            ###
            stotal_label = Label(
                price_frame, text="Sub Total Price:", background="white"
            )
            stotal_label.grid(row=0, column=0)

            ###
            ship_label = Label(price_frame, text="Shipping Price:", background="white")
            ship_label.grid(row=1, column=0)

            ###
            total_label = Label(price_frame, text="Total Price:", background="white")
            total_label.grid(row=2, column=0)

            ### price values
            stotal_label = Label(
                price_frame, text=self.sub_total_price, background="white"
            )
            stotal_label.grid(row=0, column=1)

            ###
            ship_label = Label(
                price_frame, text=self.shipping_price, background="white"
            )
            ship_label.grid(row=1, column=1)

            ###
            total_label = Label(price_frame, text=self.total_price, background="white")
            total_label.grid(row=2, column=1)

            ## check Card
            update_button = Button(
                submit_frame,
                text="Update Profile",
                background="white",
                command=lambda: self.controller.show_frame("UpdateProfile"),
            )
            update_button.grid(row=0, column=2, sticky=E, padx=6)

            ## check Card
            checkout_button = Button(
                submit_frame,
                text="Buy",
                background="white",
                command=self.final,
            )
            checkout_button.grid(row=0, column=3, sticky=E, padx=6)

    def insert_card_items(self):

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
                        item.quantity,
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
                        item.quantity,
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

    def final(self):
        if (
            messagebox.askquestion(title="finalize", message="Are you Sure To Proceed!")
            == "yes"
        ):
            purchace_date = datetime.now(tz=timezone.utc)
            deliver_date = purchace_date + timedelta(days=5)

            order = create_order(
                self.user.user_id,
                str(self.total_price),
                self.user.credit_card,
                None,
                deliver_date.timestamp(),
                purchace_date.timestamp(),
            )
            if order:
                clear_card(self.user.card.id)
                self.controller.user = get_customer_by_id(self.user.id)
                self.controller.current_order_id = order.id
                self.controller.show_frame("FactorPage")
            else:
                messagebox.showinfo("error", "there is problem creating new order")
