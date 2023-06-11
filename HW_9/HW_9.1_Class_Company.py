class Company:
    CURRENT_YEAR = 2023

    def __init__(self, name: str, country: str, headquarter: str, founded: int, ceo: str, employees: int):
        """
        Default function to create Object of Company Class with specific parameters
        :param name: Company Name
        :param country: Country where Company is origin from
        :param headquarter: City where company's headquarter is located
        :param founded: Year when company was founded
        :param ceo: Name and Last Name of current company's CEO
        :param employees: Total amount of employees in 2023
        """
        self.__name = name
        self.__country = country
        self.__headquarter = headquarter
        self.__founded = founded
        self.__ceo = ceo
        self.__employees = employees

    @property
    def name(self):
        """Company name"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """
        Set Company name
        :param new_name: new name of the company
        """
        if not new_name.isalpha():
            raise ValueError('Company name can contain only letters')
        if len(new_name) > 25:
            raise ValueError('Company length cannot be longer than 25 characters')
        self.__name = new_name

    @name.deleter
    def name(self):
        """Delete Company name"""
        raise NotImplementedError('It is not allowed to delete Company name')

    @property
    def country(self):
        """Country of registration"""
        return self.__country

    @country.setter
    def country(self, new_country):
        """
        Set new country of registration
        :param new_country: new country of registration
        """
        if new_country.lower() == 'russia':
            raise ValueError('russia is terrorist organization. Only civilized countries are allowed.')
        self.__country = new_country

    @country.deleter
    def country(self):
        """ Delete country of registration"""
        raise NotImplementedError('It is not allowed to delete attribute Country')

    @property
    def headquarter(self):
        """Headquarter"""
        return self.__headquarter

    @headquarter.setter
    def headquarter(self, new_headquarter):
        """
        Set new location of headquarter
        :param new_headquarter: new location of headquarter
        """
        if new_headquarter == self.__headquarter:
            raise ValueError('Headquarter is already set to the indicated location')
        self.__headquarter = new_headquarter

    @property
    def founded(self):
        """Year of company's foundation"""
        return self.__founded

    @founded.setter
    def founded(self, new_founded):
        """
        Set new year of company's foundation
        :param new_founded: new year value
        """
        if not isinstance(new_founded, int):
            raise TypeError('Year foundation can only be an integer value')
        if new_founded > self.CURRENT_YEAR:
            raise ValueError('Year of foundation cannot be in the future')
        self.__founded = new_founded

    @property
    def ceo(self):
        """Company's CEO"""
        return self.__ceo

    @ceo.setter
    def ceo(self, new_ceo):
        """
        Set new CEO of company
        :param new_ceo: new name of company's CEO
        """
        if not all(x.isalpha() or x.isspace() for x in new_ceo):
            raise ValueError('CEO name can only contain letters and spaces')
        self.__ceo = new_ceo

    @property
    def employees(self):
        """Amount of employees"""
        return self.__employees

    @employees.setter
    def employees(self, new_employees):
        """
        Set new amount of employees
        :param new_employees: new amount of employees
        """
        if not isinstance(new_employees, int):
            raise TypeError('Amount of employees should be a integer number')
        if new_employees <= 0:
            raise ValueError('There should be at least one employees')
        self.__employees = new_employees

    @staticmethod
    def get_company_spread():
        """Get info if company is worldwide spread"""
        return 'Company is worldwide spread'

    @classmethod
    def create_fop_company(cls, name, country, headquarter, founded):
        """
        Construct a FOP company based on __init__
        :param name: FOP name
        :param country: Country of registration
        :param headquarter: City of registration
        :param founded: Year of registration
        :return: created company object with processed parameters
        """
        return cls(f'FOP {name}', country, headquarter, founded, name, 1)

    def print_company_article(self):
        """
        Function that returns short article about the company based on all input parameters
        """
        print(
            f'Full company info: \n'
            f'Company  {self.__name} was founded in {self.__country} in {self.__founded}. \n'
            f'Currently headquarter is located in {self.__headquarter}. \n'
            f'{self.__ceo} is now taking the position of Chief Executive Officer in {self.__name} company. \n'
            f'Total amount of employees in 2023 is {self.__employees} people')

    def get_company_age(self) -> int:
        """
        Function that calculates the age of the company based on year of foundation
        """
        return self.CURRENT_YEAR - self.__founded

    def is_company_in_faang(self) -> bool:
        """
        Function to check whether company is one of FAANG group
        :return: TRUE or FALSE
        """
        faang_list = ['Facebook', 'Apple', 'Amazon', 'Netflix', 'Google']
        return self.__name in faang_list

    def hire_employees(self, worker=1):
        """
        Function to hire one additional
        :param worker: amount of worker to hire. 1 by default
        """
        if worker <= 0:
            raise ValueError('Worker to hire should be positive value')
        self.__employees += worker

    def fire_employees(self, worker=1):
        """
        Function to fire specific amount of employees
        :param worker: amount of worker to fire. 1 by default
        """
        if worker <= 0:
            raise ValueError('Worker to fire should be positive value')
        if (self.employees - worker) == 0:
            return 'No more workers in Company. Was it closed?'
        if (self.employees - worker) < 0:
            raise ValueError('It\'s not possible to fire more employees than currently work in company')
        self.__employees -= worker


