import os
from walrus.country import Country

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, 'data', 'country-capitals.csv')
country = Country(file_path)


def hello():
    return "Hello World"


def find_capital(country_name, raise_errors=False):
    capital = country.get_capital(country_name)

    if capital is None:
        if raise_errors:
            raise ValueError(f"Data not found for: {country_name}")
        else:
            return None

    return capital


def get_capital(country_names, raise_errors=False):
    if isinstance(country_names, str):
        return find_capital(country_names, raise_errors)

    else:
        return {a_country: find_capital(a_country, raise_errors)
                for a_country in country_names}
