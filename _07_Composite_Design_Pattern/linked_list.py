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


import abc
from abc import ABC

# pylint: disable=too-few-public-methods
class Node(ABC):
    """
    An abstract class that is to be inherited, which
    in turn helps to create the Node
    """

    def __init__(self, val: int) -> None:
        """
        Init a node with the value passed

        Args:
            val (int): Value to assign to the node

        Return:
            None
        """
        self.value = val

    @abc.abstractmethod
    def __str__(self) -> str:
        """
        String representation of the Object

        Args:
            None

        Return:
            str: String representation of the Object
        """
        return  f'{self.value}'


# pylint: disable=too-few-public-methods
# pylint: disable=super-init-not-called
class LeafNode(Node):
    """
    Inherits the Node class. Accepts a value which the node will contain.
    We dont need to have an init method here as it would be initialized
    by the super class directly.
    """
    def __str__(self):
        """
        String representation of the Object

        Args:
            None

        Return:
            str: String representation of the Object
        """
        return f'{self.value}'


class CompositeNode(Node):
    """
    This class too, inherits the Node class and associates the child nodes
    to the node given. In a different implementation, I will show that we
    can inherit list as well and add Nodes to list and work with it.

    Here, inheriting Node class also makes sense as all the elements here
    need to have Node propertie, to qualify as Composite design pattern.
    """
    def __init__(self):
        """
        Init a node with the value passed

        Args:
            val (int): Value to assign to the node

        Return:
            None
        """
        self.child_node = []

    def add_node(self, node: Node) -> None:
        """
        Adds new node as child node of the Node that is created.

        Args:
            node (Node): Node to be added to child node list

        Returns:
            None
        """
        self.child_node.append(node)

    def remove_node(self, node) -> None:
        """
        Removes node from child node list

        Args:
            node (Node): Node to be removed
        
        Returns:
            None
        """
        self.child_node.remove(node)

    def __str__(self) -> str:
        """
        String representation of the Object

        Args:
            None
        
        Return:
            str: String representation of the Object
        """
        node = []
        for child in self.child_node:
            node.append(str(child))
        return ' --> '.join(node)


# pylint: disable=invalid-name
def main():
    """
    Main function shows 2 Composite Nodes being added here and how
    one composite node is a collection of 2 nodes.

    And then how one more composite node and be appended to another
    composite node too.
    """

    n1 = LeafNode(1)
    n2 = LeafNode(2)
    nl = CompositeNode()
    nl.add_node(n1)
    nl.add_node(n2)
    print(nl)

    n3 = LeafNode(3)
    n4 = LeafNode(4)
    nl2 = CompositeNode()
    nl2.add_node(n3)
    nl2.add_node(n4)
    print(nl2)

    nl.add_node(nl2)
    print(nl)


if __name__ == '__main__':
    main()


OUTPUT = r"""
>>> from linked_list import *
>>> main()
1 --> 2
3 --> 4
1 --> 2 --> 3 --> 4
>>> exit()
"""
