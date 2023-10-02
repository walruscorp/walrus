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


def get_capital_2(country_names, raise_errors=False):
    # Dictionary to store country and capital as key-value pair
    country_capital = {}

    # Open the csv file with the reading mode
    with open(file_path, 'r') as file:
        # Split the file line by line and store it in a list
        data = file.readlines()

        # Store country and its capital as a key-value pair
        for line in data:
            values = line.split(",")
            country_capital[values[0]] = values[1]

    # Handle a single country name
    if isinstance(country_names, str):
        capital = country_capital.get(country_names)

        # Check if any data was found
        if capital is None:
            if raise_errors:
                raise ValueError(f"No data found for country: {country_names}")
            else:
                return None

        # Extract and return the capital
        return capital

    # Handle multiple country names
    else:
        # Dictionary to store hte country and capitals of requested countries
        results = {}

        for country in country_names:
            capital = country_capital.get(country)
            if capital is None:
                if raise_errors:
                    raise ValueError(f"No data found for country: {country}")
                else:
                    results[country] = None
            else:
                results[country] = capital
    return results



