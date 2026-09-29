
"""Read, clean, and upload Mockaroo CSV data to MySQL."""

import logging
import os

import mysql.connector
import pandas as pd


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


DBHOST = os.environ["DBHOST"]
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBNAME = os.environ["DBNAME"]


def read_data(filename):
    """Read the CSV file into a pandas DataFrame."""
    logging.info("Reading data from %s", filename)

    data = pd.read_csv(filename)

    logging.info(
        "Read %d rows and %d columns",
        data.shape[0],
        data.shape[1],
    )

    return data


def clean_data(data):
    """Remove rows with missing values from the DataFrame."""
    logging.info("Cleaning data")

    cleaned_data = data.dropna()

    logging.info(
        "Removed %d rows with missing values",
        len(data) - len(cleaned_data),
    )

    return cleaned_data


def load_data(data, table):
    """Create the MySQL table if needed and upload the DataFrame."""
    logging.info("Loading data into table %s", table)

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=DBHOST,
            user=DBUSER,
            password=DBPASS,
            database=DBNAME,
        )

        cursor = connection.cursor()
        create_table_sql = f"""
        CREATE TABLE IF NOT EXISTS {table} (
            id BIGINT,
            `group` VARCHAR(255),
            name VARCHAR(255),
            age BIGINT,
            email VARCHAR(255),
            city VARCHAR(255)
        )
        """

        cursor.execute(create_table_sql)
        insert_sql = f"""
        INSERT INTO {table}
        (id, `group`, name, age, email, city)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        for row in data.itertuples(index=False, name=None):
            cursor.execute(insert_sql, row)

        connection.commit()

        logging.info(
            "Successfully uploaded %d rows",
            len(data),
        )

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)

    finally:
        # Close the database connection.
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

        logging.info("Database connection closed")


def main():
    """Read, clean, and upload the Mockaroo CSV data."""
    logging.info("Starting data processing")

    data = read_data("MOCK_DATA.csv")

    cleaned_data = clean_data(data)

    load_data(cleaned_data, "mock")

    logging.info("Data processing complete")


if __name__ == "__main__":
    main()
