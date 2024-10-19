import os
from databricks import sql
from dotenv import load_dotenv


complex_query = """ 

CREATE TABLE mwg29_combined_births 
AS SELECT * FROM mwg29_birthdata
UNION ALL
SELECT * FROM mwg29_birthdata_1994;

SELECT 
    year, 
    SUM(births) AS total_births,
    AVG(births) AS avg_births
FROM 
    mwg29_combined_births
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
            cursor.execute(complex_query)

            cursor.close()
            connection.close()
    return "query successful"


if __name__ == "__main__":
    query()
