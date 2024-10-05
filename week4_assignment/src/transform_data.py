import json
import pandas as pd

# Load the raw data from the JSON file
with open('datalake/raw_data.json', 'r') as f:
    data = json.load(f)

# Extract relevant fields from the raw data
incidents = data.get('incidents', [])

# Convert the data to a pandas DataFrame
df = pd.DataFrame(incidents)

# Select the columns that match your database model
df = df[['incidentType', 'time', 'playerName', 'homeScore', 'awayScore']]

# Rename the columns to match your database model
df.columns = ['incident_type', 'time', 'player_name', 'home_score', 'away_score']

# Save the transformed data as a CSV file in the datalake
df.to_csv('datalake/processed_data.csv', index=False)

print("Data transformed and saved successfully!")
