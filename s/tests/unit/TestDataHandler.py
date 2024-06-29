import unittest
from io import StringIO
from unittest.mock import patch

from s.DataHandler import DataHandler


class TestDataHandler(unittest.TestCase):

    def setUp(self):
        self.data = [
            ["col1", "col2", "col3"],
            [1, 4.5, "test1"],
            [2, 3.6, "test2"],
            [3, None, "test3"],
            [4, 7.8, "test4"],
        ]
        self.csv_data = StringIO(
            """col1,col2,col3
1,4.5,test1
2,3.6,test2
3,,test3
4,7.8,test4"""
        )

        self.json_data = StringIO(
            """
        [
            {"col1": 1, "col2": 4.5, "col3": "test1"},
            {"col1": 2, "col2": 3.6, "col3": "test2"},
            {"col1": 3, "col2": null, "col3": "test3"},
            {"col1": 4, "col2": 7.8, "col3": "test4"}
        ]
        """
        )

    def test_load_csv_data(self):
        handler = DataHandler(self.csv_data, file_type="csv")
        self.assertIsNotNone(handler.data)
        self.assertEqual(len(handler.data), 4)

    def test_load_json_data(self):
        handler = DataHandler(self.json_data, file_type="json")
        self.assertIsNotNone(handler.data)
        self.assertEqual(len(handler.data), 4)

    def test_display_headers(self):
        handler = DataHandler(self.csv_data, file_type="csv")
        headers = handler.data.columns.tolist()
        self.assertEqual(headers, ["col1", "col2", "col3"])

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_column_not_found(self, mock_stdout):
        handler = DataHandler(self.csv_data, file_type="csv")

        handler.display_column("nonexistent_column")
        output = mock_stdout.getvalue()
        expected_output = "'nonexistent_column' column not found in headers.\n"
        self.assertEqual(output, expected_output)

    @patch("sys.stdout", new_callable=StringIO)
    def test_display_column_existing(self, mock_stdout):
        handler = DataHandler(self.csv_data, file_type="csv")

        handler.display_column("col1")
        output = mock_stdout.getvalue()
        expected_output = "col1:\n1\n2\n3\n4\n"
        self.assertEqual(output, expected_output)

    def test_display_column_not_found2(self):
        handler = DataHandler(self.csv_data, file_type="csv")
        output = handler.display_column("col4")
        self.assertIsNone(output)

    def test_sort_data(self):
        handler = DataHandler(self.csv_data, file_type="csv")
        sorted_data = handler.sort_data("col2", ascending=True)
        self.assertEqual(sorted_data.iloc[0]["col2"], 3.6)

    def test_sort_data_column_not_found(self):
        handler = DataHandler(self.csv_data, file_type="csv")
        sorted_data = handler.sort_data("col4", ascending=True)
        self.assertIsNone(sorted_data)


if __name__ == "__main__":
    unittest.main()
