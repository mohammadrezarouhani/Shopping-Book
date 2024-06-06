from traceback import format_exc
from database.card import get_card
from models import *


def get_orders(id) -> Order:
    query = f"""select * from Orders where id={id} inner join OrderItems on Orders.id=OrderItems.order_id;"""
    print(query)

    res = cursor.execute(query)
    orders = res.fetchall()
    return Order(
        id=id,
        customer_id=orders[0][1],
        product_id=orders[0][2],
        order_item=[OrderItem(*item[3:]) for item in orders],
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


def create_order(customer_id) -> Order | None:
    try:
        card = get_card(customer_id)
        query = f"""insert into Orders values({card.customer_id},0)"""
        cursor.execute(query)
        sqliteConnection.commit()
        order_id = cursor.lastrowid

        order_items = []
        for c in card.card_items:
            query = f"insert into CardItems ({order_id},{c.product_id},{c.quantity})"
            cursor.execute(query)
            sqliteConnection.commit()
            order_items.append(
                OrderItem(cursor.lastrowid, order_id, c.product_id, c.quantity)
            )

        return Order(order_id, customer_id, order_items)
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
