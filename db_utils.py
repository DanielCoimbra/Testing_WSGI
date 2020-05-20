# db_utils.py
import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'music_store.db')

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def create_customer(con, TrackId):
    sql = """
        UPDATE Tracks   (first_name, last_name)
        VALUES (?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (first_name, last_name))
    return cur.lastrowid

def create_order(con, customer_id, date):
    sql = """
        INSERT INTO orders (customer_id, date)
        VALUES (?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (customer_id, date))
    return cur.lastrowid

def create_lineitem(con, order_id, product_id, qty, total):
    sql = """
        INSERT INTO linitems
            (order_id, product_id, quantity, total)
        VALUES (?, ?, ?, ?)"""
    cur = con.cursor()
    cur.execute(sql, (order_id, product_id, qty, total))
    return cur.lastrowid
