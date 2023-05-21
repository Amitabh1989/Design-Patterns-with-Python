"""
SINGLETON DESIGN PATTERN

Perhaps the most disliked design pattern and I dont really know WHY!
It has its own utility when we want to have only 1 copy of the object. This
can be useful in many scenarios where we want to share a common object to
avoid objects over-writing or making local copies of unshared data, which we
need to mandate. 

So all in all, we will find pretty significant application of this design
pattern all around us.

Nonetheless. Let's explore the types here
1. DataBase  : Represent Singleton ALLOCATOR implementation
2. DataBase1 : Represents using DECORATORS to apply singleton concept
3. DataBase2 : Represents usage of METACLASSES for applying singleton

"""

from typing import Any, TypeVar
import random


# ==============================================
# ALLOCATOR IMPLEMENTATION
# ==============================================

Self = TypeVar("Self", bound="DataBase")

# pylint: disable=too-few-public-methods
class DataBase:
    """
    Singleton class representing a database. Using ALLOCATOR implementation.
    """

    _instance: Self = None

    def __new__(cls: type[Self], *args: Any, **kwargs: Any) -> Self:
        """
        Create a new instance of the class if it doesn't exist already.

        Args:
            cls (type[Self]): The class type.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Self: The instance of the class.

        """
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self) -> None:
        """
        Initialize the database.

        Prints a greeting message with a random ID.
        """
        print(f"Hello from the Database, id {random.randint(1, 100)}")

# Create instances of the database
d1 = DataBase()
d2 = DataBase()
print(d1 == d2)
print("---")


# ==============================================
# DECORATOR IMPLEMENTATION
# ==============================================

Self = TypeVar("Self", bound="DataBase2")

def singleton(class_):
    """
    Function used a decorator that takes in a class and checks for the
    instance. If instance is available, return it else create a new

    Args:
        class_ (class): The class for which we need single instance only.

    Returns:
        object: Object of the class decorated.
    """
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return get_instance

# pylint: disable=too-few-public-methods
@singleton
class DataBase2:
    """
    Singleton class representing a database. Using DECORATOR implementation
    """

    def __init__(self) -> None:
        """
        Initialize the database.

        Prints a greeting message with a random ID.
        """
        print(f"Hello from the Database, id {random.randint(1, 100)}")

# Create instances of the database
d3 = DataBase2()
d4 = DataBase2()
print(d3 == d4)
print("---")


# ==============================================
# METACLASS IMPLEMENTATION
# ==============================================

# Singleton Metaclass
# pylint: disable=too-few-public-methods
class SingletonClass(type):
    """
    Implements docstring as a METACLASS. The derived class/child class
    inherits this class as metaclass. This class then invoke the __call__
    method 
    """
    _instances = {}

    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonClass, cls).__call__(*args, **kwds)
        return cls._instances[cls]


# pylint: disable=too-few-public-methods
class DataBase3(metaclass=SingletonClass):
    """
    Singleton class representing a database.
    """

    def __init__(self) -> None:
        """
        Initialize the database.

        Prints a greeting message with a random ID.
        """
        print(f"Hello from the Database, id {random.randint(1, 100)}")

# Create instances of the database
d5 = DataBase3()
d6 = DataBase3()
print (d5 == d6)
print("---")
