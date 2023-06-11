from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, movement: str, replication: str):
        self._movement = movement
        self._replication = replication

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def replicate(self):
        pass
