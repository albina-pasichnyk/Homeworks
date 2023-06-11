from HW_10.Class_Mammal import Mammal


class Feline(Mammal):
    def __init__(self, name: str, domesticated: bool):
        super().__init__(name, legs=4)
        self.domesticated = domesticated

    def purring(self):
        print('Mur Mur or Making a low continuous vibratory sound expressing contentment')

    def see_human(self):
        if self.domesticated is True:
            self.purring()
        else:
            print('I am hunting')
