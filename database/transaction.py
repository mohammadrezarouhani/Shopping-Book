from .connection import *

def create_user_table():
    cursor.execute("DROP TABLE IF EXISTS Users;")
    query = """
       CREATE TABLE Users
            (
                id int primary key,
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


def create_customer_table():
    cursor.execute("DROP TABLE IF EXISTS Customers;")

    query = """CREATE TABLE Customers
            (
                id int primary key,
                user_id int,
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
                id int primary key,
                number varchar(115)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create phone table result]: {res}")


def create_admin_table():
    cursor.execute("DROP TABLE IF EXISTS PhoneNumbers;")
    query = """CREATE TABLE PhoneNumbers
            (
                id int primary key,
                phone_id int,
                FOREIGN KEY (phone_id) REFERENCES PhoneNumber(id)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create admin table result]: {res}")


def create_card_table():
    cursor.execute("DROP TABLE IF EXISTS Cards;")
    query = """CREATE TABLE Cards
            (
                id int primary key,
                customer_id int,
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
                id int primary key,
                product_id int,
                card_id int,
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
                id int primary key,
                customer_id int,
                product_id int,
                card_id int,
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
                id int primary key,
                order_id int,
                product_id int,
                quantity int,
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
                id int primary key,
                order_id int,
                product_id int,
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
                id int primary key,
                isbn int not null unique,
                user_id int,
                category_id int
                title varchar(115),
                publisher varchar(115),
                price varchar(115),
                quantity int,
                year int,
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
                id int primary key,
                product_id int,
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
                id int primary key,
                title varchar(115),
                state varchar(115),
                credit_type varchar(115)
            );
        """
    print(query)
    res = cursor.execute(query)
    print(f"[create category table result]: {res}")





def init_database():
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

if __name__=='__main__':
    init_database()
