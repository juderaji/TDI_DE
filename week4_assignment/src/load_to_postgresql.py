from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import SofaScoreData  # Adjust based on your models
import pandas as pd
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Create PostgreSQL connection URL
db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

# Create engine and session
engine = create_engine(db_url)
Session = sessionmaker(bind=engine)
session = Session()

# Load the transformed CSV data
df = pd.read_csv('datalake/processed_data.csv')

# Insert the data into the database
for _, row in df.iterrows():
    record = SofaScoreData(
        incident_type=row['incident_type'],
        time=row['time'],
        player_name=row['player_name'],
        home_score=row['home_score'],
        away_score=row['away_score']
    )
    session.add(record)

# Commit the transaction to save data
session.commit()
print("Data loaded into PostgreSQL successfully!")
