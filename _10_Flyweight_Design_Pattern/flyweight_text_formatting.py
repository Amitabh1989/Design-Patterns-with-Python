"""
Flyweight Pattern

The Flyweight pattern is a structural design pattern that focuses on
minimizing memory usage by sharing data between multiple objects. It is useful
when we need to create a large number of similar objects that consume a
significant amount of memory. By sharing common data instead of storing it in
each object, we can reduce memory consumption and improve performance.

This module provides an example implementation of the Flyweight pattern using
two classes: FormattedText and BetterFormattedText.

1. FormattedText:
    This class represents formatted text and provides methods for applying
    formatting to specific text ranges. It uses a list of boolean values to
    track the formatting status of each character in the text. The __str__
    method generates the final formatted text by iterating over the plain
    text and applying formatting based on the boolean values.

2. BetterFormattedText:
    This class extends the functionality of FormattedText by introducing a
    nested TextRange class. Each TextRange represents a specific range of text
    and its associated formatting options, such as capitalization, italics
    and bold. The format_text method allows adding new TextRanges to the
    formatted text.

Example Usage:
    # Create a FormattedText object
    text = FormattedText("Hello, World!")

    # Apply capitalization to a specific range
    text.capitalize(7, 12)

    # Print the formatted text
    print(text)  # Output: "Hello, WORLD!"

    # Create a BetterFormattedText object
    better_text = BetterFormattedText("Hello, World!")

    # Add a TextRange with capitalization to the formatted text
    range = better_text.format_text(7, 12)
    range.capitalize = True

    # Print the formatted text
    print(better_text)  # Output: "Hello, WORLD!"

Maintaining PEP 8:
    The code follows the PEP 8 style guidelines, including proper indentation,
    lowercase function and variable names, and the use of whitespace for
    readability.

"""

from dataclasses import dataclass, field


@dataclass
class FormattedText:
    """
    Class representing formatted text with the ability to apply formatting
    to specific text ranges.
    """

    plain_text: str
    formatted_text: list = field(init=False)

    def __post_init__(self) -> None:
        """
        Initialize the formatted text list with default formatting status
        for each character.
        """
        self.formatted_text = [False] * len(self.plain_text)

    def capitalize(self, start: int, end: int) -> None:
        """
        Apply capitalization formatting to the specified text range.

        Args:
            start (int): Start index of the text range.
            end (int): End index of the text range.
        """
        for index, _ in enumerate(self.formatted_text):
            if start <= index < end:
                self.formatted_text[index] = True

    # pylint: disable=unused-variable
    def __str__(self) -> str:
        """
        Generate the final formatted text by applying formatting to each
        character.

        Returns:
            str: The formatted text.
        """
        result = []
        # i here is use to demonstrate the usage of the Enumerate and ZIP
        # function together. Its not useful nonetheless.
        for i, (is_formatted, char) in enumerate(zip(self.formatted_text,
                                                    self.plain_text)):
            result.append(char.upper() if is_formatted else char)
        return "".join(result)


@dataclass
class BetterFormattedText:
    """
    Class representing better-formatted text with support for multiple text
    ranges and customizable formatting options.
    """

    plain_text: str
    formatted_text: list = field(init=False, default_factory=list)

    @dataclass
    class TextRange:
        """
        Class representing a specific range of text with associated formatting
        options.
        """

        start: int
        end: int
        capitalize: bool = False
        italic: bool = False
        bold: bool = False

        def covers(self, position: int) -> bool:
            """
            Check if the TextRange covers the specified position.

            Args:
                position (int): The position to check.

            Returns:
                bool: True if the TextRange covers the position, False
                otherwise.
            """
            return self.start <= position <= self.end

    def format_text(self, start: int, end: int) -> TextRange:
        """
        Create a new TextRange for the specified text range and add it to the
        formatted text.

        Args:
            start (int): Start index of the text range.
            end (int): End index of the text range.

        Returns:
            TextRange: The created TextRange object.
        """
        text_range = self.TextRange(start, end)
        self.formatted_text.append(text_range)
        return text_range

    def __str__(self) -> str:
        """
        Generate the final formatted text by applying formatting based on the
        defined text ranges.

        Returns:
            str: The formatted text.
        """
        result = []
        for i, char in enumerate(self.plain_text):
            for text_range in self.formatted_text:
                if text_range.covers(i):
                    result.append(char.upper())
                else:
                    result.append(char)
        return "".join(result)


def main():
    """
    The Main function.
    """
    # Example usage of FormattedText
    text = FormattedText("Hello, World!")
    text.capitalize(7, 12)
    print(text)  # Output: "Hello, WORLD!"

    # Example usage of BetterFormattedText
    better_text = BetterFormattedText("Hello, World!")
    range_ = better_text.format_text(7, 12)
    range_.capitalize = True
    print(better_text)  # Output: "Hello, WORLD!"


if __name__ == "__main__":
    main()
