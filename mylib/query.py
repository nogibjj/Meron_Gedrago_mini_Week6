import os
from databricks import sql
from dotenv import load_dotenv


join_table = """ 

CREATE TABLE combined_births 
AS SELECT * FROM mwg29_birthdata
UNION ALL
SELECT * FROM mwg29_birthdata_1994;
"""

agg_and_sort = """
SELECT 
    year, 
    SUM(births) AS total_births,
    AVG(births) AS avg_births
FROM 
    combined_births
GROUP BY 
    year
ORDER BY 
    avg_births DESC;
"""


def query():
    """ "Transforms and Loads data into the databricks database"""
    load_dotenv()
    with sql.connect(
        server_hostname=os.getenv("SQL_SERVER_KEY"),
        http_path=os.getenv("HTTP_PATH"),
        access_token=os.getenv("DATABRICKS_KEY"),
    ) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM combined_births")
            result = cursor.fetchall()
            if not result:
                cursor.execute(join_table)

            cursor.execute(agg_and_sort)

            cursor.close()
            connection.close()
    return "query successful"


if __name__ == "__main__":
    query()
