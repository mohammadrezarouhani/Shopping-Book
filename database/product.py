from traceback import format_exc
from models import *


def create_product(isbn, user_id, category_id, title, publisher, price, quantity, year):
    query = f"""
        INSERT INTO PRODUCT ('{isbn}','{user_id}','{category_id}','{title}',
        '{publisher}','{price}','{quantity}','{year}',0)
    """

    print(query)

    cursor.execute(query)
    sqliteConnection.commit()
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
    )


def update_product(id, category_id, title, publisher, price, quantity, year) -> bool:
    try:
        query = f"""
                    update Products set category_id={category_id}, title='{title}',
                    publisher='{publisher}',price='{price},quantity='{quantity}',year='{year}'
                    where id={id}
                """
        print(query)
        cursor.execute(query)
        sqliteConnection.commit()

        return True
    except:
        print(format_exc())
        return False


def get_products() -> List[Product] | bool:
    try:
        query = """select * from Products where deleted!=1"""
        res = cursor.execute(query)
        return [Product(*item) for item in res.fetchall()]
    except:
        print(format_exc())
        return False
