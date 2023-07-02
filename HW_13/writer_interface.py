from abc import ABC, abstractmethod


class IWriter(ABC):
    """Writer Interface"""
    @abstractmethod
    def write_file(self, browser_version: str): ...
