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
    id: Optional[int] = None
    user_id: Optional[int] = None
    username: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    password: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    role: Optional[str] = None
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
    credit_type: Optional[str] = None
    credit_card: Optional[str] = None
    credit_expire_date: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    role: Optional[str] = None
    card: Optional[Card] = None


@dataclass
class OrderItem:
    id: int
    order_id: int
    product_id: int
    quantity: int
    product: Optional[Product] = None


@dataclass
class Order:
    id: int
    customer_id: int
    submitted: Optional[int] = None
    admin_id: Optional[int] = None
    amount: Optional[str] = None
    credit_card: Optional[str] = None
    purchase_data: Optional[float] = None
    deliver_data: Optional[float] = None
    order_item: List[OrderItem] = field(default_factory=list)
    customer: Optional[Customer] = None


@dataclass
class MainOrder:
    id: int
    customer_id: int
    submitted: Optional[int] = None
    admin_id: Optional[int] = None
    amount: Optional[str] = None
    credit_card: Optional[str] = None
    customer: Optional[Customer] = None


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


@dataclass
class CategoryLastMonth:
    title: str
    amount: float


@dataclass
class CategoryRecordsNumber:
    title: str
    number: int


@dataclass
class TopSellers:
    name: str
    income: str

@dataclass
class ExpensiveBook:
    category: str
    book_title: str
    price: str
@dataclass
class SaleCustomerAvg:
    username:str
    amount:str
@dataclass
class ProductNumPerSale:
    title:str
    number:int