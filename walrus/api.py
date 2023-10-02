import os

file_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(file_dir, 'data', 'country-capitals.csv')


def hello():
    return "Hello World"


def find_capital(country_name, raise_errors=False):
    # Dictionary to store country and capital as key-value pair
    country_capital = {}

    # Open the csv file with the reading mode
    with open(file_path, 'r') as file:
        # Split the file line by line and store it in a list
        data = file.readlines()

        # Header of the csv file
        header = data[0].split(",")

        # Indexes for country and capitals, respectively
        country_col = header.index('CountryName')
        capital_col = header.index('CapitalName')

        # Ignore the first line
        # Store country and its capital as a key-value pair
        for line in data[1:]:
            values = line.split(",")
            country_capital[values[country_col]] = values[capital_col]

    capital = country_capital.get(country_name)

    # Check if any data was found
    if capital is None:
        if raise_errors:
            raise ValueError(f"No data found for country: {country_name}")
        else:
            return None

    # Extract and return the capital
    return capital


def get_capital(country_names, raise_errors=False):
    # Handle a single country name
    if isinstance(country_names, str):
        return find_capital(country_names, raise_errors)

    # Handle multiple country names
    else:
        # Dictionary to store the country and capitals of requested countries
        results = {}

        for country in country_names:
            results[country] = find_capital(country, raise_errors)

        return results
