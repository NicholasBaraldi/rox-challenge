from sqlalchemy import create_engine
import click
import os

from rox_challenge.source.data_source import CSVSource
from rox_challenge.targets.target_db import Target


@click.command()
def create_tables():
    """Command line to read csv files and write then as a sql database."""
    files = [filename for filename in os.listdir("data")]
    csv = CSVSource(base_path="data", source_files=files)
    dict = csv.read()
    engine = create_engine(
        "postgresql://postgres:password@localhost:5432/bike_database"
    )
    postgres = Target(engine=engine)
    for file_name, df in dict.items():
        postgres.write(dataframe=df, table_name=file_name)


if __name__ == "__main__":
    create_tables()
