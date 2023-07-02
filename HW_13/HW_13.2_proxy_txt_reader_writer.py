from HW_13.reader_interface import IReader
from HW_13.txt_reader import TxtReader
from HW_13.txt_writer import TxtWriter
from HW_13.writer_interface import IWriter


class TxtProxyReaderWriter(IReader, IWriter):
    """Class of Proxy with Reader & Writer"""
    def __init__(self, txt_path):
        self.__result = ''
        self._is_actual = False
        self.__reader = TxtReader(txt_path)
        self.__writer = TxtWriter(txt_path)

    def read_file(self):
        """Proxy reader file method"""
        if self._is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read_file()
            self._is_actual = True
            return self.__result

    def write_file(self, browser_version: str):
        """
        Proxy writer file method
        :param browser_version: new browser version
        """
        if browser_version == self.__result:
            return
        else:
            self._is_actual = False
            self.__writer.write_file(browser_version)


if __name__ == '__main__':
    txt_proxy = TxtProxyReaderWriter('13_2_config_file.txt')
    data = txt_proxy.read_file()
    new_data = txt_proxy.read_file()
    txt_proxy.write_file('13.0')
    txt_proxy.read_file()
