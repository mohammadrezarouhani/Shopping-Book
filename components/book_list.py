import tkinter as tk
from tkinter import (
    CENTER,
    E,
    NO,
    RIGHT,
    W,
    Y,
    Button,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)
from tkinter import messagebox
from .main_frame import MainFrame
from database import *


class BookListPage(MainFrame):
    def init(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Order Book", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # Search Frame
        search_frame = LabelFrame(self, text="Input")
        search_frame.pack(fill="x", expand="yes")
        search_frame.columnconfigure(0, weight=1)
        search_frame.columnconfigure(1, weight=1)
        search_frame.columnconfigure(2, weight=1)

        # create search label
        search_label = Label(
            search_frame,
            text="search by ISBN or title or publisher",
            font=("Arial", 10),
        )
        search_label.grid(row=0, column=0, padx=10, pady=10)

        # create a entry labelo and biding text change event
        self.text_var = tk.StringVar()
        search_entry = Entry(search_frame, textvariable=self.text_var)
        search_entry.grid(row=0, column=1, padx=10, pady=10)
        # search_entry.bind("<KeyRelease>", self.search)

        search_button = Button(
            search_frame,
            text="Search",
            width=6,
            background="white",
            command=self.search,
        )
        search_button.grid(row=0, column=2, sticky=W)

        # create add to card button
        add_to_button = Button(
            search_frame,
            text="Add to Card",
            width=8,
            background="white",
            command=self.add_to_card,
        )
        add_to_button.grid(row=0, column=3, sticky=W)

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
        self.book_tree["columns"] = ("ISBN", "Title", "Publisher", "Price", "Quantity")

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

        # Search Frame
        card_frame = LabelFrame(self, text="Card Detail")
        card_frame.pack(fill="x", expand="yes")
        card_frame.grid_columnconfigure(1, weight=1)

        # create card label
        self.card_label = Label(card_frame, text="There is 0 Item in Shopping Card")
        self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

        # checkout Card
        checkout_button = Button(
            card_frame,
            text="Checkout",
            background="white",
            command=self.checkout,
        )
        checkout_button.grid(row=0, column=1, sticky=E, padx=6)

        self.remove_from_tree()
        self.product_list = get_products()
        self.insert_book_item()

    def insert_book_item(self):
        for index, product in enumerate(self.product_list):
            if index % 2 == 0:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=product.id,
                    text="",
                    values=(
                        product.isbn,
                        product.title,
                        product.publisher,
                        product.price + "$",
                        product.quantity,
                    ),
                    tags="odd",
                )

            else:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=product.id,
                    text="",
                    values=(
                        product.isbn,
                        product.title,
                        product.publisher,
                        product.price + "$",
                        product.quantity,
                    ),
                    tags="even",
                )

    def search(self, *args):
        self.remove_from_tree()
        self.product_list = filter_product(self.text_var.get())
        self.insert_book_item()

    def add_to_card(self):
        # create inital car dif user not logged in

        if not self.controller.user:
            self.controller.user = Customer()
            self.controller.user.card = Card()

        card_items: List[CardItem] = self.controller.user.card.card_items

        for item in self.book_tree.selection():
            target_product_id = int(item)

            # card item product
            product = get_single_product(target_product_id)
            user = self.controller.user

            if not self.controller.logged_in:
                pointer = -1
                # get index if item already added
                for index, card_item in enumerate(card_items):
                    if card_item.product_id == target_product_id:
                        pointer = index
                        break

                # if index create new item else update old item
                if pointer < 0:
                    new_item = CardItem(0, target_product_id, 0, 1, product)
                    user.card.card_items.append(new_item)
                    print("[Added]:", new_item)

                elif card_items[pointer].quantity < product.quantity:
                    user.card.card_items[pointer].quantity += 1
                    print("[Increased]: +1")
                else:
                    messagebox.showerror(title="error", message="not enough in stock!")

            else:
                item = get_card_item(target_product_id, user.card.id)

                if item:
                    update_card_item(target_product_id, user.card.id, item.quantity + 1)
                else:
                    create_card_item(user.card.id, target_product_id, 1)

                self.controller.user.card = get_card(user.id)

            self.card_label.config(
                text=f"there is {len(self.controller.user.card.card_items)} items in Shopping",
                foreground="green",
            )

    def remove_from_tree(self):
        for record in self.book_tree.get_children():
            self.book_tree.delete(record)

    def checkout(self):
        try:
            card_items: List[CardItem] = self.controller.user.card.card_items
        except:
            card_items = []

        if len(card_items):
            self.controller.show_frame("ShoppingCardPage")
        else:
            messagebox.showerror(
                title="error", message="there is no item in shopping card"
            )
