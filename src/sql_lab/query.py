import logging
import os

import mysql.connector


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

DBHOST = os.environ["DBHOST"]
DBUSER = os.environ["DBUSER"]
DBPASS = os.environ["DBPASS"]
DBNAME = os.environ["DBNAME"]


VALID_COLUMNS = {"id", "group", "name", "age", "email", "city"}


def get_data_by_group(value):
    """Return all rows where the `group` column equals value."""
    logging.info("Getting rows where group = %s", value)

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

        query = """
        SELECT id, `group`, name, age, email, city
        FROM mock
        WHERE `group` = %s
        """
        cursor.execute(query, (value,))

        rows = cursor.fetchall()

        logging.info("Found %d matching rows", len(rows))

        return rows

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

        logging.info("Database connection closed")


def plot_counts(groupby):
    logging.info("Counting rows grouped by %s", groupby)

    if groupby not in VALID_COLUMNS:
        logging.error("Invalid column name: %s", groupby)
        return []

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

        query = f"""
        SELECT `{groupby}`, COUNT(*) AS count
        FROM mock
        GROUP BY `{groupby}`
        ORDER BY count DESC
        """

        cursor.execute(query)

        counts = cursor.fetchall()

        logging.info(
            "Found %d distinct values for %s",
            len(counts),
            groupby,
        )

        return counts

    except mysql.connector.Error as error:
        logging.error("Database error: %s", error)
        return []

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None:
            connection.close()

        logging.info("Database connection closed")


def main():
    group_rows = get_data_by_group("ewqw")

    print("\nRows where group = 'ewqw':")
    for row in group_rows:
        print(row)
    city_counts = plot_counts("city")

    print("\nCounts by city:")
    for city, count in city_counts:
        print(f"{city}: {count}")


if __name__ == "__main__":
    main()
