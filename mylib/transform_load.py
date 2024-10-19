"""
Load data into the databricks database
"""

import csv
import os
from databricks import sql
from dotenv import load_dotenv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/birthdata.csv", dataset_1994="data/birthdata_1994.csv"):
    """Load data into the databricks database"""
    df = csv.reader(open(dataset, newline=""), delimiter=",")
    df_1994 = csv.reader(open(dataset_1994, newline=""), delimiter=",")
    next(df)
    next(df_1994)
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SQL_SERVER_KEY"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS mwg29_birthdata (year INT, month INT, date_of_month INT, day_of_week INT, births INT);"""
            )
            cursor.execute("SELECT * FROM mwg29_birthdata")
            result = cursor.fetchall()
            if not result:
                string_sql = "INSERT INTO mwg29_birthdata VALUES"
                for i in df:
                    string_sql += "\n" + str(tuple(i)) + ","
                string_sql = string_sql[:-1] + ";"
                cursor.execute(string_sql)

            cursor.execute(
                """CREATE TABLE IF NOT EXISTS mwg29_birthdata_1994 (year INT, month INT, date_of_month INT, day_of_week INT, births INT);"""
            )
            cursor.execute("SELECT * FROM mwg29_birthdata_1994")
            result = cursor.fetchall()
            if not result:
                string_sql_1994 = "INSERT INTO mwg29_birthdata_1994 VALUES"
                for i in df_1994:
                    string_sql_1994 += "\n" + str(tuple(i)) + ","
                string_sql_1994 = string_sql_1994[:-1] + ";"
                cursor.execute(string_sql_1994)

            cursor.close()
            connection.close()
    return "dataset loaded to databricks or already exists!"


if __name__ == "__main__":
    load()
