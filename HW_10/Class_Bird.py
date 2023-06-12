from HW_10.Class_Animal import Animal


class Bird(Animal):
    """Class of Birds inherited from Abstract Animal class"""

    def __init__(self, name: str, food: str):
        """
        Constructor of Bird Class, with pre-defined parameter movement and replication
        :param name: name of object of Bird class
        :param food: type of food that it's consuming
        """
        super().__init__(movement='flying', replication='eggs')
        self._name = name
        self._food = food

    def move(self):
        """ Method of Bird's moving, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I am {self._movement}')

    def replicate(self):
        """Method of Bird's replication, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I replicate via {self._replication}')
