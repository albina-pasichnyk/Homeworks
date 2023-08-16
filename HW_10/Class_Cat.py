from Class_Feline import Feline


class Cat(Feline):
    """Class of Cat inherited from Feline class"""

    def __init__(self, nickname: str, slave_name):
        """
        Constructor of Cat Class, with pre-defined parameter name and domesticated
        :param nickname: nickname of a cat
        :param slave_name: name of its slave, who think he/she is owner
        """
        super().__init__(name='cat', domesticated=True)
        self._nickname = nickname
        self._slave_name = slave_name

    def print_hierarchy_info(self):
        """Method to get hierarchy info of a cat and human"""
        print(f'{self._nickname} has a slave {self._slave_name}')

    def print_food_info(self):
        """Method to get info about food consumed by cat"""
        print(f'As a domastic {self._name} I eat only cooked food')
