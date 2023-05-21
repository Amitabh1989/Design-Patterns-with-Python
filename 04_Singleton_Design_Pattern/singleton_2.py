"""
SINGLETON DESIGN PATTERN

Perhaps the most disliked design pattern and I dont really know WHY!
It has its own utility when we want to have only 1 copy of the object. This
can be useful in many scenarios where we want to share a common object to
avoid objects over-writing or making local copies of unshared data, which we
need to mandate. 

So all in all, we will find pretty significant application of this design
pattern all around us.

Nonetheless. Let's explore a new type of implementation for Singleton classes.
We haev seen 3 different ways to invoke Singleton classes in previous files.
Now, let's see this new implementation : MONOSTATE

4. MONOSTATE : Works with the concept of the shared data in a private class
variable / dict. And then slaping it with a Monostate metaclass.

Let's see the implementation here.

"""

from typing import Any, TypeVar

# =================================================
# 4. MONOCLASS IMPLEMENTATION (uses __shared_data)
# =================================================

# pylint: disable=too-few-public-methods
class Singleton:
    """
    Implements the idea of shared private dictionary that gets copied and
    hence shared between all objects. __shared_data here is a name mangled
    variable. Hence can not be used directly by the class objects.
    """
    __shared_data = {
        "name": "Amitabh",
        "designation": "CEO"
    }

    def __init__(self) -> None:
        """
        This implementation over-rides the __dict__ with the shared data.
        """
        self.__dict__ = self.__shared_data

    # pylint: disable=no-member
    def __str__(self) -> str:
        """
        String representation of the class object.
        """
        return f"{self.name} is the {self.designation} of the company!"

# if __name__ == '__main__':
#     ceo1 = Singleton()
#     print(ceo1)

#     ceo2 = Singleton()
#     ceo2.name = "Amitabh Suman"
#     print(f"CEO 1 : {ceo1}")
#     print(f"CEO 2 : {ceo2}")

OUTPUT_1 = r"""
>>> import singleton_2
>>> from singleton_2 import *
>>> p1 = Singleton()
>>> p1
<singleton_2.Singleton object at 0x0000015F9C51D340>
>>> str(p1)
'Amitabh is the CEO of the company!'
>>> p2 = Singleton()
>>> p2
<singleton_2.Singleton object at 0x0000015F9C5A2C70>
>>> str(p2)
'Amitabh is the CEO of the company!'
>>> p2.name = "Amitabh Suman"
>>> p2.designation = "Owner"
>>> str(p1) 
'Amitabh Suman is the Owner of the company!'
>>> str(p2) 
'Amitabh Suman is the Owner of the company!'
>>>
"""


# =================================================
# 5. MONOCLASS IMPLEMENTATION (uses inheritance)
# =================================================

Self = TypeVar("Self", bound="Monostate")

# pylint: disable=too-few-public-methods
class Monostate:
    """
    NOTE the difference here. This implementation sure does gives you a
    different object each time you create an instance. But all of them will be
    sharing the data capturedas part of the "_shared_data" dictionary.
    
    Kindly make a note of how the "__dict__" has been overwritten with the 
    _shared_data to mandate all objects sharing the data.

    Dict here is a private dictionary.
    """
    _shared_data = {}

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_data
        return obj


# pylint: disable=too-few-public-methods
class SingletonNew(Monostate):
    """
    This class inherits the Monostate class which then over-rides the __new__
    method of this class and makes sure all objects have the shared dict.
    """

    def __init__(self) -> None:
        self.name = ""
        self.position = "CEO"

    def __str__(self) -> str:
        return f'{self.name} is a {self.position} in the company!'

if __name__ == '__main__':
    person1 = SingletonNew()
    print(person1)

    person2 = SingletonNew()
    person1.name = "Amitabh Suman"
    print(f"PERSON 1 : {person1}")
    print(f"PERSON 2 : {person2}")


OUTPUT_2 = r"""
>>> import singleton_2                   
>>> from singleton_2 import *
>>> p1 = SingletonNew()
>>> p1.name = "Amitabh"
>>> p1.position = "Owner"
>>> str(p1)
'Amitabh is a Owner in the company!'
>>>
>>>
>>> p2 = SingletonNew()
>>> p2.position = "GodFather"
>>>
>>> str(p1)
' is a GodFather in the company!'
>>> p2.name
''
>>> p1.name          
''
>>> p2.name = "Amitabh"
>>> str(p1)
'Amitabh is a GodFather in the company!'
>>> str(p2) 
'Amitabh is a GodFather in the company!'
>>>
"""
