import pdb
import random
import select
from traceback import format_exc
from .models import *


def create_product(
    isbn: int,
    user_id: int,
    category_id: int,
    title: str,
    publisher: int,
    price: str,
    quantity: int,
    year: int,
    authors: list,
):
    try:
        query = f"""
            INSERT INTO Products (isbn,user_id,category_id,title,publisher,price,quantity,year,deleted) values(?,?,?,?,
            ?,?,?,?,0);
        """

        print(query)

        cursor.execute(
            query, [isbn, user_id, category_id, title, publisher, price, quantity, year]
        )
        sqliteConnection.commit()
        product_id = cursor.lastrowid
        authors_list = []

        for a in authors:
            if len(a.split()) > 1:
                firstname = a.split(" ")[0]
                lastname = a.split(" ")[1]
            else:
                firstname = a
                lastname = ""

            query = f"insert into Authors (product_id,firstname,lastname) values(?,?,?)"

            cursor.execute(query, [product_id, firstname, lastname])
            sqliteConnection.commit()
            authors_list.append(
                Author(cursor.lastrowid, product_id, firstname, lastname)
            )
    except:
        print(format_exc())
        return False

    return Product(
        cursor.lastrowid,
        isbn,
        user_id,
        category_id,
        title,
        publisher,
        price,
        quantity,
        year,
        0,
        authors,
    )


def update_product(
    id, category_id, title, publisher, price, quantity, year, authors: List[str]
) -> bool:
    try:
        query = f"""
                    update Products set category_id=?, title=?,
                    publisher=?,price=?,quantity=?,year=?
                    where id=?
                """
        print(query)
        cursor.execute(
            query,
            [category_id, title, publisher, price, quantity, year, id],
        )
        sqliteConnection.commit()

        query1 = "delete from Authors where product_id=?"
        cursor.execute(query1, [id])
        sqliteConnection.commit()

        for author in authors:
            query2 = "insert into Authors (product_id,firstname,lastname) values(?,?,?)"
            name = author.split(" ")
            if len(name) > 1:
                firstname = name[0]
                lastname = name[1]
            else:
                firstname = author
                lastname = ""

            cursor.execute(query2, [id, firstname, lastname])

        return True
    except:
        print(format_exc())
        return False


def get_all_user_products(user_id) -> List[Product]:
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.user_id=?
        """
        print(query)
        res = cursor.execute(query, [user_id])

        return [
            Product(
                *item[0:10],
                Category(*item[10:]),
            )
            for item in res.fetchall()
        ]
    except:
        print(format_exc())
        return False


def get_all_products():
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.deleted=0 
        """
        print(query)
        res = cursor.execute(query)

        return [
            Product(
                *item[0:10],
                Category(*item[10:]),
            )
            for item in res.fetchall()
        ]
    except:
        print(format_exc())
        return False


def get_deleted_user_products(user_id) -> List[Product]:
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.deleted=0 AND Products.user_id=?
        """
        print(query)
        res = cursor.execute(query, [user_id])

        return [
            Product(
                *item[0:10],
                Category(*item[10:]),
            )
            for item in res.fetchall()
        ]
    except:
        print(format_exc())
        return False


def get_product_by_id(product_id) -> Product:
    try:
        query = """
            SELECT * FROM Products
            LEFT JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.id=?
        """
        print(query)
        res = cursor.execute(query, [product_id])
        item = res.fetchone()

        return Product(
            *item[0:10],
            Category(*item[10:]),
        )
    except:
        print(format_exc())
        return False


def filter_product(sr) -> List[Product]:
    sr += "%"
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.deleted=0 
            AND (Products.isbn LIKE ? OR Products.title LIKE ? OR Products.publisher LIKE ?)
        """
        print(query)
        res = cursor.execute(query, [sr, sr, sr])

        return [
            Product(
                *item[0:10],
                Category(*item[10:]),
            )
            for item in res.fetchall()
        ]
    except:
        print(format_exc())
        return False


def get_single_product(id) -> Product:
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.deleted=0 AND Products.id=? LIMIT 100
        """
        print(query)
        res = cursor.execute(query, [id])
        product = res.fetchone()

        return Product(
            *product[0:10],
            Category(*product[10:]),
        )

    except:
        print(format_exc())
        return False


def update_product_quantity(id, quantity):
    try:
        query = "update Products set quantity=? where id=?"
        cursor.execute(query, [quantity, id])
        sqliteConnection.commit()
        return True
    except:
        print(format_exc())
        return False


def delete_product(id):
    try:
        query = "update Products set deleted=-1 where id=?"
        cursor.execute(query, [id])
        sqliteConnection.commit()
        return True
    except:
        print(format_exc)
        return False


def get_author_by_product(product_id) -> List[Author]:
    query = "select * from Authors where product_id=?"
    res = cursor.execute(query, [product_id])
    authors = res.fetchall()

    return [
        Author(
            *author[0:],
        )
        for author in authors
    ]
