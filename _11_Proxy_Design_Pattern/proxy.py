"""
PROXY DESIGN PATTERN 
====================

The code demonstrates the Proxy pattern. The NewJoineeProxy class acts as a
proxy for registering new joinees (employees). It performs additional checks
on the employees, such as their experience level before allowing them to join.

If an employee has less than 5 years of experience, they are not allowed to
join. This proxy pattern helps control and restrict the registration process
based on certain conditions.

Where as the NewJoinee class could add any employee without any checks.
NewJoinee class also, did not support list of employees to be registered.

Let's see the magic !

"""

from dataclasses import dataclass


@dataclass
class Employee:
    """Class representing an employee."""

    name: str
    age: int
    department: str
    experience: float

    def __str__(self) -> str:
        """Return a string representation of the employee."""
        return f'{self.name} aged {self.age} is from {self.department} with " + \
            {self.experience} years experience.'


@dataclass
class NewJoinee:
    """Class representing a new joinee."""

    emp: Employee

    def add_to(self, department):
        """Add the new joinee to a department."""
        self.emp.department = department

    def __str__(self) -> str:
        """Return a string representation of the new joinee."""
        return f'{self.emp.name} has joined {self.emp.department} with " + \
            {self.emp.experience} years experience.'


# INTRODUCING PROXY
# =================
# But now let's say I want to be able to allow register list of Employees
# And also dont allow them is their experience is less than 5 years.


@dataclass
class NewJoineeProxy(list):
    """Proxy class for controlling new joinee registration."""

    emp: Employee

    def __post_init__(self) -> None:
        """Perform additional initialization after object creation."""
        for e in self.emp:
            print(f"Checking details for : {e}")
            if e.experience <= 5.0:
                print(f'{e.name} has less than 5 years experience, cannot join')
                self.emp.remove(e)

    def add_to(self, department):
        """Add the new joinee to a department."""
        for employee in self.emp:
            if employee.experience >= 5.0:
                employee.department = department
            else:
                print(f'{employee.name} has less than 5 years experience, cannot join')
                self.emp.remove(employee)

    def __str__(self) -> str:
        """Return a string representation of the new joinee."""
        data = []
        return '\n'.join(str(employee) for employee in self.emp)


def main() -> None:
    """
    Main function to demonstrate both, Proxy and Non Proxy interface usage
    """
    emp1 = Employee("Amitabh", 31, "CEO", 10.0)
    print(emp1)

    join_ = NewJoinee(emp1)
    print(join_)

    # PROXY
    emp1 = Employee("Amitabh", 31, "CEO", 10.0)
    emp2 = Employee("Suman", 31, "BOD", 4)
    emp_l = [emp1, emp2]
    print(emp_l)

    join_ = NewJoineeProxy(emp_l)
    print(repr(join_))

    # As you can see that the interface remained same but the behaviour changed
    # entirely!


OUTPUT_NON_PROXY = r"""
>>> import proxy        
>>> from proxy import *
>>> emp1 = Employee("Amitabh", 31, "CEO", 10.0)
>>> print(emp1)
Amitabh aged 31 is from CEO with 10.0 years experience.
>>> join_ = NewJoinee(emp1)
>>> print(join_)
Amitabh has joined CEO with 10.0 years experience.
"""

OUTPUT_PROXY = r"""
>> import proxy        
>>> from proxy import *
>>> emp1 = Employee("Amitabh", 31, "CEO", 10.0)
>>> emp2 = Employee("Suman", 31, "CEO", 4.0)
>>> emp_l = [emp1, emp2]
>>> joine = NewJoineeProxy(emp_l) 
Checking details for : Amitabh aged 31 is from CEO with 10.0 years experience.
Checking details for : Suman aged 31 is from CEO with 4.0 years experience.
Suman has less than 5 years experience, cant not join
>>> print(repr(joine))
NewJoineeProxy(emp=[Employee(name='Amitabh', age=31, department='CEO', experience=10.0)])
>>>
"""

OUTPUT_PROXY_2 = r"""
>>> import proxy        
>>> from proxy import *
>>> emp1 = Employee("Amitabh", 31, "CEO", 10.0)
>>> emp2 = Employee("Suman", 31, "CEO", 4.0)
>>> emp2 = Employee("Suman", 31, "CEO", 11.0)
>>> emp2 = Employee("Suman", 31, "CEO", 4.0)  
>>> emp3 = Employee("Suman", 31, "CEO", 11.0)
>>> emp_l = [emp1, emp2, emp3]  
>>> print(emp_l)
[Employee(name='Amitabh', age=31, department='CEO', experience=10.0),
 Employee(name='Suman', age=31, department='CEO', experience=4.0),
 Employee(name='Suman', age=31, department='CEO', experience=11.0)]
>>> joine = NewJoineeProxy(emp_l)
Checking details for : Amitabh aged 31 is from CEO with 10.0 years experience.
Checking details for : Suman aged 31 is from CEO with 4.0 years experience.
Suman has less than 5 years experience, cannot join
>>> str(joine)
'Amitabh aged 31 is from CEO with 10.0 years experience.
 Suman aged 31 is from CEO with 11.0 years experience.'
>>> joine.add_to("CEO") 
>>> str(joine)
'Amitabh aged 31 is from CEO with 10.0 years experience.
 Suman aged 31 is from CEO with 11.0 years experience.'
>>> joine.add_to("CFO") 
>>> str(joine)
'Amitabh aged 31 is from CFO with 10.0 years experience.
 Suman aged 31 is from CFO with 11.0 years experience.'
>>> emp1.experience = 3.0
>>> joine.add_to("CFO")
Amitabh has less than 5 years experience, cannot join
>>> str(joine)
'Amitabh aged 31 is from CFO with 3.0 years experience.
 Suman aged 31 is from CFO with 11.0 years experience.'
"""
