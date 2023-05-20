"""
The Prototype Design Pattern is a Creational Design Pattern that allows
cloning and creating new instances of an existing object without relying
on subclassing. It provides a way to create objects based on an existing
prototype object, thus avoiding the costly process of creating objects
from scratch.

One most common example is that use of cloning a SQL database object that
references to other objects from other tables. Creating another object can
and will be a costly process. Hence, we can use prototying there. Nonetheless,
below is the example for a simple Prototype use case.

In the below code piece writtne, we have two classes:
1. Capabilities : The class Capabilities represents the capabilities of a
   Game character
2. GameCharacter : GameCharacter class represents a game character with a
   name, power, and set of capabilities.

"""

class Capabilities:
    """
    Represents the capabilities of a Game character genrated at runtime.
    
    Attributes:
        **kwargs: Keyword arguments representing the capabilities and their values.
    """
    def __init__(self, **kwargs) -> None:
        """
        Initializes the capabilities of a game character.
        
        Args:
            **kwargs: Keyword arguments representing the capabilities and their values.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the capabilities.
        
        Returns:
            str: String representation of the capabilities.
        """
        attributes = vars(self)  # Get dictionary of object's attributes
        attribute_list = [f'{k}={v}' for k, v in attributes.items()]
        return f'Capabilities: {", ".join(attribute_list)}'


class GameCharacter:
    """
    Represents a game character with various attributes.
    
    Attributes:
        name (str): The name of the game character.
        power (str): The power of the game character.
        capabilities (Capabilities): The capabilities of the game character.
    """
    def __init__(self, name: str, power: str, capabilities: Capabilities) -> None:
        """
        Initializes a game character with a name, power, and capabilities.
        
        Args:
            name (str): The name of the game character.
            power (str): The power of the game character.
            capabilities (Capabilities): The capabilities of the game character.
        """
        self.name = name
        self.power = power
        self.capabilities = capabilities
    
    def __str__(self) -> str:
        """
        Returns a string representation of the game character.
        
        Returns:
            str: String representation of the game character.
        """
        return f'{self.name} has {self.power} powers with {self.capabilities}'



OUTPUT = r"""
>>> import prototype        
>>> from prototype import *
>>> cap = Capabilities(power="Ultra Smart", speed="Ultra Fast")
>>> str(cap)
'Capabilities: power=Ultra Smart, speed=Ultra Fast'
>>> c1 = GameCharacter("Ragnar", "Immortal", cap)      
>>> c1
<prototype.GameCharacter object at 0x0000017835A9D2E0>
>>> str(c1)
'Ragnar has Immortal powers with Capabilities: power=Ultra Smart, speed=Ultra Fast'
>>> cap1 = c1.capabilities
>>> cap1.power = "Ultra A Smart"
>>> c2
<prototype.GameCharacter object at 0x0000017835A9D4C0>
>>> str(c2)
'Ragnar has Immortal powers with Capabilities: power=Ultra Smart, speed=Ultra Fast'
>>> str(c1)
'Ragnar has Immortal powers with Capabilities: power=Ultra A Smart, speed=Ultra Fast'
>>> c2 = c1                                     
>>> str(c1)
'Ragnar has Immortal powers with Capabilities: power=Ultra A Smart, speed=Ultra Fast'
>>> str(c2) 
'Ragnar has Immortal powers with Capabilities: power=Ultra A Smart, speed=Ultra Fast'
>>> c2.capabilities.power = "Ultra B Smart"
>>> str(c1)
'Ragnar has Immortal powers with Capabilities: power=Ultra B Smart, speed=Ultra Fast'
>>>
>>> import copy
>>> from copy import deepcopy
>>> c2 = deepcopy(c1)
>>> print (c1==c2)
False
>>> c1.capabilities.power = "Ultra C Smart"
>>> str(c1)
'Ragnar has Immortal powers with Capabilities: power=Ultra C Smart, speed=Ultra Fast'
>>> str(c2) 
'Ragnar has Immortal powers with Capabilities: power=Ultra B Smart, speed=Ultra Fast'
>>>
"""