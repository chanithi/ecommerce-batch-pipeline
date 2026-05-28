import pandas as pd
import logging

def extract_data():
    logging.info("Starting data extraction")

    df = pd.read_csv("data/raw/ecommerce_data.csv")

    df.to_csv("data/processed/extracted_data.csv", index=False)

    logging.info("Extraction completed")