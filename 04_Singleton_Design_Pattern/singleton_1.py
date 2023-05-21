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
# 1. ALLOCATOR IMPLEMENTATION
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

# You will see that the INIT is run for n nujmber of times, based on number of
# objects created. Verify this with the run. Output at end of the program
# Let's solve this with decorators and the using Metaclass.

# ==============================================
# 2. DECORATOR IMPLEMENTATION
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
# 3. METACLASS IMPLEMENTATION (uses __call__)
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

OUTPUT = r"""
>>> import singleton_1
Hello from the Database, id 38
Hello from the Database, id 55
True
---
Hello from the Database, id 7
True
---
Hello from the Database, id 56
True
---
"""


"""
READ : DIFFERENCE BETWEEN __new__ and __call__

The `__new__` and `__call__` methods in Python have different purposes and
behaviors:

1. `__new__` method: ==> Come to play when class in INHERITED
    1. The `__new__` method is a special method that is responsible for creating
       and returning a new instance of a class.
    2. It is a static method that is called before the `__init__` method.
    3, Its primary purpose is to allocate and initialize the memory required for
       a new object.
    4. The `__new__` method takes the class as its first argument (`cls`) and
       returns a newly created instance of that class.
    5. You can override the `__new__` method to customize the object creation
       process, such as returning an existing instance instead of creating a
       new one (e.g., for implementing a singleton pattern).

2. `__call__` method: ==> Comes to play when class is used as METACLASS
    1. The `__call__` method allows an object of a class to be called as a
       function.
    2. It provides the functionality of making an instance of a class callable
       like a regular function.
    3. When an instance is called as a function, the `__call__` method of the
       class is invoked.
    4. The `__call__` method can take arguments like a regular function, and you
       can define its behavior based on those arguments.
    5. It can be useful for creating callable objects or implementing callable
       classes that can be invoked directly.

In summary, `__new__` is responsible for object creation, while `__call__`
allows objects to be called as functions. They serve different purposes in 
the object-oriented programming model of Python.
"""
