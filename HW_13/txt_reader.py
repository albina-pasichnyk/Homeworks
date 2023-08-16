from reader_interface import IReader


class TxtReader(IReader):
    """Class of TxtReader"""

    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        """Method to read from txt file"""
        with open(self.file_path) as file:
            text = file.read()
        return text
