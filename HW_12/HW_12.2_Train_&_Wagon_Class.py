class Wagon:
    """Class of Wagon of a Train"""
    CAPACITY = 10  # Amount of seats in Wagon

    def __new__(cls, number: int, list_of_passengers: list):
        """Create a new instance of a Wagon class"""
        if not isinstance(list_of_passengers, list):
            raise TypeError('List of passengers should be provided')
        if list_of_passengers.__len__() > cls.CAPACITY:
            raise ValueError(f'There is place in wagon only for {cls.CAPACITY} passengers')
        return super().__new__(cls)

    def __init__(self, number: int, list_of_passengers: list):
        """Fill in Object of Wagon Class with specific parameters"""
        self._number = number
        self._list_of_passengers = list_of_passengers

    def __len__(self):
        """Length of wagon showing"""
        return self._list_of_passengers.__len__()

    def __str__(self):
        """Return str(self)."""
        res_string = f'[{self._number}]'
        return res_string

    @property
    def number(self):
        """Wagon number"""
        return self._number

    @number.setter
    def number(self, new_wagon_number):
        """
        Set Wagon number
        :param new_wagon_number: new wagon number
        """
        self._number = new_wagon_number

    def add_passenger(self, passenger: str):
        """
        Function to add a wagon to a Train
        :param passenger: passenger (name, identification etc.)
        """
        if self._list_of_passengers.__len__() < self.CAPACITY:
            self._list_of_passengers.append(passenger)
        else:
            raise ValueError(f'There is place in wagon only for {self.CAPACITY} passengers')


class Train:
    """Class Train with wagons"""
    CAPACITY = 15  # Amount of wagons in a Train
    LOCOMOTIVE = '<=[HEAD]'  # Locomotive of the Train

    def __new__(cls, wagons: list):
        """Create a new instance of a Train class"""
        if not isinstance(wagons, list):
            raise TypeError('List of wagons should be provided')
        if wagons.__len__() > cls.CAPACITY:
            raise ValueError(f'Only {cls.CAPACITY} wagons can be added to the train')
        return super().__new__(cls)

    def __init__(self, wagons: list):
        """Fill in Object of Train Class with specific parameters"""
        wagon_number = 1
        for each in wagons:
            each.number = wagon_number
            wagon_number += 1
        self._wagons = wagons

    def __len__(self):
        """Length of the train without locomotive"""
        return self._wagons.__len__()

    def __str__(self):
        """Return str(self). numbers of wagon are updated to order of adding to the Train"""
        string_to_print = self.LOCOMOTIVE
        for each in self._wagons:
            string_to_print += '-' + str(each)
        return string_to_print

    def add_wagon(self, new_wagon: Wagon):
        """
        Function to add a wagon to a Train
        :param new_wagon: new Wagon object
        """
        if self._wagons.__len__() > self.CAPACITY:
            raise ValueError(f'Only {self.CAPACITY} wagons can be added to the train')
        new_wagon.number = self._wagons.__len__() + 1
        self._wagons.append(new_wagon)


if __name__ == '__main__':
    wagon = Wagon(1, ['passenger-1', 'passenger-2', 'passenger-3', 'passenger-4'])
    # Check __len__ of the created Wagon object
    assert wagon.__len__() == 4
    wagon.add_passenger('passenger-5')
    # Check __len__ of the Wagon object after adding passenger
    assert wagon.__len__() == 5
    # Check creating wagon with amount passengers exceeding its capacity
    try:
        wagon2 = Wagon(6, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'])
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'There is place in wagon only for 10 passengers'
    # Check adding more passenger than seat in Wagon
    wagon2 = Wagon(6, ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    try:
        wagon2.add_passenger('11')
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'There is place in wagon only for 10 passengers'

    wagon3 = Wagon(3, ['1', '2'])
    # Check printing for wagon to display its number assigned while creation
    print(wagon)
    print(wagon2)
    print(wagon3)

    train = Train([wagon, wagon2, wagon3])
    # Check __len__ of the created Train object
    print(train.__len__())
    # Check printing for Train to display specific string with locomotive representation and wagon numbers
    print(train)
