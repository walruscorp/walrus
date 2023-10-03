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

            self._country_capital = {
                line.split(",")[country_col]: line.split(",")[capital_col]
                for line in data[1:]
            }

    def get_capital(self, country):
        return self._country_capital.get(country, None)
