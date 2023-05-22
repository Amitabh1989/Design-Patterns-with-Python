"""
BRIDGE DESIGN PATTERN

The Bridge design pattern allows you to separate the abstraction from the
implementation. It is a structural design pattern. 

There are 2 parts in Bridge design pattern : 

1. Abstraction
2. Implementation

This is a design mechanism that encapsulates an implementation class inside
of an interface class.  

1. The bridge pattern allows the Abstraction and the Implementation to be
developed independently and the client code can access only the Abstraction
part without being concerned about the Implementation part.

2. The abstraction is an interface or abstract class and the implementer is
also an interface or abstract class.

3. The abstraction contains a reference to the implementer.
Children of the abstraction are referred to as refined abstractions, and
children of the implementer are concrete implementers. Since we can change
the reference to the implementer in the abstraction, we are able to change
the abstraction’s implementer at run-time. Changes to the implementer do not
affect client code.

4. It increases the loose coupling between class abstraction and it’s
implementation.

"""

import abc


# pylint: disable=too-few-public-methods
class Employee(abc.ABC):
    """Abstract base class for an employee."""

    def __init__(self, name, department) -> None:
        """Initialize the Employee object."""
        self.name = name
        self.department = department

    def __str__(self) -> str:
        """Return a string representation of the employee."""
        return f'{self.name} is from {self.department} department.'


# pylint: disable=too-few-public-methods
class Engineer(Employee):
    """Concrete class representing an engineer."""

    def __init__(self, name, department, role) -> None:
        """Initialize the Engineer object."""
        super().__init__(name, department)
        self.role = role

    def __str__(self) -> str:
        """Return a string representation of the engineer."""
        return f'{super().__str__()} Role is {self.role}'


# pylint: disable=too-few-public-methods
class Support(Employee):
    """Concrete class representing a support employee."""

    def __init__(self, name, department, role) -> None:
        """Initialize the Support object."""
        super().__init__(name, department)
        self.role = role

    def __str__(self) -> str:
        """Return a string representation of the support employee."""
        return f'{super().__str__()} Role is {self.role}'


# pylint: disable=too-few-public-methods
class EmployeeInfo(abc.ABC):
    """Abstract base class for obtaining employee information."""

    def __init__(self, employee) -> None:
        """Initialize the EmployeeInfo object."""
        self.employee = employee

    # pylint: disable=unnecessary-pass
    @abc.abstractmethod
    def get_info(self):
        """Abstract method to get employee information."""
        pass


# pylint: disable=too-few-public-methods
class SalaryInfo(EmployeeInfo):
    """Concrete class for obtaining salary information."""

    def __init__(self, employee, salary) -> None:
        """Initialize the SalaryInfo object."""
        super().__init__(employee)
        self.salary = salary

    def get_info(self):
        """Get the salary information for the employee."""
        return f'{self.employee.name} has a salary of USD {self.salary}'


# pylint: disable=too-few-public-methods
class RoleInfo(EmployeeInfo):
    """Concrete class for obtaining role information."""

    def get_info(self):
        """Get the role information for the employee."""
        return f'{self.employee.name} has a role {self.employee.role}'


if __name__ == '__main__':
    eng_emp = Engineer("Amitabh", "SWD", "eng")
    it_emp = Support("Charles", "IT_2", "it")
    print(eng_emp, it_emp, sep='\n')
    eng_emp.role = "Senior SWD"
    print(eng_emp, it_emp, sep='\n')
    emp_info = SalaryInfo(eng_emp, 1000000000000000000)
    print(eng_emp, it_emp, sep='\n')
    emp_info_role = RoleInfo(eng_emp)
    print(eng_emp, it_emp, sep='\n')
    print(emp_info.get_info(), emp_info_role.get_info(), sep='\n')


OUTPUT = r"""
Amitabh is from SWD department. Role is eng
Charles is from IT_2 department. Role is it
Amitabh is from SWD department. Role is Senior SWD
Charles is from IT_2 department. Role is it
Amitabh is from SWD department. Role is Senior SWD
Charles is from IT_2 department. Role is it
Amitabh is from SWD department. Role is Senior SWD
Charles is from IT_2 department. Role is it
Amitabh has a salary of USD1000000000000000000
Amitabh has a role Senior SWD
"""
