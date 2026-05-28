# import pandas as pd
# import logging

# def transform_data():
#     logging.info("Starting transformation")

#     df = pd.read_csv("data/processed/cleaned_data.csv")

#     df["total_price"] = df["quantity"] * df["price"]

#     df.to_csv("data/processed/transformed_data.csv", index=False)

#     logging.info("Transformation completed")
import pandas as pd
from scripts.database import engine


def transform_customers():
    # Read staging data
    query = "SELECT * FROM stg_customers"
    df = pd.read_sql(query, engine)

    # Create full_name
    df["full_name"] = df["first_name"] + " " + df["last_name"]

    # Select final columns
    final_df = df[
        ["customer_id", "full_name", "email", "country"]
    ]

    # Load into dimension table
    final_df.to_sql(
        "dim_customers",
        engine,
        if_exists="replace",
        index=False
    )

    print("dim_customers loaded successfully")


def transform_products():
    query = "SELECT * FROM stg_products"
    df = pd.read_sql(query, engine)

    df.to_sql(
        "dim_products",
        engine,
        if_exists="replace",
        index=False
    )

    print("dim_products loaded successfully")


def transform_orders():
    # Read staging tables
    orders_df = pd.read_sql(
        "SELECT * FROM stg_orders",
        engine
    )

    products_df = pd.read_sql(
        "SELECT * FROM dim_products",
        engine
    )

    # Join orders with products
    merged_df = orders_df.merge(
        products_df,
        on="product_id",
        how="left"
    )

    # Calculate total amount
    merged_df["total_amount"] = (
        merged_df["quantity"] * merged_df["price"]
    )

    # Select final columns
    fact_df = merged_df[
        [
            "order_id",
            "customer_id",
            "product_id",
            "quantity",
            "order_date",
            "total_amount"
        ]
    ]

    # Load fact table
    fact_df.to_sql(
        "fact_orders",
        engine,
        if_exists="replace",
        index=False
    )

    print("fact_orders loaded successfully")


def transform_data():
    transform_customers()
    transform_products()
    transform_orders()