from HW_10.Class_Bird import Bird


class Eagle(Bird):
    def __init__(self, species: str, wings_size: float):
        super().__init__(name='eagle', food='rabbits')
        self._species = species
        self._wings_size = wings_size

    def print_eagle_info(self):
        print(f'I am {self._species} and my wings size is {self._wings_size} meters')

    def hunting(self):
        print(f'I am hunting and eating {self._food}')
