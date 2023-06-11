from HW_10.Class_Animal import Animal


class Mammal(Animal):
    def __init__(self, name: str, legs: int):
        super().__init__(movement='walking', replication='live birth')
        self._name = name
        self._legs = legs

    def move(self):
        print(f'I am {self._name} and I am {self._movement} on {self._legs} legs')

    def replicate(self):
        print(f'I am {self._name} and I replicate via {self._replication}')
