from sqlalchemy import create_engine
import pandas as pd

# PostgreSQL connection
engine = create_engine(
    "postgresql://postgres@localhost:5432/ecommerce"
)

# Load customers
customers_df = pd.read_csv("data/raw/customers.csv")

customers_df.to_sql(
    "customers",
    engine,
    if_exists="append",
    index=False
)

print("customers loaded successfully")

# Load products
products_df = pd.read_csv("data/raw/products.csv")

products_df.to_sql(
    "products",
    engine,
    if_exists="append",
    index=False
)

print("products loaded successfully")

# Load orders
orders_df = pd.read_csv("data/raw/orders.csv")

orders_df.to_sql(
    "orders",
    engine,
    if_exists="append",
    index=False
)

print("orders loaded successfully")