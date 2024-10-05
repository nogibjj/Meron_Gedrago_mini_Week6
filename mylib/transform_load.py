"""
Transforms and Loads data into the local SQLite3 database
Example:
,general name,count_products,ingred_FPro,avg_FPro_products,avg_distance_root,ingred_normalization_term,semantic_tree_name,semantic_tree_node
"""

import sqlite3
import csv
import os


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/data.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    conn = sqlite3.connect("birthData.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS birthData ")
    c.execute("CREATE TABLE birthData (year,month, date_of_month, day_of_week, births)")
    # insert
    c.executemany("INSERT INTO birthData VALUES (?,?, ?,?,?)", payload)
    conn.commit()
    conn.close()
    return "birthData.db"


if __name__ == "__main__":
    load()
