from HW_10.Class_Mammal import Mammal


class Feline(Mammal):
    """Class of Feline inherited from Mammal class"""

    def __init__(self, name: str, domesticated: bool):
        """
        Constructor of Feline Class, with pre-defined parameter legs
        :param name: name of object of Feline class
        :param domesticated: if is feline domesticated
        """
        super().__init__(name, legs=4)
        self.domesticated = domesticated

    def purring(self):
        """Method of Feline to purr"""
        print('Mur Mur or Making a low continuous vibratory sound expressing contentment')

    def see_human(self):
        """Method of Feline to react on human based on domestication parameter"""
        if self.domesticated is True:
            self.purring()
        else:
            print('I am hunting')
