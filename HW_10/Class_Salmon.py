from HW_10.Class_Fish import Fish


class Salmon(Fish):
    """Class of Salmon inherited from Fish class"""

    def __init__(self, species: str, location: str, spawning: bool):
        """
        Constructor of Salmon Class, with pre-defined parameter name and food
        :param species: specie of a Salmon
        :param location: location where salmon is spread
        :param spawning: is salmon in its spawning phase
        """
        super().__init__('salmon', 'herbivore')
        self._species = species
        self._location = location
        self._spawning = spawning

    def is_danger(self):
        """Method is object is danger"""
        return False

    def print_spread_info(self):
        """Method to get info about spread location of salmon"""
        print(f'I am {self.__class__.__name__} and I live in {self._location}')

    def get_live_phase(self):
        """Method to get info about life phase"""
        if self._spawning is True:
            print('I am heading the place of my birth to caviar and die')
        else:
            print('I am happily live')
