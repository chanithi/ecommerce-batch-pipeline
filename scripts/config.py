# DB_USERNAME = "postgres"
# DB_PASSWORD = ""
# DB_HOST = "localhost"
# DB_PORT = "5432"
# DB_NAME = "ecommerce"

import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_HOST = "postgres"
DB_PORT = os.getenv("POSTGRES_PORT")
DB_NAME = os.getenv("POSTGRES_DB")