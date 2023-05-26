"""
CHAIN OF RESPONSIBILITY DESIGN PATTERN
======================================

Chain of responsibility pattern is used to achieve loose coupling in software
design where a request from the client is passed to a chain of objects to
process them. Later, the object in the chain will decide themselves who will
be processing the request and whether the request is required to be sent to
the next object in the chain or not.

Where and When Chain of Responsibility pattern is applicable : 

1. When you want to decouple a request’s sender and receiver
2. Multiple objects, determined at runtime, are candidates to handle a request
3. When you don’t want to specify handlers explicitly in your code
4. When you want to issue a request to one of several objects without
   specifying the receiver explicitly.

This pattern is recommended when multiple objects can handle a request and the
handler doesn’t have to be a specific object. Also, the handler is determined
at runtime. Please note that a request not handled at all by any handler is a
valid use case.

DOC SOURCE : Geeks for Geeks

Let's see the implementation!

"""

from dataclasses import dataclass

@dataclass
class Character:
    """
    Represents a character with attack and defense attributes.

    Args:
        name (str): The name of the character.
        attack (int): The attack power of the character.
        defence (int): The defense power of the character.
    """

    name: str
    attack: int
    defence: int

    def __str__(self) -> str:
        """
        Returns a string representation of the character.

        Returns:
            str: The string representation of the character.
        """
        return f'{self.name} power ({self.attack}/{self.defence})'

@dataclass
class Modifier:
    """
    Base class for character modifiers.

    Args:
        character (Character): The character to be modified.
        next_power (Modifier, optional): The next modifier in the chain. Defaults to None.
    """

    character: Character
    next_power: "Modifier" = None

    def add_modifier(self, attribute):
        """
        Adds a new modifier to the chain.

        Args:
            attribute (Modifier): The modifier to be added.
        """
        if self.next_power:
            self.next_power.add_modifier(attribute)
        else:
            self.next_power = attribute

    def handle(self):
        """
        Handles the modification process.
        """
        if self.next_power:
            self.next_power.handle()

@dataclass
class DoubleAttackModifier(Modifier):
    """
    Modifier class to double the attack power of a character.

    Args:
        character (Character): The character to be modified.
    """

    character: Character

    def handle(self):
        """
        Handles the doubling of attack power for the character.
        """
        print(f"Doubling attack for {self.character.name}")
        self.character.attack *= 2
        print(f"Successfully doubled attack for {self.character.name}")
        super().handle()

@dataclass
class IncreaseDefenceModifier(Modifier):
    """
    Modifier class to double the defense power of a character.

    Args:
        character (Character): The character to be modified.
    """

    character: Character

    def handle(self):
        """
        Handles the doubling of defense power for the character.
        """
        print(f"Doubling defense for {self.character.name}")
        self.character.defence *= 2
        print(f"Successfully doubled defense for {self.character.name}")
        super().handle()

@dataclass
class NoBonusModifier(Modifier):
    """
    Modifier class representing no bonus for a character.

    Args:
        character (Character): The character to be modified.
    """

    character: Character

    def handle(self):
        """
        Handles the case where there is no bonus for the character.
        """
        print("No bonus for you!")

if __name__ == '__main__':
    # Create a character
    character = Character("Thor", 1, 1)

    # Create the root modifier
    root = Modifier(character)

    # Add modifiers to the chain
    root.add_modifier(DoubleAttackModifier(character=character))
    print(root)
    root.add_modifier(DoubleAttackModifier(character=character))
    print(root)
    root.add_modifier(IncreaseDefenceModifier(character=character))
    print(root)

    # Handle the modification process
    root.handle()

    # Print the final state of the character
    print(character)


OUTPUT = r"""
Modifier(character=Character(name='Thor', attack=1, defence=1),
 next_power=DoubleAttackModifier(character=Character(name='Thor', attack=1, defence=1),
   next_power=None))
Modifier(character=Character(name='Thor', attack=1, defence=1),
 next_power=DoubleAttackModifier(character=Character(name='Thor', attack=1, defence=1),
   next_power=DoubleAttackModifier(character=Character(name='Thor', attack=1, defence=1),
     next_power=None)))
Modifier(character=Character(name='Thor', attack=1, defence=1),
 next_power=DoubleAttackModifier(character=Character(name='Thor', attack=1, defence=1),
   next_power=DoubleAttackModifier(character=Character(name='Thor', attack=1, defence=1),
     next_power=IncreaseDefenceModifier(character=Character(name='Thor', attack=1, defence=1),
       next_power=None))))
Doubling attack for Thor
Successfully doubled attack for Thor
Doubling attack for Thor
Successfully doubled attack for Thor
Doubling defense for Thor
Successfully doubled defense for Thor
Thor power (4/2)
"""
