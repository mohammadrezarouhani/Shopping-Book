from importlib.abc import ResourceReader
import pdb
import tkinter as tk
from tkinter import OptionMenu, messagebox
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


class ReportPage(MainFrame):
    def init(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Report Page", font=("Arial", 16, "bold"))
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
        report_type = ttk.Combobox(search_frame, width=15, textvariable=self.text_var)
        report_type.config(width=80)
        report_type["values"] = [
            "total sale from last month from each category",
            "total number of books in stock for each category",
            "list of top ten sellers in decending order from last three month",
            "list of most expencive book from each category in descending order",
            "for each category list teh total number of distinct buyers(as indetified byu their user name) in the last month",
            "statistical report average amount of sale per customer lastmonth, average number of books per perchase transaction, average number of customers per day",
        ]
        report_type.grid(row=0, column=1, padx=5, pady=10)

        #  add button
        search_button = Button(
            search_frame,
            text="Submit",
            background="white",
            width=15,
            command=self.submit,
        )
        search_button.grid(row=0, column=2, padx=5, pady=10, sticky="e")

        # creating a tree view
        tree_frame = Frame(self)
        tree_frame.pack(pady=20, fill="both", expand="yes", padx=20)

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
        self.category_tree.heading("State", text="State", anchor=CENTER)
        self.category_tree.heading("Credit Type", text="Publisher", anchor=CENTER)

        # set tree tags
        self.category_tree.tag_configure("odd", background="white")
        self.category_tree.tag_configure("even", background="lightblue")

    def submit(self):
        pass

    def report_1(self):
        pass

    def report2(self):
        pass

    def report3(self):
        pass

    def report4(self):
        pass

    def report5(self):
        pass

    def report6(self):
        pass
