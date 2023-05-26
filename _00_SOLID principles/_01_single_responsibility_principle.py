"""
The single responsibility principle (SRP) states that every class, method,
and function should have only one job or one reason to change.

The purposes of the single responsibility principle are to:

1. Create high cohesive and robust classes, methods, and functions.
2. Promote class composition
3. Avoid code duplication

"""

# ==============================================
# BREACH OF PRINCIPLE
# ==============================================
# Explanation
# TODOLIST class takes on extra responsibility to handle saving list to text
# file. What if we need to use JSON instead of the TEXT file. We will end up
# changing the whole function.

import os


# pylint: disable=useless-object-inheritance
class ToDoList(object):
    """
    Class adheres to the SRP Principle

    Attributes:
        task_list (list): Maintains list of all the tasks added.

    Methods:
        add_task(): Appends task to the task_list.
        save_to_file(): Saves tasks to file.
    """

    def __init__(self):
        self.task_list = []

    def add_task(self, task: str) -> None:
        """
        Takes the task as string and appends to the list.

        Args:
            task (str): Task to perform.
        
        Returns:
            None .
        """
        print(f"Adding : {task}")
        self.task_list.append(task)

    def __str__(self):
        task_str = '\n'.join([f'{index} : {task}' for index,
                               task in enumerate(self.task_list)])
        print(f"Task list:\n{task_str}")
        return f"Task list:\n{task_str}"

    def save_to_file(self):
        """
        Saves the task list to a file in CWD with name todo_list.txt.

        Args:
            None.
        
        Returns:
            None.
        """
        with open(os.path.join(os.getcwd(), 'todo_list.txt'), 'a+',
                   encoding='utf-8') as file_handle:
            file_handle.write(str(self.task_list))

# Output here
COMMENT_1 = r"""
PS C:\GitHub\Design-Patterns-with-Python\SOLID principles> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42)
 [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import single_responsibility_principle as srp
>>> task_obj = srp.ToDoList()
>>> task_obj.add_task("Get the Whey")
Adding : Get the Whey
>>> task_obj.add_task("Get an hair cut for God's sake !")
Adding : Get an hair cut for God's sake !
>>> str(task_obj)
Task list:
0 : Get the Whey
1 : Get an hair cut for God's sake !
"Task list:\n0 : Get the Whey\n1 : Get an hair cut for God's sake !"
>>> task_obj.save_to_file()
"""


# ==============================================
# ADHERE TO THE PRINCIPLE
# ==============================================

# Changed the name else it will lead to MRO (method resolution issue)
# pylint: disable=useless-object-inheritance
class ToDoListNew(object):
    """
    Class adheres to the SRP Principle
    
    Attributes:
        task_list (list): Maintains list of all the tasks added.
    
    Methods:
        add_task(): Appends task to the task_list.
    """

    def __init__(self):
        self.task_list = []

    def add_task(self, task: str) -> None:
        """
        Takes the task as string and appends to the list.

        Args:
            task (str): Task to perform.

        Returns:
            None .
        """
        print(f"Adding : {task}")
        self.task_list.append(task)

    def __str__(self):
        task_str = '\n'.join([f'{index} : {task}' for index,
                               task in enumerate(self.task_list)])
        print(f"Task list:\n{task_str}")
        return f"Task list:\n{task_str}"

# pylint: disable=too-few-public-methods
class SaveList(object):
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
            None.

        Returns:
            None.
        """
        with open(os.path.join(os.getcwd(), 'todo_list.txt'), 'a+',
                   encoding='utf-8') as file_handle:
            file_handle.write(str(task_list))

# OUTPUT
COMMENT_2 = r"""
PS C:\GitHub\Design-Patterns-with-Python\SOLID principles> python
Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) 
[MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> import single_responsibility_principle as srp
>>> task_obj = srp.ToDoListNew() 
>>> task_obj.add_task("Get the Whey")
Adding : Get the Whey
>>> task_obj.add_task("Get an hair cut for God's sake !")
Adding : Get an hair cut for God's sake !
>>> str(task_obj)
Task list:
0 : Get the Whey
1 : Get an hair cut for God's sake !
"Task list:\n0 : Get the Whey\n1 : Get an hair cut for God's sake !"
>>> srp.SaveList.save_to_file(task_obj.task_list)
>>> 
"""
