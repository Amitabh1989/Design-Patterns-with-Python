"""
BUILDER DESIGN PATTERN
======================
- Amitabh Suman, Ai-Nebula

NOTE : We could have used Abstract design pattern as well but this is a
demonstration of "Builder Design Pattern"

Approach here is pretty simplpe and yet magnificent.
Think manually, about all steps involved in a Pizza order till deliver.
1. Someone presents menu for Pizza orders available.
2. User selects the Pizza and order preperation process kicks in.
3. The Pizza base is selected
4. Based on type of Pizza, sauce, toppings and baking is done.
5. While #4 is in progress, the progress updated in shown in the ticker.
6. Once Pizza is ready, its served!

And in below implenmentation, you will see that exact same process has been
followed. Each process is a class (well, almost)

A step-by-step approach to build the final product !

"""
from enum import Enum
import time

PizzaProgress = Enum('PizzaProgress', 'queued preperation baking ready')
PizzaDough = Enum('PizzaDough', 'thin thick')
PizzaSauce = Enum('PizzaSauce', 'tomato creme')
PizzaTopping = Enum('PizzaTopping',
                    'mozzarella double_mozzarella bacon '
                    'ham mushrooms red_onion oregano')

STEP_DELAY = 3  # assumed for this example

class Pizza:
    """
    Class representing a pizza.

    Args:
        name (Enum): The name of the pizza.

    Attributes:
        name (Enum): The name of the pizza.
        dough (PizzaDough): The type of dough used in the pizza.
        sauce (PizzaSauce): The type of sauce used in the pizza.
        topping (list): List of toppings used in the pizza.

    Methods:
        __str__: Returns a string representation of the pizza.
        prepare_dough: Prepares the dough for the pizza.

    """

    def __init__(self, name: Enum) -> None:
        self.name = name
        self.dough = None
        self.sauce = None
        self.topping = []

    def __str__(self) -> str:
        """
        Returns a string representation of the pizza.

        Returns:
            str: The string representation of the pizza.
        """
        return f'{self.name}'

    def prepare_dough(self, dough: str) -> None:
        """
        Prepares the dough for the pizza.

        Args:
            dough (str): The type of dough for the pizza.

        Returns:
            None
        """
        self.dough = dough
        print(f'Preparing the {self.dough} of your {self}...')
        time.sleep(STEP_DELAY)
        print(f'Done with the {self.dough} dough')


class MargaritaBuilder:
    """
    Class representing a builder for Margarita pizza.

    Attributes:
        pizza (Pizza): The Margarita pizza being built.
        progress (PizzaProgress): The progress of the pizza preparation.
        baking_time (int): The baking time for the pizza.

    Methods:
        __init__: Initializes the MargaritaBuilder object.
        prepare_dough: Prepares the dough for the Margarita pizza.
        add_sauce: Adds sauce to the Margarita pizza.
        add_topping: Adds toppings to the Margarita pizza.
        bake: Bakes the Margarita pizza.

    """

    def __init__(self) -> None:
        self.pizza = Pizza('margarita')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self) -> None:
        """
        Prepares the dough for the Margarita pizza.

        Returns:
            None
        """
        self.progress = PizzaProgress.preperation
        self.pizza.prepare_dough(PizzaDough.thin)

    def add_sauce(self) -> None:
        """
        Adds sauce to the Margarita pizza.

        Returns:
            None
        """
        print("Adding tomato sauce to your pizza")
        self.pizza.sauce = PizzaSauce.tomato
        time.sleep(STEP_DELAY)
        print("Done with sauce addition")

    def add_topping(self) -> None:
        """
        Adds toppings to the Margarita pizza.

        Returns:
            None
        """
        toppings = 'double mozzarella, oregano'
        topping_items = (PizzaTopping.double_mozzarella, PizzaTopping.oregano)
        print(f"Adding toppings {toppings} to your pizza")
        self.pizza.topping.append(list(topping_items))
        print("Toppings added")

    def bake(self) -> None:
        """
        Bakes the Margarita pizza.

        Returns:
            None
        """
        self.progress = PizzaProgress.baking
        print("Baking your pizza")
        time.sleep(STEP_DELAY)
        self.progress = PizzaProgress.ready
        print("Pizza is ready!")


