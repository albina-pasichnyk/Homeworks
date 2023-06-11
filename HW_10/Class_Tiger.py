from HW_10.Class_Feline import Feline


class Tiger(Feline):
    def __init__(self, weight: int, color: str):
        super().__init__(name='tiger', domesticated=False)
        self._weight = weight
        self._color = color

    def print_tiger_info(self):
        print(f'I am {self._color} tiger and my weight is {self._weight} kilos')

    def print_food_info(self):
        print(f'I {self._name} and I eat only raw hunted food')
