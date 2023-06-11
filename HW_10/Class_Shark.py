from HW_10.Class_Fish import Fish


class Shark(Fish):
    def __init__(self, species: str, location: str):
        super().__init__('shark', 'carnivore')
        self._species = species
        self._location = location

    def is_danger(self):
        if self._species in ['white', 'tiger']:
            return True
        if self._species == 'cat':
            return False
        else:
            raise ValueError('Unknown dangerous')

    def print_spread_info(self):
        print(f'I am {self.__class__.__name__} and I live in {self._location}')
