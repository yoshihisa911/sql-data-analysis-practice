import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    billing_email TEXT,
    payment_method TEXT,
    card_brand TEXT
)
""")

cursor.execute("""
INSERT INTO payments (billing_email, payment_method, card_brand)
SELECT DISTINCT
    billing_email,
    'credit_card',
    card_brand
FROM
    orders
""")

conn.commit()
conn.close()

print("payments 完了")
