import os

# from s import DataAnalyzer, DataVisualizer
from s.DataHandler import DataHandler
from s.FileManager import FileManager
from s.DataVisualizer import DataVisualizer
from s.DataAnalyzer import DataAnalyzer


class Menu:
    def __init__(self):
        self.main_menu()

    def main_menu(self):
        while True:
            print("\nMenu1:")
            print("1. CSV")
            print("2. JSON")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice in ["1", "2"]:
                file_type = "csv" if choice == "1" else "json"
                directory = f"data/{file_type}"
                files = FileManager.list_files(directory)

                if files:
                    print(f"Available {file_type.upper()} files:")
                    for idx, file in enumerate(files, start=1):
                        print(f"{idx}. {file}")
                    file_choice = int(input("Select a file by number: ")) - 1
                    file_path = os.path.join(directory, files[file_choice])
                    data_handler = DataHandler(file_path, file_type)

                    self.data_menu(data_handler)
                else:
                    print(f"No {file_type.upper()} files found.")

            elif choice == "3":
                print("Exiting program.")
                break
            else:
                print("Invalid option. Please choose again.")

    def data_menu(self, data_handler):
        da = DataAnalyzer(data_handler.data)
        dv = DataVisualizer(data_handler.data)
        while True:
            print("\nData Options:")
            print("1. Display Headers")
            print("2. Display Column")
            print("3. Sorting")
            print("4. Filter")
            print("5. Bar Chart")
            print("6. Pie Chart")
            print("7. Go back")
            data_choice = input("Choose an option: ")

            if data_choice == "1":
                data_handler.display_headers()
            elif data_choice == "2":
                column = input("Enter the column name to display: ")
                data_handler.display_column(column)
            elif data_choice == "3":
                headers = data_handler.get_headers()
                if headers:
                    headers_str = ", ".join(headers)
                    print("Available options:", headers_str)
                column = input("Enter the column name to sort: ")
                ascending = input("Sort ascending (y/n)? ") == "y"
                try:
                    da.sort_data(column, ascending)
                except ValueError as e:
                    print(e)
            elif data_choice == "4":
                column = input("Enter the column name to filter: ")
                value = input("Enter the value to filter: ")
                print(da.filter_data(column, value))
            elif data_choice == "5":
                column = input("Enter the column name for pie chart: ")
                dv.plot_top_pie(column)
            elif data_choice == "6":
                column = input("Enter the column name for top 10: ")
                dv.plot_top_bar(column)
            elif data_choice == "7":
                break
            else:
                print("Invalid option. Please choose again.")


if __name__ == "__main__":
    Menu()
