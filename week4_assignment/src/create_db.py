import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from models import create_tables

# Load environment variables from the .env file
load_dotenv()

# PostgreSQL connection url
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create the PostgreSQL engine
engine=create_engine(db_url)

# Create tables
create_tables(engine)

print("Tables created successfully!")