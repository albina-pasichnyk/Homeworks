class Worker:
    COMPANY_AGE = 25

    def __init__(self, first_name: str, last_name: str, position: str, salary: int,
                 years_in_company: int, fte: bool):
        """
        Constructor to create Object of Worker Class with specific attributes
        :param first_name: First name of Worker
        :param last_name: Last name of employee
        :param position: Worker's Position in company
        :param salary: Salary of respective worker in USD
        :param years_in_company: Amount of years employee works in the company
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__position = position
        self.__salary = salary
        self.__years_in_company = years_in_company
        self.fte = fte

    @property
    def first_name(self):
        """ First name of worker"""
        return self.__first_name

    @first_name.setter
    def first_name(self, new_first_name):
        """
        Set first name of worker
        :param new_first_name: new first name of worker
        :return:
        """
        if not isinstance(new_first_name, str):
            raise TypeError('Value must be a string')
        if not new_first_name.isalpha():
            raise ValueError('Name can contain only alphabetic characters')
        if not 2 <= len(new_first_name) < 20:
            raise ValueError(
                'Incorrect length of first name. It should be at least 2 letters, but not more than 20')
        self.__first_name = new_first_name

    @first_name.deleter
    def first_name(self):
        """Delete first name of worker"""
        raise NotImplementedError('It is not allowed to delete worker\'s name')

    @property
    def last_name(self):
        """Last name"""
        return self.__last_name

    @last_name.setter
    def last_name(self, new_last_name):
        """
        Set new Last name
        :param new_last_name: new value of last name
        """
        if not isinstance(new_last_name, str):
            raise TypeError('Value mist be a string')
        if not new_last_name.isalpha():
            raise ValueError('Last name can contain only alphabetic characters')
        if not 1 <= len(new_last_name) <= 25:
            raise ValueError('Incorrect length of first name. It should be at least 1 letters, but not more than 25')
        self.__last_name = new_last_name

    @last_name.deleter
    def last_name(self):
        """Delete last name"""
        raise NotImplementedError('It is not allowed to delete worker\'s last name')

    @property
    def position(self):
        """Position"""
        return self.__position

    @position.setter
    def position(self, new_position):
        """
        Set new position
        :param new_position: new position
        """
        if not isinstance(new_position, str):
            raise TypeError('Worker\'s position must be a string value')
        self.__position = new_position

    @property
    def salary(self):
        """Salary"""
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        """
        Set new salary
        :param new_salary: new salary
        """
        if not isinstance(new_salary, int):
            raise TypeError('Salary can be only a numeric value')
        if not 0 < new_salary <= 10000:
            raise ValueError('Salary should be between 1 and 10000 inclusively')
        self.__salary = new_salary

    @property
    def years_in_company(self):
        """Years in company"""
        return self.__years_in_company

    @years_in_company.setter
    def years_in_company(self, new_years_in_company):
        """
        Set new amount of years in company
        :param new_years_in_company: new value of years in company
        """
        if not isinstance(new_years_in_company, int):
            raise TypeError('Value should be integer')
        if not 0 < new_years_in_company <= self.COMPANY_AGE:
            raise ValueError('Worker cannot work in company more than company\'s age')
        self.__years_in_company = new_years_in_company

    @staticmethod
    def get_vacation_days():
        """Get amount of vacation days"""
        return 21

    @classmethod
    def create_part_time_employee(cls, first_name: str, last_name: str, position: str, salary: int,
                                  years_in_company: int, part_time: float):
        """
        Construct a part time employee company based on __init__
        :param first_name: First name of PTE
        :param last_name: Last name of PTE
        :param position: Position of PTE
        :param salary: Salary of PTE
        :param years_in_company: Years PTE works for company
        :param part_time: coefficient applied to full time
        :return: created worker object with processed parameters
        """
        if not 0 < part_time < 1:
            raise ValueError('Part time value should be between 0 and 1 exclusively')
        salary = int(salary * part_time)
        return cls(first_name, last_name, position, salary, years_in_company, False)

    def __calculate_yearly_bonus(self) -> float:
        """
        Private function to calculate bonus based on amount of years employees work for company
        :return: bonus coefficient
        """
        bonus = 1
        if self.__years_in_company > 20:
            bonus += 0.1
        if self.__years_in_company % 5 == 0:
            bonus += 0.05
        return bonus

    def update_salary(self):  # change to result of previous function
        """
        Function to update salary based on worker's bonus
        """
        bonus = self.__calculate_yearly_bonus()
        self.__salary = self.__salary * bonus


if __name__ == '__main__':
    # Short version of Set of tests for Worker Class

    # Create an object of Class Company
    Developer = Worker('Sam', 'Grey', 'Developer', 5000, 15, True)
    QA = Worker('Alf', 'Street', 'QA', 3000, 4, True)

    # Check Class Method create_part_time_employee
    # Test 1 - Check create object using class method
    part_time_worker = Worker.create_part_time_employee('Beta', 'Grey', 'CEO', 1000, 10, 0.5)
    assert part_time_worker.salary == 500
    # Test 2 - Check incorrect part_time parameter
    try:
        part_time_worker_2 = Worker.create_part_time_employee('Name', 'Last name', 'AQA', 2000, 5, 1.5)
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Part time value should be between 0 and 1 exclusively'

    # Check update_salary function
    Developer.update_salary()
    assert Developer.salary == 5250