class CreamyBaconBuilder:
    """
    Class representing a builder for Creamy Bacon pizza.

    Attributes:
        pizza (Pizza): The Creamy Bacon pizza being built.
        progress (PizzaProgress): The progress of the pizza preparation.
        baking_time (int): The baking time for the pizza.

    Methods:
        __init__: Initializes the CreamyBaconBuilder object.
        prepare_dough: Prepares the dough for the Creamy Bacon pizza.
        add_sauce: Adds sauce to the Creamy Bacon pizza.
        add_topping: Adds toppings to the Creamy Bacon pizza.
        bake: Bakes the Creamy Bacon pizza.

    """

    def __init__(self) -> None:
        self.pizza = Pizza('creamy bacon')
        self.progress = PizzaProgress.queued
        self.baking_time = 5

    def prepare_dough(self) -> None:
        """
        Prepares the dough for the Creamy Bacon pizza.

        Returns:
            None
        """
        self.progress = PizzaProgress.preperation
        self.pizza.prepare_dough(PizzaDough.thick)

    def add_sauce(self) -> None:
        """
        Adds sauce to the Creamy Bacon pizza.

        Returns:
            None
        """
        print("Adding tomato sauce to your pizza")
        self.pizza.sauce = PizzaSauce.creme
        time.sleep(STEP_DELAY)
        print("Done with sauce addition")

    def add_topping(self) -> None:
        """
        Adds toppings to the Creamy Bacon pizza.

        Returns:
            None
        """
        toppings = 'mozzarella, oregano, bacon, ham, mushroom, red onion'
        topping_items = (
            PizzaTopping.mozzarella,
            PizzaTopping.oregano,
            PizzaTopping.bacon,
            PizzaTopping.mushrooms,
            PizzaTopping.red_onion,
            PizzaTopping.ham
        )
        print(f"Adding toppings {toppings} to your pizza")
        self.pizza.topping.append(list(topping_items))
        print("Toppings added")

    def bake(self) -> None:
        """
        Bakes the Creamy Bacon pizza.

        Returns:
            None
        """
        self.progress = PizzaProgress.baking
        print("Baking your pizza")
        time.sleep(STEP_DELAY)
        self.progress = PizzaProgress.ready
        print("Pizza is ready!")


class Waiter:
    """
    Class representing a waiter who constructs pizzas.

    Attributes:
        builder: The builder object used for constructing the pizza.

    Methods:
        __init__: Initializes the Waiter object.
        construct_pizza: Constructs a pizza using the provided builder.
        pizza: Returns the constructed pizza.

    """

    def __init__(self) -> None:
        self.builder = None

    # pylint: disable=expression-not-assigned
    def construct_pizza(self, builder) -> None:
        """
        Constructs a pizza using the provided builder.

        Args:
            builder: The builder object used for constructing the pizza.

        Returns:
            None
        """
        self.builder = builder
        steps = (
            builder.prepare_dough,
            builder.add_sauce,
            builder.add_topping,
            builder.bake
        )
        [step() for step in steps]

    @property
    def pizza(self):
        """
        Returns the constructed pizza.

        Returns:
            Pizza: The constructed pizza.
        """
        return self.builder.pizza


def validate_type(builders: dict) -> tuple:
    """
    Validates the user input for pizza type and returns the corresponding
    builder.

    Args:
        builders (dict): Dictionary mapping pizza type input to builder
        classes.

    Returns:
        tuple: A tuple containing a boolean indicating the validity of the
        input and the corresponding builder object.
    """
    try:
        input_msg = "What pizza would you like: \
            [m]argarita / [c]reamy bacon? "
        pizza_type = input(input_msg)
        builder = builders[pizza_type]()
        valid_input = True
    except KeyError:
        error_msg = "Sorry, not a valid input"
        valid_input = False
        print(error_msg)
        return (valid_input, None)
    return (valid_input, builder)


def main():
    """
    Main function for pizza ordering.

    Returns:
        None
    """
    builders = {
        "m": MargaritaBuilder,
        "c": CreamyBaconBuilder
    }
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_type(builders)
    print()
    waiter = Waiter()
    waiter.construct_pizza(builder)
    pizza = waiter.pizza
    print()
    print(f'Enjoy your {pizza} pizza!!')

OUTPUT = r"""
Preparing the PizzaDough.thin of your margarita...
Done with the thin dough
Adding tomato sauce to your pizza
Done with sauce addition
Adding toppings double mozzarela, oregano to your pizza
Topping added
Baking your pizza
Pizza is ready!

Enjoy your pizza !!
>>>  
"""
