from prefect import task, Flow
from src.fetch_data import fetch_data
from src.transform_data import transform_data
from src.load_to_postgresql import load_data

@task
def etl_pipeline():
    fetch_data()
    transform_data()
    load_data()

with Flow("ETL Flow") as flow:
    etl_pipeline()

# Run the flow
flow.run()