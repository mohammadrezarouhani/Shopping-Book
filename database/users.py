import pdb
from sqlite3 import IntegrityError
import sys
from traceback import format_exc
from database.card import create_card, get_card
from .models import *


def create_customer(
    username: str,
    firstname: str,
    lastname: str,
    password: str,
    address: str,
    city: str,
    state: str,
    zip_code,
    credit_type,
    credit_card,
    credit_expire_date,
) -> Customer:
    try:
        query = f"""
            INSERT INTO Users (username, firstname, lastname, password, address, city, state,zip_code,role) 
            VALUES (?, ?,?,?, ?, ?, ?,?,'customer');
            """
        print(query)
        cursor.execute(
            query,
            [username, firstname, lastname, password, address, city, state, zip_code],
        )
        sqliteConnection.commit()
        user_id = cursor.lastrowid
        print(["insert user result"], user_id)

        # create customer
        query2 = f"INSERT INTO Customers (user_id,credit_type,credit_card,credit_expire_date) VALUES (?,?,?,?)"
        print(query2)

        cursor.execute(query2, [user_id, credit_type, credit_card, credit_expire_date])
        sqliteConnection.commit()
        customer_id = cursor.lastrowid

        print("[customer insert id result]", customer_id)
        card = create_card(user_id)

        return Customer(
            customer_id,
            user_id,
            credit_type,
            credit_card,
            credit_expire_date,
            username,
            firstname,
            lastname,
            password,
            address,
            city,
            state,
            zip_code,
            "customer",
            card,
        )
    except IntegrityError as e:
        raise e
    except:
        print(format_exc())
        return False


def update_customer(
    user_id,
    firstname: str,
    lastname: str,
    address: str,
    city: str,
    state: str,
    zip_code,
    credit_type,
    credit_card,
    credit_expire_date,
) -> bool:
    try:
        query = f"""
            UPDATE Users  set firstname=?,
            lastname=?,address=?,city=?,state=?,zip_code=?
            WHERE id=?;
            """
        print(query)
        cursor.execute(
            query,
            [firstname, lastname, address, city, state, zip_code, user_id],
        )
        sqliteConnection.commit()

        query2 = (
            """update Customers set credit_type=?,credit_card=?,credit_expire_date=?"""
        )
        print(query2)
        cursor.execute(query2, [credit_type, credit_card, credit_expire_date])
        sqliteConnection.commit()
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


def get_customer_by_id(id) -> Customer:
    try:
        query = f"SELECT * FROM Users WHERE id=?"
        print(query)

        res = cursor.execute(query, [id])
        user = res.fetchone()

        res = cursor.execute(f"SELECT * FROM Customers WHERE user_id=?", [user[0]])
        customer = res.fetchone()
        card = get_card(user[0])

        return Customer(*customer, *user[1:], card)
    except:
        print(format_exc())
        return None


def get_user(username, password) -> Customer | Admin:
    try:
        query = f"SELECT * FROM Users WHERE username=? AND password=?"
        print(query)

        res = cursor.execute(query, [username, password])
        user = res.fetchone()
        if user[-1] == "customer":
            res = cursor.execute(f"SELECT * FROM Customers WHERE user_id=?", [user[0]])
            customer = res.fetchone()
            card = get_card(user[0])
            return Customer(*customer, *user[1:], card)
        else:
            res = cursor.execute(f"SELECT * FROM Admins WHERE user_id=?", [user[0]])
            admin = res.fetchone()
            return Admin(*admin, *user[1:])
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
    zip_code: str,
    phone_numbers: list,
) -> Admin:
    query = f"""
        INSERT INTO Users (username, firstname, lastname, password, address, city, state,zip_code,role) 
        VALUES (?, ?, ?, ?, ?, ?, ?,?,'admin');
        """
    print(query)
    cursor.execute(
        query, [username, firstname, lastname, password, address, city, state, zip_code]
    )
    sqliteConnection.commit()
    user_id = cursor.lastrowid
    print(["insert user result"], user_id)

    # create customer
    query2 = f"INSERT INTO Admins (user_id) VALUES (?)"
    print(query2)

    cursor.execute(query2, [user_id])
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


def get_admin(username, password) -> Admin:
    try:
        query = f"SELECT * FROM Users WHERE username=? AND password=?"
        print(query)

        res = cursor.execute(query, [username, password])
        user = res.fetchone()

        res = cursor.execute(f"SELECT * FROM Admins WHERE user_id=?", [user[0]])
        admin = res.fetchone()

        return Admin(*admin, *user[1:])
    except:
        print(format_exc())
        return None


def get_admin_by_id(id) -> Admin:
    try:
        query = f"SELECT * FROM Users WHERE id=?"
        print(query)

        res = cursor.execute(query, [id])
        user = res.fetchone()

        res = cursor.execute(f'SELECT * FROM Admins WHERE user_id="{user[0]}"')
        admin = res.fetchone()

        return Admin(*admin, *user[1:])
    except:
        print(format_exc())
        return None


def update_user_password(user_id, password):
    try:
        query = "update Users set password=? where id=?"
        print(query)
        cursor.execute(query, [password, user_id])
        sqliteConnection.commit()
        return True
    except:
        print(format_exc())
        return False
