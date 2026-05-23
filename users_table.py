import sqlite3

conn = sqlite3.connect("orders.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    billing_email TEXT UNIQUE,
    user_name TEXT
)
""")

cursor.execute("""
INSERT OR IGNORE INTO users (billing_email, user_name)
SELECT DISTINCT
    billing_email,
    billing_name
FROM
    orders
""")

conn.commit()
conn.close()

print("users 完了")
