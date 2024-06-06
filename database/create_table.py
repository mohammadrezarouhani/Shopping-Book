from models import *


def create_user_table():
    cursor.execute("DROP TABLE IF EXISTS Users;")
    query = """
       CREATE TABLE Users
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                firstname varchar(115),
                lastname varchar(115),
                username varchar(115) not null unique,
                password varchar(115),
                address varchar(512),
                city varchar(115),
                state carchar(115),
                role varchar(115)
            );
        """

    print(query)
    res = cursor.execute(query)
    print(f"[create user table result]: {res}")


def create_admin_table():
    cursor.execute("DROP TABLE IF EXISTS Customers;")

    query = """CREATE TABLE Customers
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """

    print(query)
    res = cursor.execute(query)
    print(f"[create customer table result]: {res}")


def create_customer_table():
    cursor.execute("DROP TABLE IF EXISTS Customers;")

    query = """CREATE TABLE Customers
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """

    print(query)
    res = cursor.execute(query)
    print(f"[create customer table result]: {res}")


def create_phone_table():
    cursor.execute("DROP TABLE IF EXISTS PhoneNumber;")
    query = """CREATE TABLE PhoneNumber
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               user_id INTEGER,
               number varchar(115),
               FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create phone table result]: {res}")


def create_admin_table():
    cursor.execute("DROP TABLE IF EXISTS Admins;")
    query = """CREATE TABLE Admins
            (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create admin table result]: {res}")


def create_card_table():
    cursor.execute("DROP TABLE IF EXISTS Cards;")
    query = """CREATE TABLE Cards
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES Customers(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create card table result]: {res}")


def create_card_item_table():
    cursor.execute("DROP TABLE IF EXISTS CardItems;")
    query = """CREATE TABLE CardItems
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                card_id INTEGER,
                FOREIGN KEY (product_id) REFERENCES Cards(id)
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create card item table result]: {res}")


def create_order_table():
    cursor.execute("DROP TABLE IF EXISTS Orders;")
    query = """CREATE TABLE Orders
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER,
                product_id INTEGER,
                card_id INTEGER,
                submit INTEGER,
                FOREIGN KEY (product_id) REFERENCES Cards(id)
                FOREIGN KEY (customer_id) REFERENCES Customers(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create order table result]: {res}")


def create_order_item_table():
    cursor.execute("DROP TABLE IF EXISTS OrderItems;")
    query = """CREATE TABLE OrderItems
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                quantity INTEGER,
                FOREIGN KEY (order_id) REFERENCES Orders(id)
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create order item table result]: {res}")


def create_review_table():
    cursor.execute("DROP TABLE IF EXISTS Reviews;")
    query = """CREATE TABLE Reviews
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_id INTEGER,
                product_id INTEGER,
                FOREIGN KEY (order_id) REFERENCES Orders(id)
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create review table result]: {res}")


def create_product_table():
    cursor.execute("DROP TABLE IF EXISTS Products;")
    query = """CREATE TABLE Products
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                isbn int not null unique,
                user_id INTEGER,
                category_id int
                title varchar(115),
                publisher varchar(115),
                price varchar(115),
                quantity INTEGER,
                year INTEGER,
                deleted INTEGER,
                FOREIGN KEY (user_id) REFERENCES Users(id)
                FOREIGN KEY (category_id) REFERENCES Categoreis(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create product table result]: {res}")


def create_author_table():
    cursor.execute("DROP TABLE IF EXISTS Authors;")
    query = """CREATE TABLE Authors
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_id INTEGER,
                firstname varchar(115),
                lastname varchar(115),
                FOREIGN KEY (product_id) REFERENCES Products(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create author table result]: {res}")


def create_category_table():
    cursor.execute("DROP TABLE IF EXISTS Categoreis;")
    query = """CREATE TABLE Categoreis
            (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
                title varchar(115),
                state varchar(115),
                credit_type varchar(115)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create category table result]: {res}")


def init_database():
    create_admin_table()
    create_user_table()
    create_customer_table()
    create_phone_table()
    create_admin_table()
    create_category_table()
    create_product_table()
    create_author_table()
    create_review_table()
    create_card_table()
    create_card_item_table()
    create_order_table()
    create_order_item_table()


if __name__ == "__main__":
    create_phone_table()
    create_admin_table()