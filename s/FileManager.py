import os


class FileManager:
    @staticmethod
    def list_files(directory):
        try:
            return [
                f
                for f in os.listdir(directory)
                if os.path.isfile(os.path.join(directory, f))
            ]
        except FileNotFoundError:
            print("Directory not found.")
            return []
