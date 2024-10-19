"""
Extract a dataset from a URL, JSON or CSV formats tend to work well
"""

import requests
import os


def extract1(
    url="https://github.com/fivethirtyeight/data/raw/refs/heads/master/births/US_births_2000-2014_SSA.csv",
    file_path="data/birthdata.csv",
):
    """ "Extract a url to a file path"""

    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


def extract2(
    url2="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/births/US_births_1994-2003_CDC_NCHS.csv",
    file_path2="data/birthdata_1994.csv",
):
    """ "Extract a url to a file path"""
    os.makedirs(os.path.dirname(file_path2), exist_ok=True)
    with requests.get(url2) as r:
        with open(file_path2, "wb") as f:
            f.write(r.content)

    return file_path2


if __name__ == "__main__":
    extract1()
    extract2()
