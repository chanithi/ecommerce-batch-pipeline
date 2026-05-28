import pandas as pd
import logging

def clean_data():
    logging.info("Starting data cleaning")

    df = pd.read_csv("data/processed/extracted_data.csv")

    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)

    df.to_csv("data/processed/cleaned_data.csv", index=False)

    logging.info("Cleaning completed")