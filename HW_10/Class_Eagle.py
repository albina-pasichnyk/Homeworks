from HW_10.Class_Bird import Bird


class Eagle(Bird):
    """Class of Eagles inherited from Birds class"""

    def __init__(self, species: str, wings_size: float):
        """
        Constructor of Eagle Class, with pre-defined parameter name and food
        :param species: species of an Egle
        :param wings_size: size of wings in meters
        """
        super().__init__(name='eagle', food='rabbits')
        self._species = species
        self._wings_size = wings_size

    def print_eagle_info(self):
        """Method to print info about object of Eagle class"""
        print(f'I am {self._species} and my wings size is {self._wings_size} meters')

    def hunting(self):
        """Method of hunting"""
        print(f'I am hunting and eating {self._food}')
