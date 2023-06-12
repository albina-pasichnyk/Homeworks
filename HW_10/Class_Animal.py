from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract Animal Class"""

    def __init__(self, movement: str, replication: str):
        """
        Constructor of abstract animal class
        :param movement: way of movement which animal is doing
        :param replication: way of replication is used by animal
        """
        self._movement = movement
        self._replication = replication

    @abstractmethod
    def move(self):
        """Abstract method for animal's moving"""
        pass

    @abstractmethod
    def replicate(self):
        """ Abstract method for animal's replication"""
        pass
