import os.path
import pandas as pd

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, 'data', 'country-capitals.csv')


def hello():
    return "Hello World"


def get_capital(country_name, raise_errors=False):
    # Load the data
    data = pd.read_csv(file_path)

    # Find the row where the 'CountryName' column matches the input country_name
    country_data = data[data['CountryName'] == country_name]

    # Check if any data was found
    if country_data.empty:
        if raise_errors:
            raise ValueError(f"No data found for country: {country_name}")
        else:
            return None

    # Extract and return the capital from the matched row
    return country_data.iloc[0]['CapitalName']

