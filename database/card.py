from traceback import format_exc
from models import *


def create_card(customer_id: int):
    pass


def get_card(customer_id) -> Card:
    try:
        query = f"""select * from Cards where customer_id={customer_id} join CardItems on Cards.id=CardItems.card_id"""
        res = cursor.execute(query)
        data = res.fetchall()

        return Card(data[0][0], data[0][1], [CardItem(item[2:]) for item in data])
    except:
        print(format_exc())
        return False


def create_card_item(card_id, product_id):
    pass


def delete_card_item(id):
    pass


def delete_cards_item(card_id):
    pass
