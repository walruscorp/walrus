import pytest
import os
from walrus.country import Country

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, "test_data", "test-data.csv")
data = open(file_path, "r").readlines()


def test_iteration_items():
    country = Country(file_path)
    country_col = data[0].split(",").index("CountryName")
    for items, line in zip(country, data[1:]):
        values = line.split(",")
        assert items == values[country_col]


def test_length():
    assert len(Country(file_path)) == 34


def test_subscript():
    country = Country(file_path)
    assert country["Australia"] == "Canberra"
    assert country["Armenia"] == "Yerevan"
    assert country["Bahamas"] == "Nassau"
    assert country["Angola"] == "Luanda"
    assert country["Nothing"] is None


def test_print():
    country = Country(file_path)
    assert str(country) == "Country with 34 items"


def test_nested_loop():
    country = Country(file_path)
    count = 0

    for item_1 in country:
        for item_2 in country:
            count += 1

    assert count == 34 * 34
