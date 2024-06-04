from cgitb import text
from logging import PlaceHolder
from os import name
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

from .datetime_entry import DateEntry


class UpdateBookPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        st = ttk.Style()
        st.configure("C.Treeview", rowheight=18)

        # main label
        main_label = Label(self, text="Update Book Info", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        top_frame = Frame(self)
        top_frame.pack(fill="x", expand="yes")
        top_frame.columnconfigure(0, weight=0)
        top_frame.columnconfigure(1, weight=1)
        top_frame.columnconfigure(2, weight=0)
        top_frame.columnconfigure(3, weight=1)

        # isbn
        isbn_label = Label(top_frame, text="ISBN:", width=10)
        isbn_entry = Entry(
            top_frame,
        )
        isbn_label.grid(row=0, column=0)
        isbn_entry.grid(row=0, column=1, pady=5)

        # title
        title_label = Label(top_frame, text="Title:", width=15)
        title_entry = Entry(top_frame)
        title_label.grid(row=0, column=2)
        title_entry.grid(row=0, column=3, pady=5)

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
            auth_control_frame, textvariable=self.author_var, font=("Arial", 12)
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
            self, text="Addres Detail", font=("Arial", 14, "bold")
        )
        address_frame.pack(fill="x", expand="yes")
        address_frame.columnconfigure(0, weight=0)
        address_frame.columnconfigure(1, weight=1)
        address_frame.columnconfigure(2, weight=0)
        address_frame.columnconfigure(3, weight=1)

        # address
        address_label = Label(address_frame, text="address", width=10)
        address_entry = Entry(
            address_frame,
        )
        address_label.grid(row=0, column=0)
        address_entry.grid(row=0, column=1, pady=5)

        # city
        city_label = Label(address_frame, text="city", width=10)
        city_entry = Entry(
            address_frame,
        )
        city_label.grid(row=0, column=2)
        city_entry.grid(row=0, column=3, pady=5)

        # state
        state_label = Label(address_frame, text="state", width=10)
        state_entry = Entry(
            address_frame,
        )
        state_label.grid(row=1, column=0)
        state_entry.grid(row=1, column=1, pady=5)

        # zip code
        zip_label = Label(address_frame, text="Credit Card", width=10)
        zip_entry = Entry(
            address_frame,
        )
        zip_label.grid(row=1, column=2)
        zip_entry.grid(row=1, column=3, pady=5)

        # credit card frame
        credit_frame = LabelFrame(
            self, text="Credit Card Detail", font=("Arial", 14, "bold")
        )
        credit_frame.pack(fill="x", expand="yes")
        credit_frame.columnconfigure(0, weight=0)
        credit_frame.columnconfigure(1, weight=1)
        credit_frame.columnconfigure(2, weight=0)
        credit_frame.columnconfigure(3, weight=1)

        # credit card type
        type_label = Label(credit_frame, text="Card Type")
        type_var = tk.StringVar()
        type_select = ttk.Combobox(credit_frame, width=15, textvariable=type_var)
        type_label.grid(row=0, column=0)
        type_select.grid(row=0, column=1, pady=5)

        # zip code
        card_num_label = Label(credit_frame, text="Credit Number", width=12)
        card_num_entry = Entry(credit_frame)
        card_num_label.grid(row=0, column=2)
        card_num_entry.grid(row=0, column=3, pady=5)

        datetime_entry = DateEntry(credit_frame)
        datetime_entry.grid(row=0, column=4)

        submit_button = Button(
            self,
            text="Update",
            background="white",
            foreground="green",
            command=self.update_book_info,
        )
        submit_button.pack(fill="x", expand="yes", padx=200)

    def update_book_info(self):
        pass

    def add_author(self, *args):
        self.author_tree.insert("", index="end", values=(self.author_var.get()))
        self.author_entry.delete(0, END)

    def remove_author(self, *args):
        selection = self.author_tree.selection()

        for s in selection:
            self.author_tree.delete(s)
