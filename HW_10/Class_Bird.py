from HW_10.Class_Animal import Animal


class Bird(Animal):
    def __init__(self, name: str, food: str):
        super().__init__(movement='flying', replication='eggs')
        self._name = name
        self._food = food

    def move(self):
        print(f'I am {self._name} and I am {self._movement}')

    def replicate(self):
        print(f'I am {self._name} and I replicate via {self._replication}')
