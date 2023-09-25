import os.path
import pandas as pd


file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, 'data', 'country-capitals.csv')


def hello():
    return "Hello World"


def get_capital(country_name):
    # Load the data
    data = pd.read_csv(file_path)

    # Find the row where the 'CountryName' column matches the input country_name
    country_data = data[data['CountryName'] == country_name]

    if country_data.empty:
        return_value = "No data available for the country: " + country_name
        return return_value

    # Extract and return the capital from the matched row
    capital = country_data.iloc[0]['CapitalName']
    return capital