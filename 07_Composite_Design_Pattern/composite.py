"""
COMPOSITE DESIGN PATTERN
========================

Composite pattern is a partitioning design pattern and describes a group of
objects that is treated the same way as a single instance of the same type of
object. The intent of a composite is to “compose” objects into tree structures
to represent part-whole hierarchies. It allows you to have a tree structure
and ask each node in the tree structure to perform a task.

As described by Gof:
“Compose objects into tree structure to represent part-whole hierarchies.
Composite lets client treat individual objects and compositions of objects
uniformly”.

When dealing with Tree-structured data, programmers often have to
discriminate between a leaf-node and a branch. This makes code more complex,
and therefore, error prone. The solution is an interface that allows treating
complex and primitive objects uniformly.

In object-oriented programming, a composite is an object designed as a
composition of one-or-more similar objects, all exhibiting similar
functionality. This is known as a “has-a” relationship between objects. The
key concept is that you can manipulate a single instance of the object just
as you would manipulate a group of them. The operations you can perform on
all the composite objects often have a least common denominator relationship.

The Composite Pattern has four participants:

1. Component : Component declares the interface for objects in the composition
and for accessing and managing its child components. It also implements
default behavior for the interface common to all classes as appropriate.

2. Leaf : Leaf defines behavior for primitive objects in the composition.
It represents leaf objects in the composition.

3. Composite : Composite stores child components and implements child related
operations in the component interface.

4. Client : Client manipulates the objects in the composition through the
component interface.

doc src : https://www.geeksforgeeks.org/composite-design-pattern/

Let's code this !

"""

# pylint: disable=too-few-public-methods
class Employee:
    """
    Represents an employee in an organization.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the Employee instance.

        Args:
            name (str): The name of the employee.
        """
        self.name = name
        self.reportees = []
        self.designation = "Manager"

    # pylint: disable=protected-access
    def _print(self, emps: str, depth: int) -> None:
        """
        Helper method to recursively print the employee hierarchy.

        Args:
            emps (str): List to store the formatted employee hierarchy.
            depth (int): Current depth level in the hierarchy.
        """
        emps.append(" - " * depth)
        if self.name:
            emps.append(self.name)
        emps.append(f' ({self.designation})\n')
        print(f"{depth} EMP(PRINT) : {emps}")
        for reportee in self.reportees:
            reportee._print(emps, depth + 1)

    def __str__(self) -> str:
        """
        Returns a string representation of the employee hierarchy.

        Returns:
            str: The formatted string representation of the employee hierarchy.
        """
        emps = []
        self._print(emps, 0)
        print(f"EMP(STR) : {emps}")
        return ''.join(emps)


# pylint: disable=too-few-public-methods
class Engineer(Employee):
    """
    Represents an engineer employee.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the Engineer instance.

        Args:
            name (str): The name of the engineer.
        """
        super().__init__(name)
        self.designation = "Engineer"


# pylint: disable=too-few-public-methods
class Architect(Employee):
    """
    Represents an architect employee.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize the Architect instance.

        Args:
            name (str): The name of the architect.
        """
        super().__init__(name)
        self.designation = "Architect"


def main():
    """
    Main function
    """
    emp = Employee("Amitabh")
    emp1 = Engineer("Shweta")
    emp2 = Architect("Suman")
    emp.reportees.append(emp1)
    emp.reportees.append(emp2)

    emp3 = Employee("Aadya")
    emp3.reportees.append(Engineer("Chota Dhruv"))
    emp3.reportees.append(Architect("Dhruv"))
    emp.reportees.append(emp3)

    print(emp)

if __name__ == '__main__':
    main()


OUTPUT = r"""
>>> import composite        
>>> from composite import *
>>> main()
0 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n'
    ]
1 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n'
    ]
1 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n', ' - ', 
    'Suman', ' (Architect)\n'
    ]
1 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n', ' - ',
    'Suman', ' (Architect)\n', ' - ', 'Aadya', ' (Manager)\n'
    ]
2 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n', ' - ',
    'Suman', ' (Architect)\n', ' - ', 'Aadya', ' (Manager)\n', ' -  - ',
    'Chota Dhruv', ' (Engineer)\n'
    ]
2 EMP(PRINT) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n', ' - ',
    'Suman', ' (Architect)\n', ' - ', 'Aadya', ' (Manager)\n', ' -  - ',
    'Chota Dhruv', ' (Engineer)\n', ' -  - ', 'Dhruv', ' (Architect)\n'
    ]
EMP(STR) : [
    '', 'Amitabh', ' (Manager)\n', ' - ', 'Shweta', ' (Engineer)\n', ' - ',
    'Suman', ' (Architect)\n', ' - ', 'Aadya', ' (Manager)\n', ' -  - ',
    'Chota Dhruv', ' (Engineer)\n', ' -  - ', 'Dhruv', ' (Architect)\n'
    ]
Amitabh (Manager)
 - Shweta (Engineer)
 - Suman (Architect)
 - Aadya (Manager)
 -  - Chota Dhruv (Engineer)
 -  - Dhruv (Architect)

"""