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
class Category:
    id: int
    title: str
    state: str
    credit_type: str


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
    deleted: bool
    category: Category


@dataclass
class CardItem:
    id: int
    product_id: int
    card_id: int
    quantity: int
    product: Optional[Product] = None


@dataclass
class Card:
    id: Optional[int] = None
    customer_id: Optional[int] = None
    card_items: List[CardItem] = field(default_factory=list)


@dataclass
class Customer:
    id: Optional[int] = None
    user_id: Optional[int] = None
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    role: Optional[str] = None
    card: Optional[Card] = None


@dataclass
class OrderItem:
    id: int
    order_id: int
    product_id: int
    quantity: int


@dataclass
class Order:
    id: int
    customer_id: int
    order_item: List[OrderItem] = field(default_factory=list)


@dataclass
class Review:
    id: int
    order_id: int
    product_id: int


@dataclass
class Author:
    id: int
    product_id: int
    firstname: str
    lastname: str
