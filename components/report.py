from importlib.abc import ResourceReader
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

from database import *
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
        self.report_option = [
            "total sale from last month from each category",
            "total number of books in stock for each category",
            "list of top ten sellers in decending order from last three month",
            "list of most expencive book from each category in descending order",
            "for each category list teh total number of distinct buyers(as indetified byu their user name) in the last month",
            "statistical report average amount of sale per customer lastmonth",
            "average number of books per perchase transaction",
            "average number of customers per day",
        ]
        self.report_type = tk.StringVar()
        report_type = ttk.Combobox(
            search_frame, width=15, textvariable=self.report_type
        )
        report_type.config(width=80)
        report_type["values"] = self.report_option
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
        self.report_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode="extended",
            show="headings",
            height=5,
        )
        self.report_tree.pack(fill="both", expand=True)

        # configure scrollbar
        tree_scroll.config(command=self.report_tree.yview)

    def submit(self):
        self.clear_tree()
        if self.report_type.get() == self.report_option[0]:
            self.report_1()

        elif self.report_type.get() == self.report_option[1]:
            self.report2()

        elif self.report_type.get() == self.report_option[2]:
            self.report3()

        elif self.report_type.get() == self.report_option[3]:
            self.report4()

        elif self.report_type.get() == self.report_option[4]:
            self.report5()

        elif self.report_type.get() == self.report_option[5]:
            self.report6()

        elif self.report_type.get() == self.report_option[6]:
            self.report7()

        elif self.report_type.get() == self.report_option[7]:
            self.report8()

    def report_1(self):
        self.report_tree["columns"] = (
            "Title",
            "Amount",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Title", anchor=CENTER, width=100)
        self.report_tree.column("Amount", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Title", text="Title", anchor=CENTER)
        self.report_tree.heading("Amount", text="Amount", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.title, d.amount) for d in total_sale_for_each_category()]
        self.insert_table(data)

    def report2(self):
        self.report_tree["columns"] = (
            "Title",
            "Number",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Title", anchor=CENTER, width=100)
        self.report_tree.column("Number", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Title", text="Title", anchor=CENTER)
        self.report_tree.heading("Number", text="Number", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.title, d.number) for d in total_number_of_category_book()]
        self.insert_table(data)

    def report3(self):
        self.report_tree["columns"] = (
            "Name",
            "Income",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Name", anchor=CENTER, width=100)
        self.report_tree.column("Income", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Name", text="Name", anchor=CENTER)
        self.report_tree.heading("Income", text="Income", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.name, d.income) for d in top_ten_best_seller()]
        self.insert_table(data)

    def report4(self):
        self.report_tree["columns"] = (
            "Category",
            "Title",
            "Price",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Category", anchor=CENTER, width=100)
        self.report_tree.column("Title", anchor=CENTER, width=130)
        self.report_tree.column("Price", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Category", text="Category", anchor=CENTER)
        self.report_tree.heading("Title", text="Title", anchor=CENTER)
        self.report_tree.heading("Price", text="Price", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.category, d.book_title, d.price) for d in most_expecive_books()]
        self.insert_table(data)

    def report5(self):
        self.report_tree["columns"] = (
            "Title",
            "Number",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Title", anchor=CENTER, width=130)
        self.report_tree.column("Number", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Title", text="Title", anchor=CENTER)
        self.report_tree.heading("Number", text="Number", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.title, d.number) for d in category_distinct_buyers()]
        self.insert_table(data)

    def report6(self):
        self.report_tree["columns"] = (
            "Username",
            "Amount",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Username", anchor=CENTER, width=130)
        self.report_tree.column("Amount", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Username", text="Username", anchor=CENTER)
        self.report_tree.heading("Amount", text="Amount", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.username, d.amount) for d in avg_sale_per_customer()]
        self.insert_table(data)

    def report7(self):
        self.report_tree["columns"] = (
            "Title",
            "Number",
        )

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column("Title", anchor=CENTER, width=130)
        self.report_tree.column("Number", anchor=CENTER, width=130)

        # set hedings
        self.report_tree.heading("Title", text="Title", anchor=CENTER)
        self.report_tree.heading("Number", text="Number", anchor=CENTER)

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        data = [(d.title, d.number) for d in avg_number_of_book_per_sale()]
        self.insert_table(data)

    def report8(self):
        self.report_tree["columns"] = ("Average Customer From Last Month",)

        # set tree columns
        self.report_tree.column("#0", width=0, stretch=NO)
        self.report_tree.column(
            "Average Customer From Last Month", anchor=CENTER, width=130
        )

        # set hedings
        self.report_tree.heading(
            "Average Customer From Last Month",
            text="Average Sale Number In 30 days",
            anchor=CENTER,
        )

        # set tree tags
        self.report_tree.tag_configure("odd", background="white")
        self.report_tree.tag_configure("even", background="lightblue")
        self.insert_single_data_to_table(daily_customer_number_avg())

    def insert_table(self, items):
        for index, item in enumerate(items):
            if index % 2 == 0:
                self.report_tree.insert(
                    parent="",
                    index="end",
                    iid=index,
                    text="",
                    values=item,
                    tags="odd",
                )

            else:
                self.report_tree.insert(
                    parent="",
                    index="end",
                    iid=index,
                    text="",
                    values=item,
                    tags="even",
                )

    def insert_single_data_to_table(self, item):
        self.report_tree.insert(
            parent="",
            index="end",
            iid=0,
            text="",
            values=item,
            tags="odd",
        )

    def clear_tree(self):
        for record in self.report_tree.get_children():
            self.report_tree.delete(record)
