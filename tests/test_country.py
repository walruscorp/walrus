import pytest
import os
from walrus.country import Country
import sys
from io import StringIO

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, "test_data", "test-data.csv")
data = open(file_path, "r").readlines()


def test_iteration_next():
    country_iterator = iter(Country(file_path))
    assert next(country_iterator) == "Somaliland"
    assert next(country_iterator) == "American Samoa"
    assert next(country_iterator) == "Andorra"
    assert next(country_iterator) == "Angola"


def test_iteration_items():
    country_iterator = iter(Country(file_path))
    country_col = data[0].split(",").index("CountryName")
    for items, line in zip(country_iterator, data[1:]):
        values = line.split(",")
        assert items == values[country_col]


def test_length():
    assert len(Country(file_path)) == len(data) - 1


def test_iteration():
    country_iterator = iter(Country(file_path))
    country_col = data[0].split(",").index("CountryName")
    for line in data[1:]:
        values = line.split(",")
        assert next(country_iterator) == values[country_col]


def test_iteration_end():
    country_iterator = iter(Country(file_path))
    for i in range(len(Country(file_path))):
        next(country_iterator)

    with pytest.raises(StopIteration):
        next(country_iterator)


def test_subscript():
    country = Country(file_path)
    assert country["Australia"] == "Canberra"
    assert country["Armenia"] == "Yerevan"
    assert country["Bahamas"] == "Nassau"
    assert country["Angola"] == "Luanda"
    assert country["Nothing"] is None

def test_print():
    country = Country(file_path)
    test_dict = {item: country[item] for item in country}

    original_stdout = sys.stdout
    new_stdout = StringIO()
    sys.stdout = new_stdout

    print(country)
    sys.stdout = original_stdout

    assert new_stdout.getvalue().strip() == str(test_dict)
