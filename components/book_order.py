from cgitb import text
from functools import wraps
from importlib.abc import ResourceReader
from re import X
import tkinter as tk
from tkinter import (
    CENTER,
    NO,
    RIGHT,
    Y,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)


class BookOrderPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Manage Book Orders", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # Search Frame
        search_frame = LabelFrame(self, text="Input")
        search_frame.pack(fill="x", expand="yes")
        search_frame.columnconfigure(0, weight=1)
        search_frame.columnconfigure(1, weight=1)
        search_frame.columnconfigure(2, weight=1)

        # create search label
        search_label = Label(
            search_frame, text="search by ISBN or title or author or publisher"
        )
        search_label.grid(row=0, column=0, padx=10, pady=10)

        # create a entry labelo and biding text change event
        self.text_var = tk.StringVar()
        self.text_var.trace_add("write", self.search)
        search_entry = Entry(search_frame, textvariable=self.text_var)
        search_entry.grid(row=0, column=1, padx=10, pady=10)
        # search_entry.bind("<KeyRelease>", self.search)

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
            "Index",
            "ISBN",
            "Title",
            "Author",
            "Quantity",
            "Minimum",
            "OrderQuantity",
        )

        # set tree columns
        self.book_tree.column("#0", width=0, stretch=NO)
        self.book_tree.column("Index", width=50, anchor=CENTER)
        self.book_tree.column("ISBN", anchor=CENTER, width=100)
        self.book_tree.column("Title", anchor=CENTER, width=130)
        self.book_tree.column("Author", anchor=CENTER, width=130)
        self.book_tree.column("Quantity", anchor=CENTER, width=130)
        self.book_tree.column("Minimum", anchor=CENTER, width=100)
        self.book_tree.column("OrderQuantity", anchor=CENTER, width=100)

        # set hedings
        self.book_tree.heading("Index", text="Index", anchor=CENTER)
        self.book_tree.heading("ISBN", text="ISBN", anchor=CENTER)
        self.book_tree.heading("Title", text="Title", anchor=CENTER)
        self.book_tree.heading("Author", text="Author", anchor=CENTER)
        self.book_tree.heading("Quantity", text="Quantity in Stock", anchor=CENTER)
        self.book_tree.heading("Minimum", text="Minimum Required", anchor=CENTER)
        self.book_tree.heading("OrderQuantity", text="OrderQuantity", anchor=CENTER)

        # set tree tags
        self.book_tree.tag_configure("odd", background="white")
        self.book_tree.tag_configure("even", background="lightblue")
        self.book_tree.tag_configure("submitted", background="green")
        self.book_tree.tag_configure("dismissed", background="red")

        # insert inital data
        self.insert_order_item()

        # Search Frame
        card_frame = LabelFrame(self, text="Card Detail")
        card_frame.pack(fill="x", expand="yes")
        card_frame.grid_columnconfigure(1, weight=1)

        # create card label
        self.card_label = Label(
            card_frame, text="There is 0 Order in a Way", foreground="green"
        )
        self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

    def insert_order_item(self):
        for i in range(10):
            if i % 2 == 0:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=i,
                    text="",
                    values=(
                        i,
                        "test",
                        "test",
                        "test",
                        "test",
                        "test",
                    ),
                    tags="odd",
                )

            else:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=i,
                    text="",
                    values=(
                        i,
                        "test",
                        "test",
                        "test",
                        "test",
                        "test",
                    ),
                    tags="even",
                )

    def search(self, *args):
        """query to data base for filtering"""
        print(f"Text changed to: {self.text_var.get()}")
