import requests
import json
import os

# Define the API endpoint and parameters
url = "https://sofascore.p.rapidapi.com/matches/get-incidents"
querystring = {"matchId": "8897222"}

# Define headers, including your API key
headers = {
    'x-rapidapi-key': "85de7f2ba5mshe06b5294b6c5b41p1aed85jsnfc2a9882873f",  # Replace with your actual API key
    'x-rapidapi-host': "sofascore.p.rapidapi.com"
}

# Send the GET request to the API
response = requests.get(url, headers=headers, params=querystring)

# Check the response status and save the data
if response.status_code == 200:
    data = response.json()
    
    # Define the datalake directory and file path
    datalake_dir = 'datalake/'
    if not os.path.exists(datalake_dir):
        os.makedirs(datalake_dir)
    
    # Save the data as a JSON file in the datalake
    with open(os.path.join(datalake_dir, 'raw_data.json'), 'w') as f:
        json.dump(data, f, indent=4)
    
    print("Data fetched and saved successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(f"Response text: {response.text}")
