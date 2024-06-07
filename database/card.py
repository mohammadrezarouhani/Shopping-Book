from traceback import format_exc
from .models import *


def create_card(user_id: int) -> Card:
    try:
        query = f"insert into Cards (user_id) values({user_id})"
        print(query)
        cursor.execute(query)
        sqliteConnection.commit()
        card_id = cursor.lastrowid
        return Card(card_id, user_id, [])
    except:
        print(format_exc())
        return False


def get_card(customer_id) -> Card:
    try:
        query = f"""
            select * from Cards 
            left join CardItems on Cards.id=CardItems.card_id 
            left join Products on CardItems.product_id=Products.id 
            left join Categoreis on Products.category_id=Categoreis.id
            where Cards.user_id=? 
        """
        res = cursor.execute(query, [customer_id])
        data = res.fetchall()
        card_items = []

        for item in data:
            if item[2]!=None:
                card_items.append(
                    CardItem(
                        item[2],
                        item[3],
                        item[4],
                        item[5],
                        Product(
                            item[6],
                            item[7],
                            item[8],
                            item[9],
                            item[10],
                            item[11],
                            item[12],
                            item[13],
                            item[14],
                            item[15],
                            Category(
                                item[16],
                                item[17],
                                item[18],
                                item[19],
                            ),
                        ),
                    )
                )

        return Card(data[0][0], data[0][1], card_items)
    except:
        print(format_exc())
        return False


def create_card_item(card_id, product_id, quantity) -> CardItem | bool:
    try:
        query = f"insert into CardItems (card_id,product_id,quantity) values({card_id},{product_id},{quantity})"
        cursor.execute(query)
        sqliteConnection.commit()
        card_id = cursor.lastrowid
        return CardItem(cursor.lastrowid, product_id, card_id, quantity)
    except:
        print(format_exc())
        return False


def delete_card_item(item_id, card_id) -> List[CardItem]:
    try:
        query = f"delete from CardItems where id={item_id}"
        cursor.execute(query)
        sqliteConnection.commit()
        card_id = cursor.lastrowid

        query2 = f"select * from CardItems where card_id={card_id}"
        res = cursor.execute(query)
        items = res.fetchall()

        return [CardItem(item[0], item[1], item[2], item[3]) for item in items]
    except:
        print(format_exc())
        return False


def clear_card_item(card_id):
    try:
        query = f"delete from Card where card_id={id}"
        cursor.execute(query)
        sqliteConnection.commit()
        return True
    except:
        return False
