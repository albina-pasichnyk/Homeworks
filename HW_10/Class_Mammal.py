from HW_10.Class_Animal import Animal


class Mammal(Animal):
    """Class of Mammals inherited from Abstract Animal class"""

    def __init__(self, name: str, legs: int):
        """
        Constructor of Mammal Class, with pre-defined parameter movement and replication
        :param name: name of object of Mammal class
        :param legs: amount of legs used for walking (2 ot 4)
        """
        super().__init__(movement='walking', replication='live birth')
        self._name = name
        self._legs = legs

    def move(self):
        """Method of Mammal's moving, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I am {self._movement} on {self._legs} legs')

    def replicate(self):
        """Method of Mammal's replication, which is inherited from Abstract Class with it's own implementation"""
        print(f'I am {self._name} and I replicate via {self._replication}')
