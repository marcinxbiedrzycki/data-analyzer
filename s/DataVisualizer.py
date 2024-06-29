import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, data):
        self.data = data

    def plot_top_bar(self, column, top_n=10):
        top_artists = self.data[column].value_counts().head(top_n)
        top_artists.plot(kind="bar", color="green")
        plt.title(f"Top {top_n} {column}")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def plot_top_pie(self, column, top_n=5):
        column_name = column
        if column_name in self.data.columns:
            top_albums = self.data[column_name].value_counts().head(top_n)
            top_albums.plot(kind="pie", autopct="%1.1f%%")
            plt.title(f"Top {top_n} {column}")
            plt.ylabel("")
            plt.show()
        else:
            print(f"Column '{column_name}' not found in the dataset.")

    # TODO: toVerify
    # def plot_streams_histogram(self):
    #     plt.hist(self.data['Streams'], bins=20, color='blue')
    #     plt.title('Histogram liczby streamów')
    #     plt.xlabel('Liczba streamów')
    #     plt.ylabel('Liczba utworów')
    #     plt.show()
