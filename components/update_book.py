import pdb
from tkinter.tix import Select
from typing import List
import tkinter as tk
from tkinter import (
    CENTER,
    END,
    NO,
    RIGHT,
    Y,
    Button,
    Entry,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    StringVar,
    ttk,
)
from tkinter import messagebox
from database.category import get_categoreis, get_category, get_category_by_title
from database.models import Admin, Author
from database.product import (
    create_product,
    get_author_by_product,
    get_product_by_id,
    update_product,
)

from .main_frame import MainFrame

from .datetime_entry import DateEntry


class UpdateBookPage(MainFrame):
    def init(self):
        st = ttk.Style()
        st.configure("C.Treeview", rowheight=18)
        self.product = get_product_by_id(self.controller.current_product_id)

        # main label
        main_label = Label(self, text="Update Book", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        top_frame = Frame(self)
        top_frame.pack(fill="x", expand="yes")
        top_frame.columnconfigure(0, weight=0)
        top_frame.columnconfigure(1, weight=0)
        top_frame.columnconfigure(2, weight=0)
        top_frame.columnconfigure(3, weight=0)

        # isbn
        self.isbn = StringVar()
        self.isbn.set(self.product.isbn)
        isbn_label = Label(top_frame, text="ISBN:", width=10)
        isbn_entry = Entry(
            top_frame, textvariable=self.isbn, font=("Arial", 10), state="disabled"
        )
        isbn_label.grid(row=0, column=0, padx=5)
        isbn_entry.grid(row=0, column=1, pady=5)

        # title
        title_label = Label(top_frame, text="Title:", width=15)
        self.title = StringVar()
        self.title.set(self.product.title)
        title_entry = Entry(top_frame, textvariable=self.title, font=("Arial", 10))
        title_label.grid(row=0, column=2, padx=5)
        title_entry.grid(row=0, column=3, pady=5)

        # deleted
        deleted_label = Label(top_frame, text="Deleted:", width=15)
        self.deleted = StringVar()
        self.deleted.set('True' if self.product.deleted else 'False')

        deleted_select = ttk.Combobox(
            top_frame, textvariable=self.deleted, font=("Arial", 10)
        )
        deleted_select["values"] = ["True", "False"]
        deleted_label.grid(row=0, column=4, padx=5)
        deleted_select.grid(row=0, column=5, pady=5)

        ### Authors frame
        author_frame = LabelFrame(self, text="Author(s)", font=("Arial", 12, "bold"))
        author_frame.pack(expand="yes", fill="x")
        author_frame.columnconfigure(0, weight=0)
        author_frame.columnconfigure(1, weight=1)

        auth_control_frame = Frame(author_frame)
        auth_control_frame.grid(row=0, column=0, sticky="wn")
        auth_control_frame.columnconfigure(0, weight=0)
        auth_control_frame.columnconfigure(1, weight=0)

        # auth entry
        self.author_var = StringVar()

        self.author_entry = Entry(
            auth_control_frame, textvariable=self.author_var, font=("Arial", 10)
        )
        self.author_entry.grid(row=0, column=0, sticky="wn", padx=5, pady=20)
        self.author_entry.bind("<Return>", self.add_author)

        # add button
        add_btn = Button(
            auth_control_frame,
            command=self.add_author,
            text="Add",
            width=6,
            background="white",
        )
        add_btn.grid(row=1, column=0, sticky="wen", padx=5)

        # delete button
        delete_button = Button(
            auth_control_frame,
            command=self.remove_author,
            text="Delete",
            width=6,
            background="white",
        )
        delete_button.grid(row=2, column=0, sticky="wen", padx=5)

        # tree view
        tree_frame = Frame(author_frame)
        tree_frame.grid(row=0, column=1, sticky="wnes", padx=20, pady=20)

        # scroll bar
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        self.author_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode="extended",
            show="headings",
            height=5,
            style="C.Treeview",
        )
        self.author_tree.pack(fill="both", expand=True)
        tree_scroll.config(command=self.author_tree.yview)

        # set three headers
        self.author_tree["columns"] = ["Author"]

        # set tree columns
        self.author_tree.column("#0", width=0, stretch=NO)
        self.author_tree.column("Author", width=50, anchor=CENTER)
        self.author_tree.heading("Author", text="Author", anchor=CENTER)

        # address frame
        address_frame = LabelFrame(
            self, text="Product Detail", font=("Arial", 14, "bold")
        )
        address_frame.pack(fill="x", expand="yes")
        address_frame.columnconfigure(0, weight=0)
        address_frame.columnconfigure(1, weight=0)
        address_frame.columnconfigure(2, weight=0)
        address_frame.columnconfigure(3, weight=0)

        author = get_author_by_product(self.product.id)
        self.add_custom_author(author)

        # Publisher
        publisher_label = Label(address_frame, text="Publisher", width=10)
        self.publisher = StringVar()
        self.publisher.set(self.product.publisher)

        publisher_entry = Entry(
            address_frame, textvariable=self.publisher, font=("Arial", 10)
        )
        publisher_label.grid(row=0, column=0, padx=5)
        publisher_entry.grid(row=0, column=1, pady=5)

        # Price
        price_label = Label(address_frame, text="Price", width=10)
        self.price = StringVar()
        self.price.set(self.product.price)

        price_entry = Entry(address_frame, textvariable=self.price, font=("Arial", 10))
        price_label.grid(row=0, column=2, padx=5)
        price_entry.grid(row=0, column=3, pady=5)

        # Quantity
        quantity_label = Label(address_frame, text="Quantity", width=10)
        self.quantity = StringVar()
        self.quantity.set(self.product.quantity)

        quantity_entry = Entry(
            address_frame, textvariable=self.quantity, font=("Arial", 10)
        )
        quantity_label.grid(row=1, column=0, padx=5)
        quantity_entry.grid(row=1, column=1, pady=5)

        # Year
        publish_year_label = Label(address_frame, text="Publish Year", width=10)
        self.year = StringVar()
        self.year.set(self.product.year)

        year_entry = Entry(address_frame, textvariable=self.year, font=("Arial", 10))
        publish_year_label.grid(row=1, column=2)
        year_entry.grid(row=1, column=3, pady=5)

        # credit card frame
        credit_frame = LabelFrame(self, text="Category", font=("Arial", 14, "bold"))
        credit_frame.pack(fill="x", expand="yes")
        credit_frame.columnconfigure(0, weight=0)
        credit_frame.columnconfigure(1, weight=0)
        credit_frame.columnconfigure(2, weight=0)
        credit_frame.columnconfigure(3, weight=0)

        self.categoreis = get_categoreis()
        # credit card type
        type_label = Label(credit_frame, text="Category")
        self.category_title = tk.StringVar()

        if self.product.category and self.product.category.title:
            self.category_title.set(self.product.category.title)

        self.type_select = ttk.Combobox(
            credit_frame, width=15, textvariable=self.category_title
        )
        type_label.grid(row=0, column=0, padx=5)
        self.type_select.grid(row=0, column=1, pady=5, padx=5)
        self.type_select["values"] = [category.title for category in self.categoreis]
        self.type_select["state"] = "readonly"

        submit_button = Button(
            self,
            text="Update",
            background="white",
            foreground="green",
            command=self.update_book,
        )
        submit_button.pack(fill="x", expand="yes", padx=200)

    def update_book(self):
        while 1:
            if not self.title.get():
                messagebox.showerror(title="title", message="tile must not be empty")
                break

            elif not self.isbn.get():
                messagebox.showerror(title="isbn", message="isbn must not be empty")
                break

            elif not self.author_tree.get_children():
                messagebox.showerror(title="author", message="author must not be empty")
                break

            elif not self.publisher.get():
                messagebox.showerror(
                    title="publisher", message="publisher must not be empty"
                )
                break

            elif not self.price.get():
                messagebox.showerror(title="price", message="price must not be empty")
                break

            elif not self.quantity.get():
                messagebox.showerror(
                    title="quantity", message="quantity must not be empty"
                )
                break

            elif not self.year.get():
                messagebox.showerror(title="year", message="yaer must not be empty")
                break

            elif not self.category_title.get():
                messagebox.showerror(
                    title="category", message="select a category for book"
                )
                break

            category = get_category_by_title(self.category_title.get())
            author_list = []

            for line in self.author_tree.get_children():
                for value in self.author_tree.item(line)["values"]:
                    author_list.append(value)

            res = update_product(
                self.product.id,
                category.id,
                self.title.get(),
                self.publisher.get(),
                self.price.get(),
                int(self.quantity.get()),
                self.year.get(),
                author_list,
                int(self.deleted.get() == "True"),
            )

            if res:
                messagebox.showinfo("success", "product added success")
                prev = self.controller.history[-2]
                self.controller.show_frame(prev)
            else:
                messagebox.showerror("error", "problem adding new product")

            break

    def add_author(self, *args):
        self.author_tree.insert("", index="end", values=(self.author_var.get()))
        self.author_entry.delete(0, END)

    def add_custom_author(self, authors: List[Author]):
        for author in authors:
            self.author_tree.insert(
                "", index="end", values=author.firstname + " " + author.lastname
            )
            self.author_entry.delete(0, END)

    def remove_author(self, *args):
        selection = self.author_tree.selection()

        for s in selection:
            self.author_tree.delete(s)
