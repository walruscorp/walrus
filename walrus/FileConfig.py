class FileConfig:
    def __init__(self, file_path):
        self._country_capital = {}
        self._set_capital(file_path)

    def _set_capital(self, file_path):
        with open(file_path, 'r') as file:
            data = file.readlines()

            header = data[0].split(",")
            country_col = header.index('CountryName')
            capital_col = header.index('CapitalName')

            for line in data[1:]:
                values = line.split(",")
                country_name = values[country_col]
                capital_name = values[capital_col]
                self._country_capital[country_name] = capital_name

    def get_capital(self, country):
        return self._country_capital.get(country, None)
