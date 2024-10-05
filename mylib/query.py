"""Query the database"""

import sqlite3


def read():
    """Read and print the database for all the rows of the dataBirth table"""
    conn = sqlite3.connect("birthData.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM birthData")
    print(cursor.fetchall())
    conn.close()
    return "birthData.db"


def create():
    """Create a fake data"""
    conn = sqlite3.connect("birthData.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO birthData VALUES ('2014','1','1','1','1')")
    conn.commit()
    conn.close()
    return "birthData.db"


def update():
    """Update day of week value of 1 and set the births to 1000"""
    conn = sqlite3.connect("birthData.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE birthData SET births = '1000' WHERE day_of_week = '1';")
    conn.commit()
    conn.close()
    return "birthData.db"


def delete():
    """Delete rows that year is equal to 2000"""
    conn = sqlite3.connect("birthData.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM birthData WHERE year = '2000';")
    conn.commit()
    conn.close()
    return "birthData.db"


if __name__ == "__main__":
    read()
    create()
    update()
    delete()
