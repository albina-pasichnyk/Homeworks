from writer_interface import IWriter


class TxtWriter(IWriter):
    """Class of TxtWriter"""

    def __init__(self, file_path):
        self.file_path = file_path

    def write_file(self, browser_version: str):
        """
        Method of writing to file
        :param browser_version: new value of browser version
        """
        with open(self.file_path, 'r+') as file:
            file.seek(0)
            file.write(browser_version)
