create_table_products = '''
        CREATE TABLE IF NOT EXISTS products_2(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id TEXT,
        size TEXT,
        quantity TEXT
        )
'''

insert_product = '''
INSERT INTO products_2(product_id, size, quantity) VALUES(?,?,?)
'''

