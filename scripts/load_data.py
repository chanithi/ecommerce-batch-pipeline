import pandas as pd

from sqlalchemy import text

from database import engine
from logger import logger


def get_max_id(table_name, id_column):

    try:

        query = text(
            f"SELECT COALESCE(MAX({id_column}), 0) FROM {table_name}"
        )

        with engine.connect() as conn:

            result = conn.execute(query)

            max_id = result.scalar()

        logger.info(
            f"{table_name} current max id: {max_id}"
        )

        return max_id

    except Exception as e:

        logger.error(
            f"Error fetching max id for {table_name}: {e}"
        )

        return 0


def incremental_load(
    csv_path,
    table_name,
    id_column
):

    try:

        # read csv
        df = pd.read_csv(csv_path)

        # get current max id
        max_id = get_max_id(
            table_name,
            id_column
        )

        # filter new rows
        new_rows = df[
            df[id_column] > max_id
        ]

        if new_rows.empty:

            logger.info(
                f"No new rows for {table_name}"
            )

            print(
                f"No new rows for {table_name}"
            )

            return

        # load only new rows
        new_rows.to_sql(
            table_name,
            engine,
            if_exists="append",
            index=False
        )

        logger.info(
            f"{len(new_rows)} rows loaded into {table_name}"
        )

        print(
            f"{len(new_rows)} rows loaded into {table_name}"
        )

    except Exception as e:

        logger.error(
            f"Error loading {table_name}: {e}"
        )

        print(
            f"Error loading {table_name}"
        )


def main():

    incremental_load(
        "data/raw/customers.csv",
        "customers",
        "customer_id"
    )

    incremental_load(
        "data/raw/products.csv",
        "products",
        "product_id"
    )

    incremental_load(
        "data/raw/orders.csv",
        "orders",
        "order_id"
    )


if __name__ == "__main__":
    main()