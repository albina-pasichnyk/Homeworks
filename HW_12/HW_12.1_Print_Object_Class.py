class Phone:
    """Mobile Phone Class"""

    def __init__(self, brand: str, model: str, screen: str, resolution: str, camera: int, memory: int, os: str):
        """Constructor to create Object of Company Class with specific parameters"""
        self.__brand = brand
        self.__model = model
        self.__screen = screen
        self.__resolution = resolution
        self.__camera = camera
        self.__memory = memory
        self.__os = os

    def __str__(self):
        """Return str(self)."""
        string_result = f'{self.__class__.__name__}: {{\nbrand: {self.__brand}\nmodel: {self.__model}\nscreen: {self.__screen}\nresolution: {self.__resolution}\ncamera: {self.__camera}\nmemory: {self.__memory}\nos: {self.__os}\n}}'
        return string_result


if __name__ == '__main__':
    IPhone = Phone('Apple', 'IPhone 12 Pro', '6.06\'', '2532 × 1170', 12, 256, 'iOS 14.1')
    print(IPhone)
