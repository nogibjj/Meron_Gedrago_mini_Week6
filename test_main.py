"""
Test goes here

"""

from mylib.extract import extract1, extract2
from mylib.transform_load import load
from mylib.query import query


def test_extract():
    """testing extract"""
    test11 = extract1()
    test12 = extract2()
    assert test11 is not None
    assert test12 is not None


def test_load():
    """testing load"""
    test2 = load()
    assert test2 == "dataset loaded to databricks or already exists!"


def test_query():
    """testing query"""
    test3 = query()
    assert test3 == "query successful"


if __name__ == "__main__":
    test_extract()
    test_load()
    test_query

    print("Everything passed")
