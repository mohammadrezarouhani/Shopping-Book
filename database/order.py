from time import sleep
from traceback import format_exc
from database.card import get_card
from database.product import get_product_by_id, get_products, update_product_quantity
from database.users import get_customer_by_id
from .models import *


def get_orders(id) -> Order:
    query = f"""
        select * from Orders
        inner join OrderItems on Orders.id=OrderItems.order_id
        inner join Products on OrderItems.product_id=Products.id
        inner join Categoreis on Products.category_id=Categoreis.id
        where Orders.id=?
    """
    print(query)

    res = cursor.execute(query, [id])
    orders = res.fetchall()
    customer = get_customer_by_id(orders[0][1])

    return Order(
        id=orders[0][0],
        customer_id=orders[0][1],
        admin_id=orders[0][2],
        amount=orders[0][3],
        credit_card=orders[0][4],
        order_item=[
            OrderItem(
                item[5],
                item[6],
                item[7],
                item[8],
                Product(
                    item[9],
                    item[10],
                    item[11],
                    item[12],
                    item[13],
                    item[14],
                    item[15],
                    item[16],
                    item[17],
                    item[18],
                    category=Category(item[20], item[21], item[21], item[22]),
                ),
            )
            for item in orders
        ],
        customer=customer,
    )


def update_order(id, submit: int) -> bool:
    try:
        query = f"""update Order set submit={submit} where id={id}"""
        cursor.execute(query)
        sqliteConnection.commit()
        return True
    except:
        print(format_exc())
        return False


def create_order(user_id: int, amount: int, credit_card: str, admin_id) -> Order:
    try:
        card = get_card(user_id)
        query = f"""insert into Orders (user_id,submit,admin_id,amount,credit_card) values(?,?,?,?,?)"""
        print(query)
        cursor.execute(query, [user_id, 0, admin_id, amount, credit_card])
        sqliteConnection.commit()
        order_id = cursor.lastrowid

        order_items = []
        for c in card.card_items:
            query = (
                f"insert into OrderItems (order_id,product_id,quantity) values(?,?,?)"
            )
            cursor.execute(query, [order_id, c.product_id, c.quantity])
            sqliteConnection.commit()
            update_product_quantity(c.product_id, c.product.quantity - c.quantity)
            product = get_product_by_id(c.product_id)

            order_items.append(
                OrderItem(cursor.lastrowid, order_id, c.product_id, c.quantity, product)
            )

        return Order(order_id, user_id, 0, admin_id, amount, credit_card, order_items)
    except:
        print(format_exc())
        return False


def create_order_item(order_id, product_id, quantity):
    try:
        query = f"""insert into OrderItems ('{order_id}','{product_id}','{quantity}')"""
        cursor.execute(query)
        sqliteConnection.commit()
        return OrderItem(cursor.lastrowid, product_id, quantity)
    except:
        print(format_exc())
        return False
