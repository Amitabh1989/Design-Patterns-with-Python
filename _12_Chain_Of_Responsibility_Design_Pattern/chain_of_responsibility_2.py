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
from typing import Optional
import abc

@dataclass
class Request:
    """
    Represents a request for approval.

    Args:
        amount (int): The amount of the request.
        approved (bool, optional): Flag indicating if the request is approved. Defaults to False.
    """

    amount: int
    approved: bool = False

    def __str__(self) -> str:
        return f'Request approval for amount {self.amount} is {self.approved}'

@dataclass
class Approver(abc.ABC):
    """
    Abstract base class for the approvers in the request approval chain.

    Args:
        successor (Approver, optional): The next approver in the chain. Defaults to None.
    """

    successor: Optional["Approver"] = None

    def set_successor(self, successor):
        """
        Sets the next approver in the chain.

        Args:
            successor (Approver): The next approver in the chain.
        """
        if self.successor:
            self.set_successor(successor)
        else:
            self.successor = successor

    # pylint: disable=unnecessary-pass
    @abc.abstractmethod
    def process_request(self, request):
        """
        Process the request and decide whether to approve or pass it to the next approver.

        Args:
            request (Request): The request to be processed.
        """
        pass

@dataclass
class Manager(Approver):
    """
    Concrete implementation of an approver representing a Manager.

    Args:
        limit (int, optional): The approval limit for the Manager. Defaults to 5000.
    """

    limit: int = 5000

    def process_request(self, request):
        """
        Process the request and decide whether to approve or pass it to the next approver.

        Args:
            request (Request): The request to be processed.
        """
        if request.amount <= self.limit:
            print(f'Request for amount {request.amount} approved by {type(self).__name__}')
            request.approved = True
        else:
            self.successor.process_request(request)


@dataclass
class Director(Approver):
    """
    Concrete implementation of an approver representing a Director.

    Args:
        limit (int, optional): The approval limit for the Director. Defaults to 10000.
    """

    limit: int = 10000

    def process_request(self, request):
        """
        Process the request and decide whether to approve or pass it to the next approver.

        Args:
            request (Request): The request to be processed.
        """
        if request.amount <= self.limit:
            print(f'Request for amount {request.amount} approved by {type(self).__name__}')
            request.approved = True
        else:
            self.successor.process_request(request)

@dataclass
class CEO(Approver):
    """
    Concrete implementation of an approver representing a CEO.

    Args:
        limit (int, optional): The approval limit for the CEO. Defaults to 15000.
    """

    limit: int = 15000

    def process_request(self, request):
        """
        Process the request and decide whether to approve or reject it.

        Args:
            request (Request): The request to be processed.
        """
        if request.amount <= self.limit:
            print(f'Request for amount {request.amount} approved by {type(self).__name__}')
            request.approved = True
        else:
            request.approved = False
            print(f"Request for {request.amount} is rejected by {type(self).__name__}")


if __name__ == '__main__':
    # Instantiate the approvers
    m = Manager()
    d = Director()
    c = CEO()

    # Build the chain of approvers
    m.set_successor(d)
    d.set_successor(c)

    # Print the hierarchy
    print(f'Manager  : {m}')
    print(f'Director : {d}')
    print(f'CEO      : {c}')

    # Create requests
    r1 = Request(4000)
    r2 = Request(8000)
    r3 = Request(14000)
    r4 = Request(20000)

    # Print the requests
    print(r1)
    print(r2)
    print(r3)
    print(r4)

    # Process the requests
    m.process_request(r1)
    m.process_request(r2)
    m.process_request(r3)
    m.process_request(r4)


OUTPUT = r"""
Manager  : Manager(successor=Director(successor=CEO(successor=None, limit=15000), limit=10000), limit=5000)
Director : Director(successor=CEO(successor=None, limit=15000), limit=10000)
CEO      : CEO(successor=None, limit=15000)
Request approval for amount 4000 is False
Request approval for amount 8000 is False
Request approval for amount 14000 is False
Request approval for amount 20000 is False
Request for amount 4000 approved by Manager
Request for amount 8000 approved by Director
Request for amount 14000 approved by CEO
Request for 20000 is rejected by CEO
"""