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
    query = f"""
        INSERT INTO Products (isbn,user_id,category_id,title,publisher,price,quantity,year) values(?,?,?,?,
        ?,?,?,?);
    """

    print(query)

    cursor.execute(
        query,
        [isbn, user_id, category_id, title, publisher, price, quantity, year, authors],
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
        authors_list.append(Author(cursor.lastrowid, product_id, firstname, lastname))

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
    id, category_id, title, publisher, price, quantity, year, authors: List[Author]
) -> bool:
    try:
        query = f"""
                    update Products set category_id=?, title=?,
                    publisher=?,price='?,quantity='?',year='?'
                    where id=?
                """
        print(query)
        cursor.execute(
            query,
            [category_id, title, publisher, price, quantity, year, id],
        )
        sqliteConnection.commit()

        query1 = "delete from Authors where product_id=?"
        cursor.execute(query1)
        sqliteConnection.commit()

        for author in authors:
            query2 = "insert into Authors (product_id,firstname,lastname) values(?,?,?)"
            print(query2)
            cursor.execute(
                query, [author.product_id, author.firstname, author.lastname]
            )

        return True
    except:
        print(format_exc())
        return False


def get_products() -> List[Product]:
    try:
        query = """
            SELECT * FROM Products
            INNER JOIN Categoreis ON Products.category_id = Categoreis.id
            WHERE Products.deleted=0 LIMIT 100
        """
        print(query)
        res = cursor.execute(query)

        return [
            Product(
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[8],
                item[9],
                Category(item[10], item[11], item[12], item[13]),
            )
            for item in res.fetchall()
        ]
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
                item[0],
                item[1],
                item[2],
                item[3],
                item[4],
                item[5],
                item[6],
                item[7],
                item[8],
                item[9],
                Category(item[10], item[11], item[12], item[13]),
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
            product[0],
            product[1],
            product[2],
            product[3],
            product[4],
            product[5],
            product[6],
            product[7],
            product[8],
            product[9],
            Category(product[10], product[11], product[12], product[13]),
        )

    except:
        print(format_exc())
        return False
