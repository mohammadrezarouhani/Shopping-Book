import sqlite3
from dataclasses import dataclass, field, asdict
from typing import List, Optional

sqliteConnection = sqlite3.connect("sql.db")
cursor = sqliteConnection.cursor()


@dataclass
class Phone:
    id: int
    number: str = field(default_factory="")


@dataclass
class Admin:
    id: int
    username: str
    admin_id: int
    firstname: str = None
    lastname: str = None
    password: str = None
    address: str = None
    city: str = None
    state: str = None
    role: str = None
    phones: Optional[List[Phone]] = None


@dataclass
class Customer:
    id: int
    user_id: int
    username: str
    firstname: str = None
    lastname: str = None
    password: str = None
    address: str = None
    city: str = None
    state: str = None
    role: str = None


@dataclass
class Card:
    id: int
    customer_id: int


@dataclass
class CardItem:
    id: int
    product_id: int
    card_id: int


@dataclass
class Order:
    id: int
    customer_id: int
    product_id: int
    card_id: int


@dataclass
class OrderItem:
    id: int
    order_id: int
    product_id: int
    quantity: int


@dataclass
class Review:
    id: int
    order_id: int
    product_id: int


@dataclass
class Product:
    id: int
    isbn: int
    user_id: int
    category_id: int
    title: str
    publisher: str
    price: str
    quantity: int
    year: int


@dataclass
class Author:
    id: int
    product_id: int
    firstname: str
    lastname: str


@dataclass
class Category:
    id: int
    title: str
    state: str
    credit_type: str