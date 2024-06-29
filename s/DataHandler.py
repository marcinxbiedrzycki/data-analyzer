import pandas as pd

from s import CSVHandler


class DataHandler:
    def __init__(self, file_path, file_type="csv"):
        self.file_path = file_path
        self.data = self.load_data(file_type)

## tutaj można by z wzorców pokorzystać, 2 strategię/fabryki csv i json interfejs z metodą load data
    def load_data(self, file_type):
        try:
            if file_type == "csv":
                return pd.read_csv(self.file_path)
            elif file_type == "json":
                return pd.read_json(self.file_path)
        except (FileNotFoundError, ValueError) as e:
            print(f"Error loading {file_type} file: {e}")
            return None

    def display_headers(self):
        if self.data is not None:
            headers = list(self.data.columns)
            print("Available options:", ", ".join(headers))
        else:
            print("No data loaded.")

    def display_column(self, column_name):
        if self.data is not None:
            if column_name in self.data.columns:
                values = self.data[column_name].dropna().tolist()
                print(f"{column_name}:")
                for value in values:
                    print(value)
            else:
                print(f"'{column_name}' column not found in headers.")

        else:
            print("No data loaded. Please load the CSV file first.")

    # def sort_data(self, column, ascending=True):
    #     try:
    #         sorted_data = self.data.sort_values(by=column, ascending=ascending)
    #         print(sorted_data)
    #     except KeyError:
    #         raise ValueError(f"Column '{column}' does not exist in the dataset.")

    def sort_data(self, column, ascending=True):
        if self.data is not None:
            try:
                sorted_data = self.data.dropna(subset=[column]).sort_values(
                    by=column, ascending=ascending
                )
                print(sorted_data)
                return sorted_data
            except KeyError:
                print(f"Column '{column}' does not exist.")
        else:
            print("No data loaded.")
