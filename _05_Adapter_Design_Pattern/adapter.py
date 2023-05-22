"""
ADAPTER DESIGN PATTERN

The adapter pattern provides a uniform interface for the client to interact
with, abstracting away the differences between incompatible interfaces or
classes. It acts as a bridge between the client and the adaptee, (it not
actually a bridge pattern, though both of them aim to bridge the gap between
two interfaces!) allowing the client to use a consistent interface regardless
of the specific implementation details of the adaptee.

Internally, the adapter handles the necessary conversions or adaptations to
ensure that the output is consistent and compatible with the client's
expectations. This helps to decouple the client from the complexities
of dealing with different interfaces or classes, promoting code reusability
and maintainability.

Let's now see the implementation!

"""

import abc

class CSVFile:
    """
    Dummy class with no actual functionality that takes in a file. And
    implements a few functionalities.
    """

    def __init__(self, file: str) -> None:
        """
        Initialize a CSVFile object.

        Args:
            file (str): The name of the CSV file.

        Returns:
            None
        """
        self.filename = file

    def __str__(self) -> str:
        """
        Get a string representation of the CSVFile object.

        Returns:
            str: The string representation of the CSVFile object.
        """
        return f'{self.filename} received.'

    def read_csv(self):
        """
        Read CSV data.

        Returns:
            str: The message indicating that CSV data is being read.
        """
        return "Reading CSV data"

    def write_json(self):
        """
        Write CSV data to JSON file.

        Returns:
            str: The message indicating that CSV data is being written to a
            JSON file.
        """
        return "Writing CSV data to JSON file"


class JSONFile:
    """
    Dummy class with no actual functionality that takes in a file. And
    implements a few functionalities.
    """

    def __init__(self, file: str) -> None:
        """
        Initialize a JSONFile object.

        Args:
            file (str): The name of the JSON file.

        Returns:
            None
        """
        self.filename = file

    def __str__(self) -> str:
        """
        Get a string representation of the JSONFile object.

        Returns:
            str: The string representation of the JSONFile object.
        """
        return f'{self.filename} received.'

    def read_json(self):
        """
        Read JSON data.

        Returns:
            str: The message indicating that JSON data is being read.
        """
        return "Reading JSON data"

    def write_csv(self):
        """
        Write JSON data to CSV file.

        Returns:
            str: The message indicating that JSON data is being written to a
            CSV file.
        """
        return "Writing JSON data to CSV file"


# pylint: disable=too-few-public-methods
class FileAdapter(abc.ABC):
    """
    Base class that mandates the implementation of convert function by derived
    classes
    """

    def __init__(self, convertee) -> None:
        """
        Initialize a FileAdapter object.

        Args:
            convertee: The object to be adapted.

        Returns:
            None
        """
        self.convertee = convertee

    def convert(self):
        """
        Convert the data using the adapted object.

        Returns:
            str: The message indicating that conversion is complete.
        """
        return "Converted!"


# pylint: disable=too-few-public-methods
class JSONtoCSVConvertor(FileAdapter):
    """
    Derived class that implements the convert function of FileAdapter class
    """
    def convert(self):
        """
        Convert JSON data to CSV format.

        Returns:
            None
        """
        self.convertee.read_json()
        self.convertee.write_csv()
        print("Conversion complete!")


# pylint: disable=too-few-public-methods
class CSVtoJSONConvertor(FileAdapter):
    """
    Derived class that implements the convert function of FileAdapter class
    """

    def convert(self):
        """
        Convert CSV data to JSON format.

        Returns:
            None
        """
        self.convertee.read_csv()
        self.convertee.write_json()
        print("Conversion complete!")

def main():
    """
    Main function
    """
    csv_file = CSVFile("data.csv")
    json_file = JSONFile("data.json")

    csv_to_json_converter = CSVtoJSONConvertor(csv_file)
    csv_to_json_converter.convert()

    json_to_csv_converter = JSONtoCSVConvertor(json_file)
    json_to_csv_converter.convert()


OUTPUT = r"""
>>> import adapter
>>> from adapter import *
>>>
>>>
>>> csv_file = CSVFile("data.csv")
>>> json_file = JSONFile("data.json")
>>> csv_to_json_converter = CSVtoJSONConvertor(csv_file)
>>> csv_to_json_converter.convert()
Conversion complete!
>>> json_to_csv_converter = JSONtoCSVConvertor(json_file)
>>> json_to_csv_converter.convert()
Conversion complete!
"""