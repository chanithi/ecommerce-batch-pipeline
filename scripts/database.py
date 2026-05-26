from sqlalchemy import create_engine
from config import *

DATABASE_URL = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)