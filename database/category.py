import pdb
from tkinter.messagebox import RETRY
from traceback import format_exc
from .models import *


def get_categoreis() -> List[Category]:
    query = f"select * from Categoreis "
    print(query)
    res = cursor.execute(query)
    categoreis = res.fetchall()

    return [Category(*category) for category in categoreis]


def get_category(id) -> Category:
    query = f"select * from Categoreis where id=?"
    print(query)
    res = cursor.execute(query, [id])
    category = res.fetchone()

    return Category(*category)


def get_category_by_title(title) -> Category:
    query = f"select * from Categoreis where title=?"
    print(query)
    res = cursor.execute(query, [title])
    category = res.fetchone()

    return Category(*category)


def filter_category(title: str):
    try:
        query = f"select * from Categoreis where title like ?"
        print(query)
        res = cursor.execute(query, [title + "%"])
        categoreis = res.fetchall()
        return [Category(*category) for category in categoreis]
    except:
        print(format_exc())
        return False


def create_category(title, state, credit_type):
    try:
        query = f"insert into Categoreis (title,state,credit_type) values(?,?,?)"
        print(query)
        cursor.execute(query, [title, state, credit_type])
        sqliteConnection.commit()
        return Category(cursor.lastrowid, title, state, credit_type)
    except:
        print(format_exc())
        return False


def update_category(id, title, state, credit_type):
    try:
        query = "update Categoreis set title=?,state=?,credit_type=? where id=?"
        print(query)
        cursor.execute(query, [title, state, credit_type, id])
        sqliteConnection.commit()
        return Category(id, title, state, credit_type)

    except:
        return False


def delete_category(id):
    try:
        query = "delete from Categoreis where id=?"
        cursor.execute(query, [id])
        sqliteConnection.commit()
        return True
    except:
        print(format_exc())
        return False