"""
Extract a dataset from a URL, JSON or CSV formats tend to work well
"""

import requests
import os


def extract(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/births/US_births_2000-2014_SSA.csv",
    file_path="data/data.csv",
):
    """ "Extract a url to a file path"""

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


if __name__ == "__main__":
    extract()
