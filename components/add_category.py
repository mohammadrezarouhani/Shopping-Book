from ast import Delete
from cgitb import text
from logging import PlaceHolder
from os import name
import pdb
from sqlite3 import Row
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

from database.category import (
    create_category,
)

from .main_frame import MainFrame


class InsertCategoryPage(MainFrame):
    def init(self):
        st = ttk.Style()
        st.configure("C.Treeview", rowheight=18)

        # main label
        main_label = Label(self, text="Insert New Category", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        top_frame = Frame(self)
        top_frame.pack(fill="x", expand="yes")
        top_frame.columnconfigure(0, weight=1)
        top_frame.columnconfigure(1, weight=1)

        # Title:
        self.title = StringVar()
        title_label = Label(top_frame, text="Title:", width=15)
        title_entry = Entry(top_frame, textvariable=self.title, font=("Arial", 10))
        title_label.grid(row=0, column=0, padx=5, sticky="e")
        title_entry.grid(row=0, column=1, pady=5, sticky="w")

        # State:
        state_label = Label(top_frame, text="State:", width=15)
        self.state = StringVar()
        state_entry = Entry(top_frame, textvariable=self.state, font=("Arial", 10))
        state_label.grid(row=1, column=0, padx=5, sticky="e")
        state_entry.grid(row=1, column=1, pady=5, sticky="w")

        # Credit Type:
        state_label = Label(top_frame, text="Credit Type:", width=15)
        self.creadit_type = StringVar()
        state_entry = Entry(
            top_frame, textvariable=self.creadit_type, font=("Arial", 10)
        )
        state_label.grid(row=2, column=0, padx=5, sticky="e")
        state_entry.grid(row=2, column=1, pady=5, sticky="w")

        submit_button = Button(
            self,
            text="Insert",
            background="white",
            foreground="green",
            command=self.insert_new_category,
        )
        submit_button.pack(fill="x", expand="yes", padx=200)

    def insert_new_category(self):
        while 1:
            if not self.title.get():
                messagebox.showerror(title="title", message="tile must not be empty")
                break

            elif not self.state.get():
                messagebox.showerror(title="state", message="state must not be empty")
                break

            elif not self.creadit_type.get():
                messagebox.showerror(
                    title="creadit_type", message="creadit_type must not be empty"
                )
                break

            res = create_category(
                self.title.get(), self.state.get(), self.creadit_type.get()
            )

            if res:
                messagebox.showinfo("success", "product added success")
                prev = self.controller.history[-2]
                self.controller.show_frame(prev)
            else:
                messagebox.showerror("error", "problem adding new product")
            break
