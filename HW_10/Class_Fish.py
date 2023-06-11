from HW_10.Class_Animal import Animal


class Fish(Animal):
    def __init__(self, name: str, food: str):
        super().__init__(movement='swimming', replication='caviar')
        self._name = name
        self.__food = food

    def move(self):
        print(f'I am {self._name} and I am {self._movement}')

    def replicate(self):
        print(f'I am {self._name} and I replicate via {self._replication}')