if __name__ == '__main__':
    # Set of tests for Company Class

    # Create an object of Class Company
    Toshiba = Company('Toshiba', 'Japan', 'Minato City', 1875, 'Taro Shimada', 116000)
    Apple = Company('Apple', 'USA', 'Cupertino', 1976, 'Tim Cook', 450000)

    # Check using name property to get value of name parameter
    assert Toshiba.name == 'Toshiba'
    assert Apple.name == 'Apple'

    # Check setter for name parameter
    # Test 1 - using setter to set name parameter with new valid value
    Toshiba.name = 'KIA'
    assert Toshiba.name == 'KIA'
    # Test 2 - using setter to set name parameter with invalid value - not only letters
    try:
        Toshiba.name = 'Test!@#'
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Company name can contain only letters'
    # Test 3 - using setter to set name parameter with invalid value - > 25 chars
    try:
        Toshiba.name = 'Sometextwithlongtexttwentyfivechars'
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Company length cannot be longer than 25 characters'

    # Check deleter for name parameter
    try:
        del Toshiba.name
    except NotImplementedError as e:
        assert e.__class__ is NotImplementedError
        assert e.args[0] == 'It is not allowed to delete Company name'

    # Check using country property to get value of country parameter
    assert Toshiba.country == 'Japan'
    assert Apple.country == 'USA'

    # Check setter for country parameter
    # Test 1 - using setter to set country parameter with new valid value
    Toshiba.country = 'Canada'
    assert Toshiba.country == 'Canada'
    # Test 2 - using setter to set country parameter with invalid value - only civilized country allowed
    try:
        Toshiba.country = 'russia'
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'russia is terrorist organization. Only civilized countries are allowed.'

    # Check deleter for country parameter
    try:
        del Apple.country
    except NotImplementedError as e:
        assert e.__class__ is NotImplementedError
        assert e.args[0] == 'It is not allowed to delete attribute Country'

    # Check using headquarter property to get value of headquarter parameter
    assert Toshiba.headquarter == 'Minato City'
    assert Apple.headquarter == 'Cupertino'

    # Check setter for headquarter parameter
    # Test 1 - using setter to set headquarter parameter with new valid value
    Toshiba.headquarter = 'Kyiv'
    assert Toshiba.headquarter == 'Kyiv'
    # Test 2 - using setter to set headquarter parameter with invalid value - already existing value
    try:
        Toshiba.headquarter = 'Kyiv'
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Headquarter is already set to the indicated location'

    # Check using founded property to get value of founded parameter
    assert Toshiba.founded == 1875
    assert Apple.founded == 1976

    # Check setter for founded parameter
    # Test 1 - using setter to set founded parameter with new valid value
    Toshiba.founded = 1888
    assert Toshiba.founded == 1888
    # Test 2 - using setter to set founded parameter with invalid value - not integer value
    try:
        Toshiba.founded = 'Twenty First century'
    except TypeError as e:
        assert e.__class__ is TypeError
        assert e.args[0] == 'Year foundation can only be an integer value'
    # Test 3 - using setter to set founded parameter with invalid value - from future
    try:
        Toshiba.founded = 2024
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Year of foundation cannot be in the future'

    # Check using ceo property to get value of ceo parameter
    assert Toshiba.ceo == 'Taro Shimada'
    assert Apple.ceo == 'Tim Cook'

    # Check setter for ceo parameter
    # Test 1 - using setter to set ceo parameter with new valid value
    Toshiba.ceo = 'Bohdan Dovbysh'
    assert Toshiba.ceo == 'Bohdan Dovbysh'
    # Test 2 - using setter to set ceo parameter with invalid value - with not only letters and spaces
    try:
        Toshiba.ceo = 'Some value with !@#$'
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'CEO name can only contain letters and spaces'

    # Check using employees property to get value of employees parameter
    assert Toshiba.employees == 116000
    assert Apple.employees == 450000

    # Check setter for employees parameter
    # Test 1 - using setter to set employees parameter with new valid value
    Toshiba.employees = 10000
    assert Toshiba.employees == 10000
    # Test 2 - using setter to set employees parameter with invalid value - not integer
    try:
        Toshiba.employees = 10.5
    except TypeError as e:
        assert e.__class__ is TypeError
        assert e.args[0] == 'Amount of employees should be a integer number'
    # Test 3 - using setter to set employees parameter with invalid value - 0 or less
    try:
        Toshiba.employees = 0
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'There should be at least one employees'

    # Check static method
    assert Company.get_company_spread() == 'Company is worldwide spread'

    # Check class method
    FOP_Albina = Company.create_fop_company('Albina Pasichnyk', 'Ukraine', 'Kyiv', 2015)
    assert FOP_Albina.name == 'FOP Albina Pasichnyk'
    assert FOP_Albina.ceo == 'Albina Pasichnyk'
    assert FOP_Albina.employees == 1

    # Check print_company_article function
    Apple.print_company_article()
    FOP_Albina.print_company_article()

    # Check get_company_age
    assert FOP_Albina.get_company_age() == 8

    # Check is_company_in_faang
    assert Toshiba.is_company_in_faang() is False
    assert Apple.is_company_in_faang() is True

    # Check hire_employees function
    # Test 1 - Check with default parameter
    Apple.hire_employees()
    assert Apple.employees == 450001
    # Test 2 - Check with valid parameter
    Apple.hire_employees(4)
    assert Apple.employees == 450005
    # Test 3 - Check negative value of parameter
    try:
        Apple.hire_employees(-5)
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Worker to hire should be positive value'

    # Check fire_employees function
    # Test 1 - Check with default parameter
    Apple.fire_employees()
    assert Apple.employees == 450004
    # Test 2 - Check with valid parameter
    Apple.fire_employees(4)
    assert Apple.employees == 450000
    # Test 3 - Check negative value of parameter
    try:
        Apple.fire_employees(-5)
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'Worker to fire should be positive value'
    # Test 4 - Check fire employee to 0
    assert FOP_Albina.fire_employees() == 'No more workers in Company. Was it closed?'
    # Test 5 - Check fire more employees than work
    try:
        FOP_Albina.fire_employees(5)
    except ValueError as e:
        assert e.__class__ is ValueError
        assert e.args[0] == 'It\'s not possible to fire more employees than currently work in company'
