import pandas as pd


class CSVHandler:
    def __init__(self, file_path):
        # self.file_path = "data/s.csv"
        # self.file_path = "data/csv/flight_dataset.csv"
        self.file_path = file_path
        self.data = []

    def load_csv(self):
        try:
            self.data = pd.read_csv(self.file_path, encoding="latin1")
            print("CSV file loaded successfully.")
            return self.data
        except FileNotFoundError:
            print("File not found. Please check the file path.")
        except UnicodeDecodeError:
            print("Error decoding the file. Please check the encoding format.")

    # def display_headers(self):
    #     if self.data is not None:
    #         headers = list(self.data.columns)
    #         print("Headers:", headers)
    #     else:
    #         print("No data loaded. Please load the CSV file first.")

    def get_headers(self):
        if self.data is not None:
            return list(self.data.columns)
        else:
            print("No data loaded. Please load the CSV file first.")
            return []

    # def display_column(self, column_name):
    #     if self.data is not None:
    #         if column_name in self.data.columns:
    #             values = self.data[column_name].dropna().tolist()
    #             print(f"{column_name}:")
    #             for value in values:
    #                 print(value)
    #         else:
    #             print(f"'{column_name}' column not found in headers.")
    #
    #     else:
    #         print("No data loaded. Please load the CSV file first.")

    # def display_artists(self):
    #     if self.data is not None:
    #         if 'Artist' in self.data.columns:
    #             artists = self.data['Artist'].dropna().tolist()
    #             print("Artists:")
    #             for artist in artists:
    #                 print(artist)
    #         else:
    #             print("'Artist' column not found in headers.")
    #     else:
    #         print("No data loaded. Please load the CSV file first.")

    def sort_data(self, column, ascending=True):
        try:
            sorted_data = self.data.sort_values(by=column, ascending=ascending)
            print(sorted_data)
        except KeyError:
            raise ValueError(
                f"Column '{column}' does not exist in the dataset."
            )
