from re import X
from tkinter import (
    CENTER,
    E,
    NO,
    RIGHT,
    Y,
    Button,
    Frame,
    Label,
    LabelFrame,
    Scrollbar,
    ttk,
)
from tkinter import messagebox

from database import *

from .main_frame import MainFrame


class ShoppingCardPage(MainFrame):
    def init(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # main label
        main_label = Label(self, text="Card Item", font=("Arial", 16, "bold"))
        main_label.pack(fill="x", expand=True)

        # creating a tree view
        tree_frame = Frame(self)
        tree_frame.pack(pady=10, fill="both", expand="yes")

        # adding scroll bar to tree view
        tree_scroll = Scrollbar(tree_frame)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # creating tree view
        self.card_tree = ttk.Treeview(
            tree_frame,
            yscrollcommand=tree_scroll.set,
            selectmode="extended",
            show="headings",
            height=5,
        )
        self.card_tree.pack(fill="both", expand=True)

        # configure scrollbar
        tree_scroll.config(command=self.card_tree.yview)

        # set three headers
        self.card_tree["columns"] = (
            "ISBN",
            "Title",
            "Publisher",
            "Price",
            "Quantity",
        )

        # set tree columns
        self.card_tree.column("#0", width=0, stretch=NO)
        self.card_tree.column("ISBN", anchor=CENTER, width=100)
        self.card_tree.column("Title", anchor=CENTER, width=130)
        self.card_tree.column("Publisher", anchor=CENTER, width=130)
        self.card_tree.column("Price", anchor=CENTER, width=100)
        self.card_tree.column("Quantity", anchor=CENTER, width=100)

        # set hedings
        self.card_tree.heading("ISBN", text="ISBN", anchor=CENTER)
        self.card_tree.heading("Title", text="Title", anchor=CENTER)
        self.card_tree.heading("Publisher", text="Publisher", anchor=CENTER)
        self.card_tree.heading("Price", text="Price", anchor=CENTER)
        self.card_tree.heading("Quantity", text="Quantity", anchor=CENTER)

        # set tree tags
        self.card_tree.tag_configure("odd", background="white")
        self.card_tree.tag_configure("even", background="lightblue")

        # Search Frame
        card_frame = LabelFrame(self, text="Card Detail")
        card_frame.pack(fill="x", expand="yes")
        card_frame.grid_columnconfigure(1, weight=1)

        # create card label
        self.card_label = Label(card_frame, text="There is 0 Item in Shopping Card")
        self.card_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)

        # action frame
        action_frame = Frame(card_frame)
        action_frame.grid(row=0, column=1, sticky="wnes")
        action_frame.columnconfigure(0, weight=1)
        action_frame.columnconfigure(1, weight=1)

        # check Card
        checkout_button = Button(
            action_frame,
            text="Proceed",
            background="white",
            command=self.checkout,
            width=10,
        )
        checkout_button.pack(side="right")

        # delete button
        del_button = Button(
            action_frame,
            text="Delete",
            background="white",
            command=self.remove_selected_items,
            width=10,
        )
        del_button.pack(side="right", padx=5)
        self.remove_from_tree()
        self.card: Card = self.controller.user.card
        self.insert_book_item()

    def insert_book_item(self):
        for index, item in enumerate(self.card.card_items):
            if index % 2 == 0:
                self.card_tree.insert(
                    parent="",
                    index="end",
                    iid=item.id,
                    text="",
                    values=(
                        item.product.isbn,
                        item.product.title,
                        item.product.publisher,
                        item.product.price,
                        item.quantity,
                    ),
                    tags="odd",
                )

            else:
                self.card_tree.insert(
                    parent="",
                    index="end",
                    iid=item.id,
                    text="",
                    values=(
                        item.product.isbn,
                        item.product.title,
                        item.product.publisher,
                        item.product.price,
                        item.quantity,
                    ),
                    tags="even",
                )

            self.card_label.config(
                text=f"there is {len(self.card.card_items)} items in Shopping Card"
            )

    def remove_from_tree(self):
        for item in self.card_tree.get_children():
            self.card_tree.delete(item)

    def remove_selected_items(self, *args):
        selection = self.card_tree.selection()
        if (
            len(selection)
            and messagebox.askquestion(
                "askquestion", f"Are you sure deleting {len(selection)} item?"
            )
            == "yes"
        ):
            for item in selection:
                self.card_tree.delete(item)

                if self.controller.logged_in:
                    delete_card_item(int(item))

            self.remove_from_tree()
            self.card: Card = get_card(self.controller.user.id)
            self.insert_book_item()

    def checkout(self):
        if self.controller.logged_in:
            self.controller.show_frame("ConfirmPage")
        else:
            self.controller.show_frame("LoginPage")
