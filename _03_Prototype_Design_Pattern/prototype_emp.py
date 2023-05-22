"""
PROTOTYPE DESIGN PATTERN

THis pattern focuses on using an object as a prototype and model it into
various "deep" copies of the object in order to use objects uniquely. 

IN cases when object creation is a costly process, Prototype is a way to
make it quicker. "Deep" copy the object and make a unique object by
customizing the object attributes as per your need.
"""

from copy import deepcopy

# pylint: disable=too-few-public-methods
class Employee:
    """
    Class representing an employee.
    """

    def __init__(self, name: str, address: str) -> None:
        """
        Initialize an employee object.

        Args:
            name (str): The name of the employee.
            address (str): The address of the employee.
        """
        self.name = name
        self.address = address

    def __str__(self) -> str:
        """
        Return a string representation of the employee.

        Returns:
            str: A string representation of the employee.
        """
        return f'{self.name} lives at {self.address}'

# pylint: disable=too-few-public-methods
class Address:
    """
    Class representing an address.
    """

    def __init__(self, street: str, road: str, country: str) -> None:
        """
        Initialize an address object.

        Args:
            street (str): The street name.
            road (str): The road name.
            country (str): The country name.
        """
        self.street = street
        self.road = road
        self.country = country

    def __str__(self) -> str:
        """
        Return a string representation of the address.

        Returns:
            str: A string representation of the address.
        """
        return f'{self.street}, {self.road}, {self.country}'


class EmployeeFactory:
    """
    Factory class for creating different types of employees.
    """

    engineer = Employee("", Address("Engineering Block", "Engineering Road", "India"))
    itsupport = Employee("", Address("Support Block", "Support Road", "India"))

    @staticmethod
    def __new_employee(proto, name, road):
        result = deepcopy(proto)
        result.name = name
        result.address.road = road
        return result

    @staticmethod
    def new_engineering_emp(name: str, road: str) -> Employee:
        """
        Create a new engineering employee.

        Args:
            name (str): The name of the employee.
            road (str): The road name of the employee's address.

        Returns:
            Employee: A new engineering employee object.
        """
        return EmployeeFactory.__new_employee(
            EmployeeFactory.engineer, name, road
        )

    @staticmethod
    def new_itsupport_emp(name: str, road: str) -> Employee:
        """
        Create a new IT support employee.

        Args:
            name (str): The name of the employee.
            road (str): The road name of the employee's address.

        Returns:
            Employee: A new IT support employee object.
        """
        return EmployeeFactory.__new_employee(
            EmployeeFactory.itsupport, name, road
        )


# Create engineering employee
emp_eng = EmployeeFactory.new_engineering_emp("Amitabh", "Kings")
print(str(emp_eng))

# Create IT support employee
emp_it = EmployeeFactory.new_itsupport_emp("Suman", "Charles")
print(str(emp_it))
