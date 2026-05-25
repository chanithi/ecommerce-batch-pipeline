from faker import Faker
import pandas as pd
import random

fake = Faker()

customers = []

for i in range(1, 101):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "city": fake.city()
    })

customers_df = pd.DataFrame(customers)

customers_df.to_csv(
    "data/raw/customers.csv",
    index=False
)

print("customers.csv generated successfully")

products = []

categories = [
    "Electronics",
    "Clothing",
    "Books",
    "Home",
    "Sports"
]

for i in range(1, 51):
    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "category": random.choice(categories),
        "price": round(random.uniform(10, 500), 2)
    })

products_df = pd.DataFrame(products)

products_df.to_csv(
    "data/raw/products.csv",
    index=False
)

print("products.csv generated successfully")

orders = []

for i in range(1, 1001):
    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 100),
        "product_id": random.randint(1, 50),
        "quantity": random.randint(1, 5),
        "order_date": fake.date_between(
            start_date="-90d",
            end_date="today"
        )
    })

orders_df = pd.DataFrame(orders)

orders_df.to_csv(
    "data/raw/orders.csv",
    index=False
)

print("orders.csv generated successfully")