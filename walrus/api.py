import os
from walrus.FileConfig import FileConfig

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, 'data', 'country-capitals.csv')
file_object = FileConfig(file_path)


def hello():
    return "Hello World"


def find_capital(country_name, raise_errors=False):
    capital = file_object.get_capital(country_name)

    if capital is None:
        if raise_errors:
            raise ValueError(f"Data not found for: {country_name}")
        else:
            return None

    return capital


def get_capital(country_names, raise_errors=False):
    # Handle a single country name
    if isinstance(country_names, str):
        return find_capital(country_names, raise_errors)

    # Handle multiple country names
    else:
        return {country: find_capital(country, raise_errors)
                for country in country_names}
