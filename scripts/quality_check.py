import pandas as pd
import logging

def run_quality_checks():
    logging.info("Running quality checks")

    df = pd.read_csv("data/processed/transformed_data.csv")

    if df.empty:
        raise ValueError("Dataset is empty")

    if df.isnull().sum().sum() > 0:
        raise ValueError("Null values detected")

    logging.info("Quality checks passed")