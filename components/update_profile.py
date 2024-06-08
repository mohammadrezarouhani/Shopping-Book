import pdb
from tkinter import Button, Entry, Label, LabelFrame, StringVar, ttk
from tkinter import messagebox

from database import Customer
from database.users import (
    get_admin_by_id,
    get_user,
    get_customer_by_id,
    update_admin,
    update_customer,
    update_user_password,
)

from .main_frame import MainFrame
from .datetime_entry import DateEntry


class UpdateProfile(MainFrame):
    def init(self):
        if self.controller.logged_in:
            self.user: Customer = self.controller.user
            self.main_label = Label(
                self, text="Update Profile", font=("Arial", 16, "bold")
            )
            self.main_label.pack(fill="x", expand=True)

            credential_frame = LabelFrame(
                self, text="Credentials", font=("Arial", 14, "bold")
            )
            credential_frame.pack(fill="x", expand="yes")
            credential_frame.columnconfigure(0, weight=0)
            credential_frame.columnconfigure(1, weight=0)
            credential_frame.columnconfigure(2, weight=0)
            credential_frame.columnconfigure(3, weight=0)

            # username
            self.username = StringVar()
            self.username.set(self.user.username)
            username_label = Label(credential_frame, text="username", width=10)
            username_entry = Entry(
                credential_frame, textvariable=self.username,state='disabled'
            )
            username_label.grid(row=0, column=0)
            username_entry.grid(row=0, column=1, pady=5, padx=5)

            # password
            self.password = StringVar()
            pass_label = Label(credential_frame, text="password", width=10)
            pass_entry = Entry(credential_frame, textvariable=self.password)
            pass_label.grid(row=1, column=0)
            pass_entry.grid(row=1, column=1, pady=5, padx=5)

            # password retype
            self.password_retype = StringVar()
            re_pass_label = Label(
                credential_frame,
                text="password retype",
                width=15,
            )
            re_pass_entry = Entry(
                credential_frame,
                textvariable=self.password_retype,
            )
            re_pass_label.grid(row=1, column=2)
            re_pass_entry.grid(row=1, column=3, pady=5, padx=5)

            ## name frame
            name_frame = LabelFrame(self, text="FullName", font=("Arial", 14, "bold"))
            name_frame.pack(expand="yes", fill="x")
            name_frame.columnconfigure(0, weight=0)
            name_frame.columnconfigure(1, weight=0)
            name_frame.columnconfigure(2, weight=0)
            name_frame.columnconfigure(3, weight=0)

            # first name
            self.firstname = StringVar()
            self.firstname.set(self.user.firstname)
            firstname_label = Label(name_frame, text="firstname", width=10)
            firstname_entry = Entry(name_frame, textvariable=self.firstname)
            firstname_label.grid(row=0, column=0)
            firstname_entry.grid(row=0, column=1, pady=5, padx=5)

            # last name
            self.lastname = StringVar()
            self.lastname.set(self.user.lastname)
            lastname_label = Label(name_frame, text="lastname", width=10)
            lastname_entry = Entry(name_frame, textvariable=self.lastname)
            lastname_label.grid(row=0, column=2)
            lastname_entry.grid(row=0, column=3, pady=5, padx=5)

            # address frame
            address_frame = LabelFrame(
                self, text="Addres Detail", font=("Arial", 14, "bold")
            )
            address_frame.pack(fill="x", expand="yes")
            address_frame.columnconfigure(0, weight=0)
            address_frame.columnconfigure(1, weight=0)
            address_frame.columnconfigure(2, weight=0)
            address_frame.columnconfigure(3, weight=0)

            # address
            self.address = StringVar()
            self.address.set(self.user.address)
            address_label = Label(address_frame, text="address", width=10)
            address_entry = Entry(address_frame, textvariable=self.address)
            address_label.grid(row=0, column=0)
            address_entry.grid(row=0, column=1, pady=5, padx=5)

            # city
            self.city = StringVar()
            self.city.set(self.user.city)
            city_label = Label(address_frame, text="city", width=10)
            city_entry = Entry(address_frame, textvariable=self.city)
            city_label.grid(row=0, column=2)
            city_entry.grid(row=0, column=3, pady=5, padx=5)

            # state
            self.state = StringVar()
            self.state.set(self.user.state)
            state_label = Label(address_frame, text="state", width=10)
            state_entry = Entry(address_frame, textvariable=self.state)
            state_label.grid(row=1, column=0)
            state_entry.grid(row=1, column=1, pady=5, padx=5)

            # zip code
            self.zip_code = StringVar()
            self.zip_code.set(self.user.zip_code)
            zip_label = Label(address_frame, text="Credit Card", width=10)
            zip_entry = Entry(address_frame, textvariable=self.zip_code)
            zip_label.grid(row=1, column=2)
            zip_entry.grid(row=1, column=3, pady=5, padx=5)

            # credit card frame
            credit_frame = LabelFrame(
                self, text="Credit Card Detail", font=("Arial", 14, "bold")
            )
            credit_frame.pack(fill="x", expand="yes")
            credit_frame.columnconfigure(0, weight=0)
            credit_frame.columnconfigure(1, weight=0)
            credit_frame.columnconfigure(2, weight=0)
            credit_frame.columnconfigure(3, weight=0)

            # credit card type
            self.credit_type = StringVar()
            self.credit_type.set(self.user.credit_type)
            type_label = Label(credit_frame, text="Card Type")
            type_entry = Entry(credit_frame, textvariable=self.credit_type)
            type_label.grid(row=0, column=0, pady=5, padx=5)
            type_entry.grid(row=0, column=1, pady=5, padx=5)

            # credit number
            self.credit_card = StringVar()
            self.credit_card.set(self.user.credit_card)
            card_num_label = Label(credit_frame, text="Credit Number:", width=12)
            card_num_entry = Entry(credit_frame, textvariable=self.credit_card)
            card_num_label.grid(row=0, column=2, pady=5, padx=5)
            card_num_entry.grid(row=0, column=3, pady=5, padx=5)

            date = self.user.credit_expire_date.split("/")
            self.datetime_entry = DateEntry(
                credit_frame, year="00", month=date[0], day=date[1]
            )
            self.datetime_entry.grid(row=0, column=4, padx=5, pady=5)

            submit_button = Button(
                self,
                text="Update",
                background="white",
                foreground="green",
                command=self.update_profile,
            )
            submit_button.pack(fill="x", expand="yes", padx=200)

    def update_profile(self):
        for i in range(1):
            if not self.firstname.get() or not self.lastname.get():
                pdb.set_trace()
                messagebox.showerror(
                    title="name",
                    message="firstname and last name must not be empty",
                )
                break
            elif not self.address.get():
                messagebox.showerror(
                    title="address", message="address must not be empty"
                )
                break

            elif not self.city.get():
                messagebox.showerror(title="city", message="city must not be empty")
                break

            elif not self.zip_code.get():
                messagebox.showerror(
                    title="zip_code", message="zip_code must not be empty"
                )
                break

            elif not self.credit_type.get():
                messagebox.showerror(
                    title="credit_type", message="credit_type must not be empty"
                )
                break

            elif not self.credit_card.get():
                messagebox.showerror(
                    title="credit_card", message="credit_card must not be empty"
                )
                break

            elif not self.datetime_entry.get():
                messagebox.showerror(
                    title="expire date", message="card expire date must not be empty"
                )
                break

            if (
                self.password.get()
                and self.password.get() == self.password_retype.get()
            ):
                update_user_password(user_id=self.user.id, password=self.password.get())

            if type(self.user) == Customer:
                res = update_customer(
                    self.user.user_id,
                    self.firstname.get(),
                    self.lastname.get(),
                    self.address.get(),
                    self.city.get(),
                    self.state.get(),
                    self.zip_code.get(),
                    self.credit_type.get(),
                    self.credit_card.get(),
                    "/".join(self.datetime_entry.get()),
                )
                self.controller.user = get_customer_by_id(self.user.user_id)

                messagebox.showinfo(title="success", message="updating user success!")
                prev = self.controller.history[-2]
                self.controller.show_frame(prev)
            else:
                res = update_admin(
                    self.user.user_id,
                    self.firstname.get(),
                    self.lastname.get(),
                    self.address.get(),
                    self.city.get(),
                    self.state.get(),
                    [],
                )
                messagebox.showinfo(title="success", message="updating user success!")

                self.controller.user = get_admin_by_id(self.user.user_id)
