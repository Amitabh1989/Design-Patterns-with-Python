"""
COMMAND DESIGN PATTERN
=======================

Command deisgn pattern is another design pattern that deal withs 
implementations of tracing the changes, do and undo operations.

Here in the example below, we have combined this idea with COMPOSITE DESIGN PATTERN.

We have below classes:
1. Bank Account : Responsible for creating bank account for a Customer
2. Abstract class Command : This basically is meant to invoke functionality of the COMMAND
   design pattern.
   1. INVOKE : Execute what ever BankAccount operation is like DEPOSIT / WITHDRAW
   2. UNDO   : Undoe the last operation.
3. BankAccountCommand : This helps in creating Bank account for customers and associates
   command pattern functionality by inheriting the above abstract class.
4. CompositeBankAccountCommand : This class converts / implements composite pattern.
   Takes in list of accounts (BankAccountCommand) and applies functionality for group /
   single account
5. WithdrawTransferCommand: Takes in the CompositeBankAccountCommand as input with from and
   to account and the amount to transfer. Then executes the intended functionality.


Let's see the implementation as below.

"""

from abc import ABC
from enum import Enum
import unittest


class BankAccount:
    """
    Class for creating the bank account for any customer
    """

    OVERDRAFTLIMIT = -500

    def __init__(self, name, amount) -> None:
        """
        Init a bank account for cusotmer
        """
        self.name = name
        self.amount = amount

    def deposit(self, amount):
        """
        Given the amount, increment the amount for the Bank account holder

        Args:
            amount (int): Amount to deposite in the account

        Return:
            None
        """
        self.amount += amount

    def withdraw(self, amount):
        """
        Given the amount, decrement the amount for the Bank account holder

        Args:
            amount (int): Amount to withdraw from the account

        Return:
            bool: True if can withdraw else False
        """
        if self.amount - amount >= BankAccount.OVERDRAFTLIMIT:
            self.amount -= amount
            return True
        return False

    def __str__(self) -> str:
        """
        String representation of the object
        """
        return f'AC Name {self.name}, balance : {self.amount}'


class Command(ABC):
    """
    Abstract class Command : This basically is meant to invoke functionality of the COMMAND
    design pattern.
    1. INVOKE : Execute what ever BankAccount operation is like DEPOSIT / WITHDRAW
    2. UNDO   : Undoe the last operation.
    """

    def __init__(self) -> None:
        self.success = False

    def invoke(self):
        pass

    def undo(self):
        pass

class BankAccountCommand(Command):
    """
    BankAccountCommand : This helps in creating Bank account for customers
    and associates command pattern functionality by inheriting the above
    abstract class.
    """

    class Action(Enum):
        DEPOSIT = 0
        WITHDRAW = 1

    def __init__(self, account, action, amount) -> None:
        super().__init__()
        self.account = account
        self.action = action
        self.amount = amount

    def invoke(self):
        """
        Depending on the action to take, calls respective action for the
        account.
        """
        if self.action == self.Action.WITHDRAW:
            self.success = self.account.withdraw(self.amount)

        elif self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True

    def undo(self):
        """
        Does the polar opposite of the last action
        """
        if self.action == self.Action.WITHDRAW:
            self.account.deposit(self.amount)

        elif self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)


class CompositeBankAccountCommand(Command, list):
    """
    CompositeBankAccountCommand : This class converts / implements composite 
    pattern. Takes in list of accounts (BankAccountCommand) and applies
    functionality for group / single account
    """

    def __init__(self, items) -> None:
        super().__init__()
        for i in items:
            self.append(i)
    
    def invoke(self):
        print(f'Composite : {self}')
        for i in self:
            i.invoke()
            self.success = True
    
    def undo(self):
        if self.success:
            for i in reversed(self):
                i.undo()


class WithdrawTransferCommand(CompositeBankAccountCommand):
    """
    WithdrawTransferCommand: Takes in the CompositeBankAccountCommand as input
    with from and to account and the amount to transfer. Then executes the
    intended functionality.
    """

    def __init__(self, from_acc, to_acc, amount) -> None:
        super().__init__([
            BankAccountCommand(from_acc, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acc, BankAccountCommand.Action.DEPOSIT, amount),
        ])
    
    def invoke(self):
        self.success = all([i.invoke() for i in self])

# if __name__ == '__main__':
#     ba1 = BankAccount("Amitabh", 0)
#     ba2 = BankAccount("Shweta", 0)

#     print(f'BA1 : {ba1}\nBA2 : {ba2}')

#     bac1 = BankAccountCommand(ba1, BankAccountCommand.Action.DEPOSIT, 500)
#     bac2 = BankAccountCommand(ba2, BankAccountCommand.Action.DEPOSIT, 1000)

#     composite = CompositeBankAccountCommand([bac1, bac2])
#     composite.invoke()

#     print(f'BA1 : {ba1}\nBA2 : {ba2}')

#     transfer = WithdrawTransferCommand(ba1, ba2, 1000)
#     transfer.invoke()

#     print(f'BA1 : {ba1}\nBA2 : {ba2}')


class TestCommand(unittest.TestCase):
    def setUp(self) -> None:
        self.ba1 = BankAccount("Amitabh", 0)
        self.ba2 = BankAccount("Shweta", 0)
        print(f'INIT: BA1 : {self.ba1}\nINIT: BA2 : {self.ba2}')

    def tearDown(self) -> None:
        print(f'TD: BA1 : {self.ba1}\nTD: BA2 : {self.ba2}')
        print("Teardowm called")
    
    def test_BankAccountCommand(self):
        bac1 = BankAccountCommand(self.ba1, BankAccountCommand.Action.WITHDRAW, 500)
        bac2 = BankAccountCommand(self.ba2, BankAccountCommand.Action.DEPOSIT, 500)
        bac1.invoke()
        bac2.invoke()
        assert self.ba1.amount == -500
        assert self.ba2.amount == 500
    
    def test_CompositeBankAccountCommand(self):
        bac1 = BankAccountCommand(self.ba1, BankAccountCommand.Action.WITHDRAW, 500)
        bac2 = BankAccountCommand(self.ba2, BankAccountCommand.Action.DEPOSIT, 500)
        comp = CompositeBankAccountCommand([bac1, bac2])
        comp.invoke()
        print(f'FN: BA1 : {self.ba1}\nFN: BA2 : {self.ba2}')
        comp.undo()
        print(f'FN: BA1 : {self.ba1}\nFN: BA2 : {self.ba2}')
        assert self.ba1.amount == 0
        assert self.ba2.amount == 0

if __name__ == '__main__':
    unittest.main()