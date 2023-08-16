from Class_Animal import Animal


class Fish(Animal):
    """Class of Fish inherited from Abstract Animal class"""

    def __init__(self, name: str, food: str):
        """
        Constructor of Fish Class, with pre-defined parameter movement and replication
        :param name: name of object of Bird class
        :param food: type of food that it's consuming
        """
        super().__init__(movement='swimming', replication='caviar')
        self._name = name
        self.__food = food

    def move(self):
        """Method of Fish's moving, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I am {self._movement}')

    def replicate(self):
        """Method of Fish's replication, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I replicate via {self._replication}')
