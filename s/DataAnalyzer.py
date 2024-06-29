class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def sort_data(self, column, ascending=True):
        try:
            # Usunięcie wierszy z brakującymi wartościami w danej kolumnie
            sorted_data = self.data.dropna(subset=[column]).sort_values(
                by=column, ascending=ascending
            )

            # Filtrowanie nieczytelnych wartości
            sorted_data = sorted_data[
                ~sorted_data[column].str.contains(r"[ýýý]", na=False)
            ]

            print(sorted_data)
            return sorted_data
        except KeyError:
            raise ValueError(
                f"Column '{column}' does not exist in the dataset."
            )

    def filter_data(self, column, value):
        if column not in self.data.columns:
            raise ValueError(f"Column '{column}' does not exist in the dataset.")
        if value not in self.data[column].values:
            raise ValueError(f"Value '{value}' not found in column '{column}'.")
        return self.data[self.data[column] == value]

    # def sort_data(self, column, ascending=True):
    #     try:
    #         sorted_data = self.data.sort_values(by=column, ascending=ascending)
    #         print(sorted_data)
    #         return self.data.sort_values(by=column, ascending=ascending)
    #     except KeyError:
    #         raise ValueError(f"Column '{column}' does not exist in the dataset.")
