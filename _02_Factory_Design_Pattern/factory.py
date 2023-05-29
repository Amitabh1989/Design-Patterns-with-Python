"""
Factory Design Pattern

The code below demonstrates the Factory Method design pattern. It follows the
basic structure of the Factory Method pattern, where we have a factory class
(Factory) responsible for creating objects of different types based on a given
parameter (num_wheels in this case).

The factory class Factory has a build_vehicle() method that acts as the
factory method. It takes the name and num_wheels parameters and returns
an instance of the corresponding vehicle class (Bike, TriCycle, or Car)
based on the value of num_wheels.

Each vehicle class (Car, Bike, and TriCycle) has its own build_vehicle()
method that returns a string representing the construction of the vehicle.

Overall, this code demonstrates the Factory Method pattern by encapsulating
the object creation logic in the Factory class, allowing the client code to
create different types of vehicles without directly knowing the specific
vehicle class to instantiate.

Think manually : We have a Car manufacturing factory.

And the company has 4 models of cars. Its pretty obvious that it may not
have 4 factories for 4 cars. You would want to optimize your resource usage
and build all cars (well, are you planning of FLYING CARS too? ;-) )!

So factory provides a uniform interface and internally invokes required
classes to cater to the request. User just needs to order the car and the
factory will return the ready Car.

Enjoy your drive!

"""

# pylint: disable=R0903
class Car:
    """
    Creates a Car based on name and number of wheels
    """

    def __init__(self, name: str, num_wheels: int) -> None:
        """
        Initialize a Car object.

        Args:
            name (str): The name of the car.
            num_wheels (int): The number of wheels on the car.
        """
        self.name = name
        self.num_wheels = num_wheels

    def build_vehicle(self) -> str:
        """
        Build the car and return a string representing the construction.

        Returns:
            str: A string representing the construction of the car.
        """
        return f"Your {self.name} {type(self).__name__} with \
            {self.num_wheels} wheels is ready!"


# pylint: disable=R0903
class Bike:
    """
    Creates a Bike based on name and number of wheels
    """

    def __init__(self, name: str, num_wheels: int) -> None:
        """
        Initialize a Bike object.

        Args:
            name (str): The name of the bike.
            num_wheels (int): The number of wheels on the bike.
        """
        self.name = name
        self.num_wheels = num_wheels

    def build_vehicle(self) -> str:
        """
        Build the bike and return a string representing the construction.

        Returns:
            str: A string representing the construction of the bike.
        """
        return f"Your {self.name} {type(self).__name__} with \
            {self.num_wheels} wheels is ready!"


# pylint: disable=R0903
class TriCycle:
    """
    Creates a Tricycle based on name and number of wheels
    """

    def __init__(self, name: str, num_wheels: int) -> None:
        """
        Initialize a TriCycle object.

        Args:
            name (str): The name of the tricycle.
            num_wheels (int): The number of wheels on the tricycle.
        """
        self.name = name
        self.num_wheels = num_wheels

    def build_vehicle(self) -> str:
        """
        Build the tricycle and return a string representing the construction.

        Returns:
            str: A string representing the construction of the tricycle.
        """
        return f"Your {self.name} {type(self).__name__} with \
            {self.num_wheels} wheels is ready!"


class Factory:
    """
    A Factory class that determine what objects will get created based on the
    request made for the vehicle. Here, dictating feeature is number of wheels
    """

    def __init__(self, name: str, num_wheels: int) -> None:
        """
        Initialize a Factory object.

        Args:
            name (str): The name of the vehicle.
            num_wheels (int): The number of wheels on the vehicle.
        """
        self.name = name
        self.num_wheels = num_wheels

    def build_vehicle(self) -> object:
        """
        Build the vehicle based on the number of wheels and return the
        corresponding object.

        Returns:
            object: An instance of the corresponding vehicle class.
        """
        if self.num_wheels == 2:
            return Bike(self.name, self.num_wheels)
        if self.num_wheels == 3:
            return TriCycle(self.name, self.num_wheels)
        if self.num_wheels == 4:
            return Car(self.name, self.num_wheels)

OUTPUT = r"""
>>> import factory
>>> from factory import *
>>> ob = Factory("Chetak", 2)
>>> print(ob)
<factory.Factory object at 0x0000013E1926D340>
>>> ob = ob.build_vehicle()
>>> print(ob)
<factory.Bike object at 0x0000013E192F2C70>
>>>
"""
