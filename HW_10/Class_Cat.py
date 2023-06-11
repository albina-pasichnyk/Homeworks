from HW_10.Class_Feline import Feline


class Cat(Feline):
    def __init__(self, nickname: str, slave_name):
        super().__init__(name='cat', domesticated=True)
        self._nickname = nickname
        self._slave_name = slave_name

    def print_hierarchy_info(self):
        print(f'{self._nickname} has a slave {self._slave_name}')

    def print_food_info(self):
        print(f'As a domastic {self._name} I eat only cooked food')
