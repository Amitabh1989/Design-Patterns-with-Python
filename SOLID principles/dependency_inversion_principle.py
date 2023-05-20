"""
To adhere to the principle of dependency inversion (the D in SOLID), we need
to ensure that high-level modules do not depend on low level modules, but
instead depend on abstractions. The abstraction should not depend on details,
instead the details should depend on abstractions.
"""

import abc

# ==============================================
# BREACH OF PRINCIPLE
# ==============================================

class SaveData(abc.ABC):
    
    def __init__(self) -> None:
        self.db_obj = object()  # Object for an imaginary DataBaseClass

    def save_data(self, data: str) -> bool:
        self.db_obj.save()
        return True
    
class Person():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        self.save_obj = SaveData()
    
    def __str__(self) -> str:
        return f'{self.name} is aged {self.age} years and has a salary of \
            INR {self.salary}'

    def save(self, data: str) -> bool:
        return self.save_obj.save_data(data)

# As you can see here that the class Person needs to save the data using 
# the save function from class SaveData.
# But there are so many things wromg here
# 1. Violation of SRP
# 2. Tomorrow if the save_data method changes, then the save() from class
#    Person will break. So let's fix this.


# ==============================================
# ADHERE TO THE PRINCIPLE
# ==============================================

import abc

class DataHandler(abc.ABC):
    """
    Abstract base class for data handling.
    """
    
    @abc.abstractmethod
    def save_data(self):
        """
        Abstract method to save data.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError

class SaveData(DataHandler):
    """
    Class for saving data using an imaginary database object.
    """

    def __init__(self) -> None:
        """
        Initialize the SaveData object.
        """
        self.db_obj = object()  # Object for an imaginary DataBaseClass

    def save_data(self, data: str) -> bool:
        """
        Save data using the imaginary database object.

        Args:
            data (str): The data to be saved.

        Returns:
            bool: True if the data is saved successfully, False otherwise.
        """
        self.db_obj.save()
        return True

class Person(SaveData):
    """
    Class representing a person.

    Args:
        name (str): The name of the person.
        age (int): The age of the person.
        salary (float): The salary of the person.
    """

    def __init__(self, name: str, age: int, salary: float) -> None:
        """
        Initialize a Person object.

        Args:
            name (str): The name of the person.
            age (int): The age of the person.
            salary (float): The salary of the person.
        """
        super().__init__()
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self) -> str:
        """
        Return a string representation of the person.

        Returns:
            str: A string representation of the person.
        """
        return f'{self.name} is aged {self.age} years and has a salary of INR {self.salary}'

    def save(self, data: str) -> bool:
        """
        Save the person's data.

        Args:
            data (str): The data to be saved.

        Returns:
            bool: True if the data is saved successfully, False otherwise.
        """
        return self.save_data(data)
