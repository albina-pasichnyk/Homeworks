from Class_Fish import Fish


class Shark(Fish):
    """Class of Shark inherited from Fish class"""

    def __init__(self, species: str, location: str):
        """
        Constructor of Shark Class, with pre-defined parameter name and food
        :param species: specie of a Shark (pre-defined: white, tiger, cat)
        :param location: location where shark is spread
        """
        super().__init__('shark', 'carnivore')
        self._species = species
        self._location = location

    def is_danger(self):
        """Method to get info if shark if danger based on its specie"""
        if self._species in ['white', 'tiger']:
            return True
        if self._species == 'cat':
            return False
        else:
            raise ValueError('Unknown dangerous')

    def print_spread_info(self):
        """Method to get info about spread location of shark"""
        print(f'I am {self.__class__.__name__} and I live in {self._location}')
