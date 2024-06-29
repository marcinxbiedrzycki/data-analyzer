import unittest
from unittest.mock import patch

from s.FileManager import FileManager


class TestFileManager(unittest.TestCase):
    @patch("os.listdir")
    @patch("os.path.isfile")
    def test_list_files(self, mock_isfile, mock_listdir):
        # Mocking os.listdir to return a specific list of files
        mock_listdir.return_value = ["file1.txt", "file2.txt", "dir1"]
        # Mocking os.path.isfile to return True only for files
        mock_isfile.side_effect = lambda x: not x.endswith("dir1")

        files = FileManager.list_files("some_directory")
        expected_files = ["file1.txt", "file2.txt"]

        self.assertEqual(files, expected_files)

    @patch("os.listdir", side_effect=FileNotFoundError)
    def test_directory_not_found(self, mock_listdir):
        files = FileManager.list_files("non_existent_directory")
        self.assertEqual(files, [])


if __name__ == "__main__":
    unittest.main()
