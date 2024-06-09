import pdb
from time import sleep
from traceback import format_exc
from database.card import get_card
from database.product import get_product_by_id, update_product_quantity
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
        orders[0][0],
        orders[0][1],
        orders[0][2],
        orders[0][3],
        orders[0][4],
        orders[0][5],
        orders[0][6],
        orders[0][7],
        order_item=[
            OrderItem(
                *item[8:12],
                Product(
                    *item[12:22],
                    category=Category(*item[22:]),
                ),
            )
            for item in orders
        ],
        customer=customer,
    )


def update_order(order_id: int, submit: int, admin_id) -> bool:
    try:
        query = "update Orders set submit=?,admin_id=? where id=?"
        cursor.execute(query, [submit, admin_id, order_id])
        sqliteConnection.commit()
        return True
    except:
        print(format_exc())
        return False


def create_order(
    user_id: int, amount: int, credit_card: str, admin_id, deliver_date, purchace_date
) -> Order:
    try:
        card = get_card(user_id)
        query = f"""
            insert into Orders 
            (user_id,submit,admin_id,amount,credit_card,deliver_date,purchase_date) values(?,?,?,?,?,?,?)
        """
        print(query)
        cursor.execute(
            query,
            [user_id, 0, admin_id, amount, credit_card, deliver_date, purchace_date],
        )
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


def get_all_orders() -> List[MainOrder]:
    query = f"""
        select * from Orders
        inner join Customers on Orders.user_id=Customers.user_id
        inner join Users on Customers.user_id=Users.id order by cast(Orders.amount as float) desc
    """
    print(query)
    res = cursor.execute(query)
    orders = res.fetchall()
    order_list = []

    for order in orders:
        order_list.append(MainOrder(*order[0:8], Customer(*order[8:13], *order[14:])))
    return order_list


def get_order_by_customer_username(username) -> List[MainOrder]:
    query = f"""
        select * from Orders
        inner join Customers on Orders.user_id=Customers.user_id
        inner join Users on Customers.user_id=Users.id
        where Users.username like ?
        order by cast(Orders.amount as float) desc
    """
    print(query)
    res = cursor.execute(query, [username + "%"])
    orders = res.fetchall()
    order_list = []
    for order in orders:
        order_list.append(MainOrder(*order[0:8], Customer(*order[8:13], *order[14:])))

    return order_list
