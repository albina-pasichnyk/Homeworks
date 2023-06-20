from abc import ABC, abstractmethod


class IRadar(ABC):
    @abstractmethod
    def _scan_area(self, quantity: int): ...
