from HW_10.Class_Feline import Feline


class Tiger(Feline):
    """Class of Tiger inherited from Feline class"""

    def __init__(self, weight: int, color: str):
        """
        Constructor of Cat Class, with pre-defined parameter name and domesticated
        :param weight: weight of a tiger
        :param color: color of a tiger (orange, white)
        """
        super().__init__(name='tiger', domesticated=False)
        self._weight = weight
        self._color = color

    def print_tiger_info(self):
        """Method to get info about tiger"""
        print(f'I am {self._color} tiger and my weight is {self._weight} kilos')

    def print_food_info(self):
        """Method to get info about food is consumed by a tiger"""
        print(f'I {self._name} and I eat only raw hunted food')
