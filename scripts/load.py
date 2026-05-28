# import pandas as pd
# from sqlalchemy import create_engine
# import logging

# def load_data():
#     logging.info("Starting database load")

#     df = pd.read_csv("data/processed/transformed_data.csv")

#     engine = create_engine(
#         "postgresql://username:password@localhost:5432/ecommerce_db"
#     )

#     df.to_sql(
#         "sales_data",
#         engine,
#         if_exists="replace",
#         index=False
#     )

#     logging.info("Data load completed")
import pandas as pd
import logging

from scripts.database import engine

def load_data():

    logging.info("Loading data into staging table")

    df = pd.read_csv("data/processed/transformed_data.csv")

    df.to_sql(
        "stg_orders",
        engine,
        if_exists="replace",
        index=False
    )

    logging.info("Staging table load completed")