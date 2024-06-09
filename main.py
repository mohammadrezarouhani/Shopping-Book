from email.mime import image
import tkinter as tk
from tkinter import E, N, S, W, Button, Frame, Menu, ttk
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
    InsertCategoryPage,
    UpdateCategoryPage,
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
        self.current_order_id = None
        self.current_product_id = None
        self.current_category = None

        style = ttk.Style(self)
        style.configure("Treeview", rowheight=40)

        container = Frame(self, background="lightblue")
        container.pack(fill="both", expand=True)
        container.columnconfigure(0, weight=1)
        container.rowconfigure(0, weight=0)
        container.rowconfigure(1, weight=1)

        # menu_frame
        menu_frame = Frame(container)
        menu_frame.grid(row=0, column=0, sticky="wnes")

        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)


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
        self.set_menu()

    def set_menu(self):

        self.clear_menubar()
        self.file = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file)
        self.file.add_command(label="Main Page", command=lambda:self.show_frame('StartPage'))
        
        if not self.logged_in:
            self.file.add_command(label="Continue As Guest", command=lambda:self.show_frame('BookListPage'))
            self.file.add_command(label="SignIn", command=lambda:self.show_frame('LoginPage'))
            self.file.add_command(label="SignUp", command=lambda:self.show_frame('SignUpPage'))

        elif type(self.user) == Customer:
            self.file.add_command(label="Order New Book", command=lambda:self.show_frame('BookListPage'))
            self.file.add_command(label="Profile", command=lambda:self.show_frame('UpdateProfile'))
            self.file.add_command(label="Goto Card", command=lambda:self.show_frame('ShoppingCardPage'))

        elif type(self.user) == Admin:
            self.file.add_command(label="Mange Products", command=lambda:self.show_frame('ManageBookPage'))
            self.file.add_command(label="Report", command=lambda:self.show_frame('BookOrderPage'))
            self.file.add_command(label="System Maintanace", command=lambda:self.show_frame('SystemPage'))

    def clear_menubar(self):
        self.menu_bar = Menu(self)
        self.config(menu=self.menu_bar)

if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
