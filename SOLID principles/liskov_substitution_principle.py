"""
The Liskov substitution principle states that a child class must be
substitutable for its parent class. Liskov substitution principle aims to 
ensure that the child class can assume the place of its parent class without
causing any errors.
"""

import abc

# ==============================================
# BREACH OF PRINCIPLE
# ==============================================
# Here, class Ostrich does not reflect its parent class Bird completely.
# We have to bypass a method fly in order to implement this. Which is a
# violation of the principle.

class Bird(abc.ABC):
    """
    Abstract base class for birds.

    Args:
        name (str): The name of the bird.
        size (str): The size of the bird.
    """

    def __init__(self, name: str, size: str) -> None:
        """
        Initialize a bird object.

        Args:
            name (str): The name of the bird.
            size (str): The size of the bird.
        """
        self.name = name
        self.size = size

    def __str__(self) -> str:
        """
        Return a string representation of the bird.

        Returns:
            str: A string representation of the bird.
        """
        print(f"{self.name} is a {self.size} bird!")
        return f"{self.name} is a {self.size} bird!"

    # pylint: disable=unnecessary-pass
    @abc.abstractmethod
    def fly(self):
        """
        Abstract method to simulate the bird's flight.

        This method must be implemented by the derived classes.
        """
        pass


class Eagle(Bird):
    """
    Class representing an eagle.

    Args:
        name (str): The name of the eagle.
        size (str): The size of the eagle.
    """

    def __init__(self, name: str, size: str) -> None:
        """
        Initialize an eagle object.

        Args:
            name (str): The name of the eagle.
            size (str): The size of the eagle.
        """
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    def fly(self):
        """
        Simulate the eagle's flight.

        Prints a message indicating that the eagle is flying.
        """
        print(f"{self.name} is a {self.size} bird and it's flying now")


class Ostrich(Bird):
    """
    Class representing an ostrich.

    Args:
        name (str): The name of the ostrich.
        size (str): The size of the ostrich.
    """

    def __init__(self, name: str, size: str) -> None:
        """
        Initialize an ostrich object.

        Args:
            name (str): The name of the ostrich.
            size (str): The size of the ostrich.
        """
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    # pylint: disable=unnecessary-pass
    def fly(self):
        """
        Method representing that the ostrich cannot fly.

        This method is empty as ostriches cannot fly.
        """
        pass



eagle = Eagle("Duniya Ka Rakshak", "medium")
ostrich = Ostrich("Dino ka Chota Bhai", "large")

str(eagle)
str(ostrich)

eagle.fly()
ostrich.fly()

OUTPUT_1 = r"""
>>> import liskov_substitution_principle
Duniya Ka Rakshak is a medium bird!
Dino ka Chota Bhai is a large bird!
>>> import liskov_substitution_principle
>>> from liskov_substitution_principle import Eagle, Ostrich   
>>> eagle = Eagle("Duniya Ka Rakshak", "medium")
>>> ostrich = Ostrich("Dino ka Chota Bhai", "large")
>>>
>>> eagle.fly()
Duniya Ka Rakshak is a medium bird and its flying now
>>> ostrich.fly() 
>>>
"""

# ==============================================
# ADHERE TO THE PRINCIPLE
# ==============================================
# Here, class Ostrich does not reflect its parent class Bird completely.
# We have to bypass a method fly in order to implement this. Which is a
# violation of the principle.


class BirdNew(abc.ABC):
    """
    Abstract base class for birds.

    Args:
        name (str): The name of the bird.
        size (str): The size of the bird.

    Attributes:
        name (str): The name of the bird.
        size (str): The size of the bird.
    """

    def __init__(self, name: str, size: str) -> None:
        self.name = name
        self.size = size

    def __str__(self) -> str:
        """
        Get a string representation of the bird.

        Returns:
            str: The string representation of the bird.
        """
        return f"{self.name} is a {self.size} bird!"


class FlyingBird(Bird):
    """
    Class representing a flying bird.

    Args:
        name (str): The name of the bird.
        size (str): The size of the bird.
    """

    def __init__(self, name: str, size: str) -> None:
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    def fly(self):
        """
        Simulate the bird's flight.

        Prints a message indicating that the bird is flying.
        """
        print(f"{self.name} is a {self.size} bird and it's flying now")


class NonFlyingBird(Bird):
    """
    Class representing a non-flying bird.

    Args:
        name (str): The name of the bird.
        size (str): The size of the bird.
    """

    def __init__(self, name: str, size: str) -> None:
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    def walk(self):
        """
        Print a message indicating that the bird is walking.
        """
        print(f"{self.name} is a {self.size} bird and it is walking now")


class EagleNew(FlyingBird):
    """
    Class representing an eagle.

    Args:
        name (str): The name of the eagle.
        size (str): The size of the eagle.
    """

    def __init__(self, name: str, size: str) -> None:
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    def fly(self):
        """
        Simulate the eagle's flight.

        Prints a message indicating that the eagle is flying.
        """
        print(f"{self.name} is a {self.size} bird and it's flying now")


class OstrichNew(NonFlyingBird):
    """
    Class representing an ostrich.

    Args:
        name (str): The name of the ostrich.
        size (str): The size of the ostrich.
    """

    def __init__(self, name: str, size: str) -> None:
        # pytlint: disable=useless-parent-delegation
        super().__init__(name, size)

    def walk(self):
        """
        Method representing that the ostrich cannot fly.

        This method is empty as ostriches cannot fly.
        """
        # print(f"{self.name} is a {self.size} bird and it's walking now")
        return super().walk()


OUTPUT_2 = r"""
>>> from liskov_substitution_principle import EagleNew, OstrichNew   
Duniya Ka Rakshak is a medium bird!
Dino ka Chota Bhai is a large bird!
Duniya Ka Rakshak is a medium bird and its flying now
>>>
>>> e = EagleNew("Cheel", "bada")
>>> o = OstrichNew("SuturMurg", "bahut bada")
>>>
>>> str(e)
Cheel is a bada bird!
'Cheel is a bada bird!'
>>> str(o) 
SuturMurg is a bahut bada bird!
'SuturMurg is a bahut bada bird!'
>>> e.fly()
Cheel is a bada bird and it's flying now
>>> o.walk()
SuturMurg is a bahut bada bird and it is walking now
>>>
"""
