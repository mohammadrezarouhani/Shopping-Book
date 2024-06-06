import sys
from traceback import format_exc
from database.card import get_card
from models import *


def create_customer(
    username: str,
    firstname: str,
    lastname: str,
    password: str,
    address: str,
    city: str,
    state: str,
) -> Customer:
    query = f"""
        INSERT INTO Users (username, firstname, lastname, password, address, city, state,role) 
        VALUES ('{username}', '{firstname}', '{lastname}', '{password}', '{address}', '{city}', '{state}','customer');
        """
    print(query)
    cursor.execute(query)
    sqliteConnection.commit()
    user_id = cursor.lastrowid
    print(["insert user result"], user_id)

    # create customer
    query2 = f"INSERT INTO Customers (user_id) VALUES ({user_id})"
    print(query2)

    cursor.execute(query2)
    sqliteConnection.commit()
    customer_id = cursor.lastrowid

    print("[customer insert id result]", customer_id)
    return Customer(
        customer_id,
        user_id,
        username,
        firstname,
        lastname,
        password,
        address,
        city,
        state,
        "customer",
    )


def update_customer(
    user_id,
    firstname: str,
    lastname: str,
    password: str,
    address: str,
    city: str,
    state: str,
) -> bool:
    try:
        query = f"""
            UPDATE Users  set firstname='{firstname}',
            lastname='{lastname}',password='{password}',address='{address}',city='{city}',state='{state}'
            WHERE id=={user_id};
            """
        print(query)
        cursor.execute(query)
        sqliteConnection.commit()
        print(["upda user success"])

        return True
    except:
        print(format_exc())
        return False


def delete_customer(user_id: int) -> bool:
    try:
        query = f'DELETE FROM Customers WHERE user_id="{user_id}"'
        print(query)
        cursor.execute(query)
        print("delete customer success")
        return True
    except:
        print(format())
        return False


def get_customer(username, password) -> Customer:
    try:
        query = (
            f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'"
        )
        print(query)

        res = cursor.execute(query)
        user = res.fetchone()

        res = cursor.execute(f'SELECT * FROM Customers WHERE user_id="{user[0]}"')
        customer = res.fetchone()
        card = get_card(res[0])
        return Customer(
            *customer,
            *user[1:],
            card
        )
    except:
        print(format_exc())
        return None


def create_admin(
    username: str,
    firstname: str,
    lastname: str,
    password: str,
    address: str,
    city: str,
    state: str,
    phone_numbers: list,
) -> Admin:
    query = f"""
        INSERT INTO Users (username, firstname, lastname, password, address, city, state,role) 
        VALUES ('{username}', '{firstname}', '{lastname}', '{password}', '{address}', '{city}', '{state}','admin');
        """
    print(query)
    cursor.execute(query)
    sqliteConnection.commit()
    user_id = cursor.lastrowid
    print(["insert user result"], user_id)

    # create customer
    query2 = f"INSERT INTO Admins (user_id) VALUES ({user_id})"
    print(query2)

    cursor.execute(query2)
    sqliteConnection.commit()
    admin_id = cursor.lastrowid

    phones = []

    for number in phone_numbers:
        query3 = (
            f"INSERT INTO PhoneNumber (number,user_id) VALUES ('{number}',{user_id})"
        )
        print(query3)
        cursor.execute(query3)
        sqliteConnection.commit()
        phone_id = cursor.lastrowid
        phones.append(Phone(phone_id, number))

    print("[customer insert id result]", admin_id)
    return Admin(
        admin_id,
        user_id,
        username,
        firstname,
        lastname,
        password,
        address,
        city,
        state,
        "customer",
        phones=phones,
    )


def update_admin(
    user_id: int,
    username: str,
    firstname: str,
    lastname: str,
    password: str,
    address: str,
    city: str,
    state: str,
    phone_numbers: list,
):
    try:
        query = f"""
                update Users set username='{username}',firstname='{firstname}',lastname='{lastname}',
                password='{password}',address='{address}',city='{city}',state='{state}'    
                where id={user_id}
        """

        cursor.execute(query)
        sqliteConnection.commit()

        query2 = f"delete from PhoneNumber where user_id={user_id}"
        cursor.execute(query2)

        phones = []

        for number in phone_numbers:
            query3 = f"INSERT INTO PhoneNumber (number,user_id) VALUES ('{number}',{user_id})"
            print(query3)
            cursor.execute(query3)
            sqliteConnection.commit()
            phone_id = cursor.lastrowid
            phones.append(Phone(phone_id, number))
    except:
        print(format_exc())
        return True


def get_admin(username, password):
    try:
        query = (
            f"SELECT * FROM Users WHERE username='{username}' AND password='{password}'"
        )
        print(query)

        res = cursor.execute(query)
        user = res.fetchone()

        res = cursor.execute(f'SELECT * FROM Admins WHERE user_id="{user[0]}"')
        admin = res.fetchone()

        return Admin(*admin, *user[1:])
    except:
        print(format_exc())
        return None
