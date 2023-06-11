from HW_10.Class_Fish import Fish


class Salmon(Fish):
    def __init__(self, species: str, location: str, spawning: bool):
        super().__init__('salmon', 'herbivore')
        self._species = species
        self._location = location
        self._spawning = spawning

    def is_danger(self):
        return False

    def print_spread_info(self):
        print(f'I am {self.__class__.__name__} and I live in {self._location}')

    def get_live_phase(self):
        if self._spawning is True:
            print('I am heading the place of my birth to caviar and die')
        else:
            print('I am happily live')
