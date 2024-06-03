from re import X
import tkinter as tk
from tkinter import (
    CENTER,
    E,
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
from turtle import width


class ShoppingCardPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # style.map("TreeView", background=[("selected", "#347083")])

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
            "Publisher",
            "Price",
        )

        # set tree columns
        self.book_tree.column("#0", width=0, stretch=NO)
        self.book_tree.column("Index", width=50, anchor=CENTER)
        self.book_tree.column("ISBN", anchor=CENTER, width=100)
        self.book_tree.column("Title", anchor=CENTER, width=130)
        self.book_tree.column("Author", anchor=CENTER, width=130)
        self.book_tree.column("Publisher", anchor=CENTER, width=130)
        self.book_tree.column("Price", anchor=CENTER, width=100)

        # set hedings
        self.book_tree.heading("Index", text="Index", anchor=CENTER)
        self.book_tree.heading("ISBN", text="ISBN", anchor=CENTER)
        self.book_tree.heading("Title", text="Title", anchor=CENTER)
        self.book_tree.heading("Author", text="Author", anchor=CENTER)
        self.book_tree.heading("Publisher", text="Publisher", anchor=CENTER)
        self.book_tree.heading("Price", text="Price", anchor=CENTER)

        # set tree tags
        self.book_tree.tag_configure("odd", background="white")
        self.book_tree.tag_configure("even", background="lightblue")

        # insert inital data
        self.insert_book_item()

        # Search Frame
        card_frame = LabelFrame(self, text="Card Detail")
        card_frame.pack(fill="x", expand="yes")
        card_frame.grid_columnconfigure(1, weight=1)

        # create card label
        self.card_label = Label(card_frame, text="There is 0 Item in Shopping Card")
        self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

        # check Card
        checkout_button = Button(
            card_frame,
            text="Proceed",
            background="white",
            command=lambda: self.controller.show_frame("ReportPage"),
        )
        checkout_button.grid(row=0, column=1, sticky=E, padx=6)

    def insert_book_item(self):
        for i in range(100):
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

    def add_to_card(self):
        for item in self.book_tree.selection():
            item_text = self.book_tree.item(item, "values")
            print(item_text)

    def remove_from_tree(self):
        for record in self.book_tree.get_children():
            self.book_tree.delete(record)
