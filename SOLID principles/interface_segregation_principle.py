"""
The interface segregation principle states that an interface should be as 
small a possible in terms of cohesion. In other words, it should do ONE
thing. It doesn't mean that the interface should have one method.
An interface can have multiple cohesive methods.

In short: A class should not be forced to use interfaces that it does not use.
"""

import abc

# ==============================================
# BREACH OF PRINCIPLE
# ==============================================
# Here, you will see that the PrinterModelA class does not perform few
# functions and hence, it raises NotImplementedError. And it is direct 
# violation of the ISP. The class PrinterModelA is forced to use features
# that are not inherently its own. Let's explore this.


class Features(abc.ABC):
    """
    Abstract base class representing features of a device.

    Args:
        name (str): The name of the feature.

    Attributes:
        name (str): The name of the feature.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a Features object.

        Args:
            name (str): The name of the feature.
        """
        self.name = name

    def __str__(self) -> str:
        """
        Return a string representation of the Features object.

        Returns:
            str: A string representation of the Features object.
        """
        return f'{self.name} class object'

    @abc.abstractmethod
    def print(self):
        """
        Abstract method to perform printing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def scan(self):
        """
        Abstract method to perform scanning.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def fax(self):
        """
        Abstract method to perform faxing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def email(self):
        """
        Abstract method to perform emailing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError


class PrinterModelA(Features):
    """
    Class representing a printer model A.

    Args:
        name (str): The name of the printer model A.
    """

    def __init__(self, name: str) -> None:
        """
        Initialize a PrinterModelA object.

        Args:
            name (str): The name of the printer model A.
        """
        super().__init__(type(self).__name__)

    def print(self):
        """
        Print a message indicating successful printing.
        """
        print("Printed Successfully !!")

    def scan(self):
        """
        Perform scanning.

        Prints a message indicating that scanning is not supported.
        """
        print("I am so sed...I can't scan :'( ")
        return super().scan()

    def fax(self):
        """
        Perform faxing.

        Prints a message indicating that faxing is not supported.
        """
        print("I am so sed...I can't fax :'( ")
        return super().fax()

    def email(self):
        """
        Perform emailing.

        Prints a message indicating that emailing is not supported.
        """
        print("I am so sed...I can't mail :'( ")
        return super().email()


OUTPUT_1 = r"""
>>> import interface_segregation_principle   
>>> from interface_segregation_principle import *   
>>>
>>> ob = PrinterModelA("Ragnar") 
>>> str(ob)    
'PrinterModelA class object'
>>> ob.print()
Printed Successfully !!
>>>
>>>
>>> ob.fax()
I am so sed...I can't fax :'(
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\GitHub\Design-Patterns-with-Python\SOLID principles\
    interface_segregation_principle.py", line 119, in fax
    return super().fax()
  File "C:\GitHub\Design-Patterns-with-Python\SOLID principles\
    interface_segregation_principle.py", line 68, in fax
    raise NotImplementedError
NotImplementedError
>>>
>>>
>>> ob.email()
I am so sed...I can't mail :'(
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\GitHub\Design-Patterns-with-Python\SOLID principles\
    interface_segregation_principle.py", line 128, in email
    return super().email()
  File "C:\GitHub\Design-Patterns-with-Python\SOLID principles\
    interface_segregation_principle.py", line 77, in email
    raise NotImplementedError
NotImplementedError
>>>
"""


# ==============================================
# ADHERE TO THE PRINCIPLE
# ==============================================
# We saw how the class PrinterModelA was forced to use interfaces it does
# not have. So let's fix this instead.

class Print(abc.ABC):
    """
    Abstract base class for printing functionality.

    This class defines an abstract method 'print' that must be implemented by derived classes
    to perform the actual printing.
    """

    @abc.abstractmethod
    def print(self):
        """
        Abstract method to perform printing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError


class Scan(abc.ABC):
    """
    Abstract base class for scanning functionality.

    This class defines an abstract method 'scan' that must be implemented by derived classes
    to perform the actual scanning.
    """

    @abc.abstractmethod
    def scan(self):
        """
        Abstract method to perform scanning.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError


class Fax(abc.ABC):
    """
    Abstract base class for faxing functionality.

    This class defines an abstract method 'fax' that must be implemented by derived classes
    to perform the actual faxing.
    """

    @abc.abstractmethod
    def fax(self):
        """
        Abstract method to perform faxing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError


class Email(abc.ABC):
    """
    Abstract base class for emailing functionality.

    This class defines an abstract method 'email' that must be implemented by derived classes
    to perform the actual emailing.
    """

    @abc.abstractmethod
    def email(self):
        """
        Abstract method to perform emailing.

        This method must be implemented by the derived classes.
        """
        raise NotImplementedError



class PrinterModelANew(Print):
    """
    Class representing Printer Model A.

    Inherits from the Print class.

    Overrides the print() method.
    """

    def print(self) -> None:
        """
        Print a message indicating that this printer can print.
        """
        print("I can Print!")


class PrinterModelBNew(Print, Scan):
    """
    Class representing Printer Model B.

    Inherits from the Print and Scan classes.

    Overrides the print() and scan() methods.
    """

    def print(self) -> None:
        """
        Print a message indicating that this printer can print.
        """
        print("I can Print!")

    def scan(self) -> None:
        """
        Perform scanning.

        Prints a message indicating that this printer can scan.
        """
        print("I can Scan")


class PrinterModelCNew(Print, Scan, Fax):
    """
    Class representing Printer Model C.

    Inherits from the Print, Scan, and Fax classes.

    Overrides the print(), scan(), and fax() methods.
    """

    def print(self) -> None:
        """
        Print a message indicating that this printer can print.
        """
        print("I can Print!")

    def scan(self) -> None:
        """
        Perform scanning.

        Prints a message indicating that this printer can scan.
        """
        print("I can Scan")

    def fax(self) -> None:
        """
        Perform faxing.

        Prints a message indicating that this printer can fax.
        """
        print("I can Fax")


class PrinterModelDNew(Print, Scan, Fax, Email):
    """
    Class representing Printer Model D.

    Inherits from the Print, Scan, Fax, and Email classes.

    Overrides the print(), scan(), fax(), and email() methods.
    """

    def print(self) -> None:
        """
        Print a message indicating that this printer can print.
        """
        print("I can Print!")

    def scan(self) -> None:
        """
        Perform scanning.

        Prints a message indicating that this printer can scan.
        """
        print("I can Scan")

    def fax(self) -> None:
        """
        Perform faxing.

        Prints a message indicating that this printer can fax.
        """
        print("I can Fax")

    def email(self) -> None:
        """
        Perform emailing.

        Prints a message indicating that this printer can email.
        """
        print("I can Email")

OUTPUT_2 = r"""
>>> import interface_segregation_principle        
>>> from interface_segregation_principle import *
>>> ob = PrinterModelANew()
>>> ob.print()
I can Print!
>>>
>>>
>>> ob1 = PrinterModelBNew() 
>>> ob1.print()
I can Print!
>>> ob1.scan()
I can Scan
>>>
>>>
>>> ob2 = PrinterModelCNew() 
>>> ob2.print() 
I can Print!
>>> ob2.scan()  
I can Scan
>>> ob2.fax()  
I can Fax
>>>
>>>
>>> ob3 = PrinterModelDNew() 
>>> ob3.print()
I can Print!
>>> ob3.scan()  
I can Scan
>>> ob3.fax()  
I can Fax
>>> ob3.email() 
I can Email
>>>
"""
