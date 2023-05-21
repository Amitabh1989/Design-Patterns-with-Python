"""
The open-closed principle states that a class, method, and function should be
open for extension but closed for modification.

The open-closed principle sounds contradictory.

The purpose of the open-closed principle is to make it easy to add new features
(or use cases) to the system without directly modifying the existing code.
"""

import os
import abc

# ==============================================
# BREACH OF PRINCIPLE
# ==============================================
# Say we want to save file as JSON as well. We will end up adding a new function
# in the class SaveList

# pylint: disable=too-few-public-methods
class SaveList():
    """
    A class for handling file operations related to task lists.

    Args:
        task_list (list): List of tasks to be saved.

    Attributes:
        None

    Methods:
        save_to_file(task_list): Saves the task list to a file.

    """

    @staticmethod
    def save_to_file(task_list):
        """
        Saves the task list to a file in CWD with name todo_list.txt.

        Args:
            task_list (str): List of task to save.

        Returns:
            None.
        """
        with open(os.path.join(os.getcwd(), 'todo_list.txt'), 'a+',
                   encoding='utf-8') as file_handle:
            file_handle.write(str(task_list))

    # pylint: disable=unused-argument
    @staticmethod
    def save_to_json(task_list):
        """
        Saves the task list to a JSON file. Implementation withdrawn

        Args:
            task_list (str): List of task to save.

        Returns:
            bool: True if saved, False is failed
        """
        # add implementation code here.
        return True


# ==============================================
# ADHERE TO THE PRINCIPLE
# ==============================================
# We define a class SaveList as abstract class and inherit it to a new
# class for saving the task list as a new format whenever the requirement
# comes


class SaveListMeta(metaclass=abc.ABCMeta):
    """
    A class for handling file operations related to task lists.

    Args:
        task_list (list): List of tasks to be saved.

    Attributes:
        None

    Methods:
        save_to_file(task_list): Saves the task list to a file.

    """

    # pylint: disable=unused-argument
    @abc.abstractmethod
    @staticmethod
    def save_task(task_list):
        """
        Saves the task list to a file in CWD with name todo_list.txt.

        Args:
            task_list (str): List of task to save.

        Returns:
            None.
        """
        raise NotImplementedError


class SaveAsTextFile(SaveList):
    """
    A class for handling file operations as Text File.

    Args:
        task_list (list): List of tasks to be saved.

    Attributes:
        None

    Methods:
        save_to_file(task_list): Saves the task list to a file.

    """

    # pylint: disable=unused-argument
    @staticmethod
    def save_task(task_list):
        """
        Saves the task list to a JSON file. Implementation withdrawn

        Args:
            task_list (str): List of task to save.

        Returns:
            bool: True if saved, False is failed
        """
        # add implementation code here.
        return True


class SaveAsJSONFile(SaveList):
    """
    A class for handling file operations as JSON File.

    Args:
        task_list (list): List of tasks to be saved.

    Attributes:
        None

    Methods:
        save_to_file(task_list): Saves the task list to a file.

    """

    # pylint: disable=unused-argument
    @staticmethod
    def save_task(task_list):
        """
        Saves the task list to a JSON file. Implementation withdrawn

        Args:
            task_list (str): List of task to save.

        Returns:
            bool: True if saved, False is failed
        """
        # add implementation code here.
        return True

# Same execution flow as from single_responsibility_principle file
# todo_obj = ToDoList()
