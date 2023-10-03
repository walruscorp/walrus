class Country:
    def __init__(self, file_path):
        self._country_capital = {}
        self._set_capital(file_path)

    def _set_capital(self, file_path):
        with open(file_path, "r") as file:
            data = file.readlines()

            header = data[0].split(",")
            country_col = header.index("CountryName")
            capital_col = header.index("CapitalName")

            self._country_capital = {
                values[country_col]: values[capital_col]
                for line in data[1:]
                for values in [line.split(",")]
            }

    def get_capital(self, country):
        return self._country_capital.get(country, None)
