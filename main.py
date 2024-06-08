from email.mime import image
import tkinter as tk
from tkinter import E, N, S, W, Button, Frame, ttk
from components import *
from database import *

# any page that we create should be registred here
frame_list = [
    StartPage,
    LoginPage,
    SignUpPage,
    BookListPage,
    ShoppingCardPage,
    ConfirmPage,
    UpdateProfile,
    FactorPage,
    ManageBookPage,
    SystemPage,
    ReportPage,
    BookOrderPage,
    UpdateBookPage,
    InsertBookPage,
]


# main window runner
class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Book Online Shop")
        self.geometry("800x600")
        self.resizable(0, 0)

        self.history = []
        self.logged_in = False
        self.user: Customer | Admin = None
        self.current_order_id=None
        self.current_product_id=None
        
        style = ttk.Style(self)
        style.configure("Treeview", rowheight=40)

        container = Frame(self, background="lightblue")
        container.pack(fill="both", expand=True)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=0)
        container.rowconfigure(1, weight=1)

        toolbar = Frame(container, height=5, background="lightblue")
        toolbar.grid(row=0, column=0, padx=5, pady=5)

        initil_page_button = Button(
            toolbar,
            text="main Page",
            background="white",
            foreground="green",
            command=lambda: self.show_frame("StartPage"),
        )
        initil_page_button.grid(row=0, column=0, sticky=W, padx=5)

        search_page_button = Button(
            toolbar,
            text="Book List",
            background="white",
            foreground="green",
            command=lambda: self.show_frame("BookListPage"),
        )
        search_page_button.grid(row=0, column=1, sticky=W, padx=5)

        self.frames = {}

        for F in frame_list:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

        self.show_frame("StartPage")

    def show_frame(self, page_name):

        if len(self.history) > 1:
            prev = self.history[-1]
            prev_frame = self.frames[prev]
            prev_frame.clean()

        frame = self.frames[page_name]
        frame.grid(row=1, column=0, sticky=N + W + E + S)
        frame.update_data()
        frame.tkraise()
        self.history.append(page_name)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
