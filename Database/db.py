import sqlite3
from Database import sql_queries

db = sqlite3.connect('Database/test.sqlite3')
cursor = db.cursor()


async def create_table():
    if db:
        print("db connected")
    cursor.execute(sql_queries.create_table_products)
    db.commit()


async def insert_product(product_id, size, quantity):
    cursor.execute(
        sql_queries.insert_product,
        (product_id, size, quantity))
    db.commit()
