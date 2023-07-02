from abc import ABC, abstractmethod


class IReader(ABC):
    """Reader Interface"""
    @abstractmethod
    def read_file(self): ...
