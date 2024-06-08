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

from database.category import *
from database.models import Admin

from .main_frame import MainFrame


class SystemPage(MainFrame):
    def init(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="System Maintanace", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # Search Frame
        search_frame = LabelFrame(self, text="Input", font=("Arial", 12, "bold"))
        search_frame.pack(fill="x", expand="yes")

        search_frame.columnconfigure(0, weight=0)
        search_frame.columnconfigure(1, weight=0)
        search_frame.columnconfigure(2, weight=1)

        # search label
        search_label = Label(search_frame, text="search category by title")
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
        self.category_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode="extended",
            show="headings",
            height=5,
        )
        self.category_tree.pack(fill="both", expand=True)

        # configure scrollbar
        tree_scroll.config(command=self.category_tree.yview)

        # set three headers
        self.category_tree["columns"] = (
            "Title",
            "State",
            "Credit Type",
        )

        # set tree columns
        self.category_tree.column("#0", width=0, stretch=NO)
        self.category_tree.column("Title", anchor=CENTER, width=100)
        self.category_tree.column("State", anchor=CENTER, width=130)
        self.category_tree.column("Credit Type", anchor=CENTER, width=130)

        # set hedings
        self.category_tree.heading("Title", text="Title", anchor=CENTER)
        self.category_tree.heading("State", text="Title", anchor=CENTER)
        self.category_tree.heading("Credit Type", text="Publisher", anchor=CENTER)

        # set tree tags
        self.category_tree.tag_configure("odd", background="white")
        self.category_tree.tag_configure("even", background="lightblue")

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
            command=lambda: self.controller.show_frame("InsertCategoryPage"),
        )
        add_to_button.grid(row=0, column=0, sticky=E, padx=5)

        #  delete button
        add_to_button = Button(
            card_frame,
            text="Delete",
            width=10,
            background="white",
            command=self.delete_cetegory,
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
        self.categoreis = get_categoreis()
        self.insert_category_item()

    def insert_category_item(self):
        for index, c in enumerate(self.categoreis):
            if index % 2 == 0:
                self.category_tree.insert(
                    parent="",
                    index="end",
                    iid=c.id,
                    text="",
                    values=(
                        c.title,
                        c.state,
                        c.credit_type,
                    ),
                    tags="odd",
                )

            else:
                self.category_tree.insert(
                    parent="",
                    index="end",
                    iid=c.id,
                    text="",
                    values=(
                        c.title,
                        c.state,
                        c.credit_type,
                    ),
                    tags="even",
                )

    def search(self, *args):
        self.categoreis = filter_category(self.text_var.get())
        self.clean_table()
        self.insert_category_item()

    def delete_cetegory(self):
        selection = self.category_tree.selection()

        if (
            len(selection)
            and messagebox.askquestion(
                "askquestion", f"Are you sure deleting {len(selection)} item?"
            )
            == "yes"
        ):
            for item in selection:
                self.category_tree.delete(item)
                delete_category(int(item))

            self.categoreis = get_categoreis()
            self.clean_table()
            self.insert_category_item()

    def clean_table(self):
        for item in self.category_tree.get_children():
            self.category_tree.delete(item)

    def modify(self):
        for id in self.category_tree.selection():
            self.controller.current_category = int(id)
            self.controller.show_frame("UpdateCategoryPage")
            break
        else:
            messagebox.showinfo("no selecteditem", "select a book inorder to modify")
