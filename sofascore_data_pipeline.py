import requests
import pandas as pd
import schedule
import time
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Fetching data from the free-football-api-data.p.rapidapi.com API
def fetch_data(url: str, params: dict, headers: dict) -> pd.DataFrame:
    """
    Fetch data from the free-football-api-data.p.rapidapi.com API.

    Args:
        url (str): The URL of the API endpoint.
        params (dict): The parameters to pass to the API.
        headers (dict): The headers to pass to the API.

    Returns:
        pd.DataFrame: The data from the API.
    """
    try:
        logging.info("Making API request...")
        response = requests.get(url, params=params, headers=headers)
        logging.info("API request complete.")
        response.raise_for_status()
        logging.info("API response status code: %s", response.status_code)
        data = response.json()
        logging.debug("API response data: %s", data)
        return pd.DataFrame(data)
    except requests.exceptions.RequestException as e:
        logging.error("Error: %s", e)
        return None

# Saving the data to a Parquet file
def save_to_parquet(df: pd.DataFrame, filename: str) -> None:
    """
    Save the data to a Parquet file.

    Args:
        df (pd.DataFrame): The data to save.
        filename (str): The filename to save the data to.
    """
    df.to_parquet(filename, index=False)

# Saving the data to an Excel file
def save_to_excel(df: pd.DataFrame, filename: str) -> None:
    """
    Save the data to an Excel file.

    Args:
        df (pd.DataFrame): The data to save.
        filename (str): The filename to save the data to.
    """
    df.to_excel(filename, index=False)

# Main program to fetch and save data
def main() -> None:
    url = "https://free-football-api-data.p.rapidapi.com/football-event-country-channels"
    params = {"eventid": "12650707"}
    headers = {
        'x-rapidapi-key': "85de7f2ba5mshe06b5294b6c5b41p1aed85jsnfc2a9882873f",
        'x-rapidapi-host': "free-football-api-data.p.rapidapi.com"
    }

    # Fetch data from API
    df = fetch_data(url, params, headers)

    if df is not None:
        # Save data to Parquet file
        logging.info("Saving data to Parquet file...")
        save_to_parquet(df, 'data.parquet')
        
        # Save data to Excel file
        logging.info("Saving data to Excel file...")
        save_to_excel(df, 'data.xlsx')
    else:
        logging.error("No data to save.")

# Setting up Periodic updates
def periodic_updates() -> None:
    logging.info("Running periodic updates...")
    try:
        main()
    except Exception as e:
        logging.error("Error running periodic updates: %s", e)

# Schedule periodic updates every 1 minute
schedule.every(1).minutes.do(periodic_updates)

def run_schedule() -> None:
    while True:
        schedule.run_pending()
        time.sleep(60)  # wait 1 minute before checking again

if __name__ == "__main__":
    run_schedule()