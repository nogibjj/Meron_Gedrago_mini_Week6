"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well
"""

import requests


def extract(
    url="https://raw.githubusercontent.com/fivethirtyeight/data/refs/heads/master/births/US_births_2000-2014_SSA.csv",
    file_path="data/data.csv",
):
    """ "Extract a url to a file path"""
    with requests.get(url) as r:
        with open(file_path, "wb") as f:
            f.write(r.content)
    return file_path


if __name__ == "__main__":
    extract()
