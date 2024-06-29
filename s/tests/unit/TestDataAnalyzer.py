import unittest
import pandas as pd

from s.DataAnalyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        data = {
            "Column1": ["A", "B", "C", "D"],
            "Column2": [4, 3, 2, 1],
            "Column3": ["ýýý", "B", "C", "D"],
        }
        self.df = pd.DataFrame(data)
        self.analyzer = DataAnalyzer(self.df)

    def test_sort_data_valid_column(self):
        sorted_df = self.analyzer.sort_data("Column2", ascending=True)
        expected_order = [3, 2, 1, 0]
        self.assertListEqual(sorted_df.index.tolist(), expected_order)

    def test_sort_data_missing_column(self):
        with self.assertRaises(ValueError):
            self.analyzer.sort_data("NonExistentColumn")

    def test_sort_data_filter_invalid_values(self):
        sorted_df = self.analyzer.sort_data("Column3", ascending=True)
        self.assertFalse(sorted_df["Column3"].str.contains(r"[ýýý]").any())

    def test_filter_data_valid(self):
        filtered_df = self.analyzer.filter_data("Column1", "A")
        self.assertEqual(len(filtered_df), 1)
        self.assertEqual(filtered_df["Column1"].iloc[0], "A")

    def test_filter_data_missing_column(self):
        with self.assertRaises(ValueError):
            self.analyzer.filter_data("NonExistentColumn", "A")

    def test_filter_data_value_not_found(self):
        with self.assertRaises(ValueError):
            self.analyzer.filter_data("Column1", "NonExistentValue")


if __name__ == "__main__":
    unittest.main()
