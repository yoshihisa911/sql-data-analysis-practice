import sqlite3
import csv

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY,
    billing_name TEXT,
    billing_address TEXT,
    billing_phone TEXT,
    billing_email TEXT,
    shipping_name TEXT,
    shipping_address TEXT,
    shipping_phone TEXT,
    shipping_email TEXT,
    product_name TEXT,
    quantity INTEGER,
    material_code TEXT,
    amount INTEGER,
    ip_address TEXT,
    class_c TEXT,
    session_cookie TEXT,
    card_brand TEXT,
    fraud TEXT
)
""")

with open("orders.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)

    for row in reader:
        try:
            cursor.execute("""
            INSERT INTO orders VALUES (
                ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?
            )
            """, row)

        except sqlite3.IntegrityError:
            pass

conn.commit()
conn.close()

print("完了")
