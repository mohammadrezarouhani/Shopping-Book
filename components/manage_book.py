from importlib.abc import ResourceReader
import pdb
import tkinter as tk
from tkinter import messagebox
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

from database.models import Admin
from database.product import (
    delete_product,
    filter_product,
    get_all_user_products,
    manger_filter_book,
)

from .main_frame import MainFrame

# from tkinter import messagebox


class ManageBookPage(MainFrame):
    def init(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Manage Book Store", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # Search Frame
        search_frame = LabelFrame(self, text="Input", font=("Arial", 12, "bold"))
        search_frame.pack(fill="x", expand="yes")

        search_frame.columnconfigure(0, weight=0)
        search_frame.columnconfigure(1, weight=0)
        search_frame.columnconfigure(2, weight=1)

        # search label
        search_label = Label(search_frame, text="search by ISBN or title or publisher")
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
            "Deleted",
        )

        # set tree columns
        self.book_tree.column("#0", width=0, stretch=NO)
        self.book_tree.column("ISBN", anchor=CENTER, width=100)
        self.book_tree.column("Title", anchor=CENTER, width=130)
        self.book_tree.column("Publisher", anchor=CENTER, width=130)
        self.book_tree.column("Price", anchor=CENTER, width=100)
        self.book_tree.column("Deleted", anchor=CENTER, width=130)

        # set hedings
        self.book_tree.heading("ISBN", text="ISBN", anchor=CENTER)
        self.book_tree.heading("Title", text="Title", anchor=CENTER)
        self.book_tree.heading("Publisher", text="Publisher", anchor=CENTER)
        self.book_tree.heading("Price", text="Price", anchor=CENTER)
        self.book_tree.heading("Deleted", text="Deleted", anchor=CENTER)

        # set tree tags
        self.book_tree.tag_configure("odd", background="white")
        self.book_tree.tag_configure("even", background="lightblue")

        # Order Frame
        card_frame = Frame(self)
        card_frame.pack(fill="x", expand="yes", padx=10)
        card_frame.grid_columnconfigure(0, weight=1)

        #  add button
        add_to_button = Button(
            card_frame,
            text="Add",
            width=10,
            background="white",
            command=lambda: self.controller.show_frame("InsertBookPage"),
        )
        add_to_button.grid(row=0, column=0, sticky=E, padx=5)

        #  delete button
        add_to_button = Button(
            card_frame,
            text="Delete",
            width=10,
            background="white",
            command=self.delete_book,
        )
        add_to_button.grid(row=0, column=1, sticky=E, padx=5)

        # checkout Card
        checkout_button = Button(
            card_frame,
            text="Modify",
            width=10,
            background="white",
            command=self.modify,
        )
        checkout_button.grid(row=0, column=2, sticky=E, padx=6, pady=10)

        self.user: Admin = self.controller.user
        self.products = get_all_user_products(self.user.user_id)
        self.insert_book_item()

    def insert_book_item(self):
        for index, p in enumerate(self.products):
            if index % 2 == 0:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=p.id,
                    text="",
                    values=(
                        p.isbn,
                        p.title,
                        p.publisher,
                        p.price,
                        "True" if p.deleted else "False",
                    ),
                    tags="odd",
                )

            else:
                self.book_tree.insert(
                    parent="",
                    index="end",
                    iid=p.id,
                    text="",
                    values=(
                        p.isbn,
                        p.title,
                        p.publisher,
                        p.price,
                        "True" if p.deleted else "False",
                    ),
                    tags="even",
                )

    def search(self, *args):
        """query to data base for filtering"""
        print(f"Text changed to: {self.text_var.get()}")
        self.products = manger_filter_book(self.text_var.get(), self.user.user_id)
        self.clean_table()
        self.insert_book_item()

    def delete_book(self):
        selection = self.book_tree.selection()

        if (
            len(selection)
            and messagebox.askquestion(
                "askquestion", f"Are you sure deleting {len(selection)} item?"
            )
            == "yes"
        ):
            for item in selection:
                self.book_tree.delete(item)
                delete_product(int(item))

            self.products = get_all_user_products(self.user.user_id)
            self.clean_table()
            self.insert_book_item()

    def clean_table(self):
        for item in self.book_tree.get_children():
            self.book_tree.delete(item)

    def modify(self):
        for id in self.book_tree.selection():
            self.controller.current_product_id = int(id)
            self.controller.show_frame("UpdateBookPage")
            break
        else:
            messagebox.showinfo("no selecteditem", "select a book inorder to modify")
