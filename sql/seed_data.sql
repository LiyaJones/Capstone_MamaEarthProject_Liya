import pandas as pd

# 1. Define seed data cleanup script content
seed_sql_content = """-- Task 2: Seed Data Loading and Null Cleanup
UPDATE orders SET discount_pct = NULL WHERE discount_pct = '';
UPDATE orders SET rating = NULL WHERE rating = '';
"""

with open('sql/seed_data.sql', 'w', encoding='utf-8') as f:
    f.write(seed_sql_content.strip())

# 2. Establish database connection and re-apply schema from Cell 1 file
conn = sqlite3.connect(':memory:')
conn.execute("PRAGMA foreign_keys = ON;")

with open('sql/schema.sql', 'r', encoding='utf-8') as f:
    conn.executescript(f.read())

# 3. Load raw CSVs into DataFrames and insert into tables
customers_df = pd.read_csv('data/customers.csv')
products_df = pd.read_csv('data/products.csv')
orders_df = pd.read_csv('data/orders.csv')

customers_df.to_sql('customers', conn, index=False, if_exists='append')
products_df.to_sql('products', conn, index=False, if_exists='append')
orders_df.to_sql('orders', conn, index=False, if_exists='append')

# 4. Execute seed cleanup script
conn.executescript(seed_sql_content)

# 5. Verification checks
print("--- Task 2 Verification ---")
print("customers count:", pd.read_sql("SELECT COUNT(*) AS cnt FROM customers", conn).iloc[0]['cnt'], "(Expected: 45)")
print("products count:", pd.read_sql("SELECT COUNT(*) AS cnt FROM products", conn).iloc[0]['cnt'], "(Expected: 16)")
print("orders count:", pd.read_sql("SELECT COUNT(*) AS cnt FROM orders", conn).iloc[0]['cnt'], "(Expected: 180)")
