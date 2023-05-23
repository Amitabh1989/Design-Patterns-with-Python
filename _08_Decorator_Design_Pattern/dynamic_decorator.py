from dataclasses import dataclass, field
from typing import Any, Iterator

@dataclass
class FileWithLogging:
    """
    FileWithLogging is a decorator class that adds logging functionality to a file object.
    It wraps a file object and delegates most operations to the underlying file.

    Args:
        file: The file object to wrap.

    Attributes:
        file: The underlying file object.

    Methods:
        writelines: Writes multiple strings to the file.
    """

    file: Any

    def writelines(self, strings):
        """
        Writes multiple strings to the file and logs the number of lines written.

        Args:
            strings: A sequence of strings to write to the file.
        """
        self.file.writelines(strings)
        print(f'Wrote {len(strings)} lines')
    
    def __iter__(self) -> Iterator[str]:
        """
        Returns an iterator over the lines of the file.

        Returns:
            An iterator that yields each line of the file as a string.
        """
        return iter(self.file)
    
    def __next__(self):
        """
        Returns the next line from the file.

        Returns:
            The next line from the file as a string.

        Raises:
            StopIteration: If there are no more lines to read.
        """
        return self.file.__next__()

    def __getattr__(self, item: str) -> Any:
        """
        Retrieves the attribute of the underlying file object.

        Args:
            item: The name of the attribute to retrieve.

        Returns:
            The value of the requested attribute.

        Raises:
            AttributeError: If the attribute is not found in the underlying file object.
        """
        return getattr(self.file, item)

    def __setattr__(self, __name: str, __value: Any) -> None:
        """
        Sets the value of the specified attribute.

        Args:
            __name: The name of the attribute to set.
            __value: The value to assign to the attribute.

        Raises:
            AttributeError: If the attribute is not found in the underlying file object.
        """
        if __name == "file":
            self.__dict__[__name] = __value
        else:
            setattr(self.file, __name, __value)
    
    def __delattr__(self, __name: str) -> None:
        """
        Deletes the specified attribute.

        Args:
            __name: The name of the attribute to delete.

        Raises:
            AttributeError: If the attribute is not found in the underlying file object.
        """
        delattr(self.file, __name)


if __name__ == '__main__':
    # Usage example
    file = FileWithLogging(open("hello_world.txt", 'w'))
    print(file)
    file.writelines(["Hey", "Amitabh"])
    file.close()
    file = FileWithLogging(open("hello_world.txt", 'r'))
    for line in file:
        print(line.strip() + '\n')
    file.close()
    