"""
FACADE DESIGN PATTERN
=====================

The Facade pattern provides a simplified interface or API that hides the
complex underlying implementation details. Clients can interact with the
Facade to perform their tasks without needing to understand or deal with
the complexities of the subsystems involved. This promotes a simpler and
more straightforward interaction between the client and the system.

Let's see here.

"""

from dataclasses import dataclass, field
from enum import Enum
import abc
from abc import ABCMeta

State = Enum("State", "new running sleeping restart zombie")

@dataclass
class Server(metaclass=ABCMeta):
    """
    Abstract base class for servers.
    """
    @abc.abstractmethod
    def boot(self):
        """
        Abstract method for booting the server.
        """
        pass

    @abc.abstractmethod
    def kill(self):
        """
        Abstract method for killing the server.
        """
        pass

@dataclass
class FileServer(Server):
    """
    Concrete implementation of FileServer server.
    """
    name: str = 'FileServer'
    state: Enum = State.new

    def boot(self):
        print(f'{self.name} booted up!')
    
    def kill(self, restart=True):
        print(f'{self.name} killed!')
        if restart:
            print(f'{self.name} restarted!')
    
    def create_file(self, user, name, permission):
        """
        Create a file for a user with the specified name and permission.

        Args:
            user (str): User for whom the file is created.
            name (str): Name of the file.
            permission (str): Permission of the file.

        Returns:
            str: Message indicating the file creation.
        """
        return f'Created file for user {user} ({name} with permissions: {permission})'
    

@dataclass
class ProcessServer(Server):
    """
    Concrete implementation of ProcessServer server.
    """
    name: str = 'ProcessServer'
    state: Enum = State.new

    def boot(self):
        print(f'{self.name} booted up!')
    
    def kill(self, restart=True):
        print(f'{self.name} killed!')
        if restart:
            print(f'{self.name} restarted!')
    
    def create_process(self, user, name):
        """
        Create a process for a user with the specified name.

        Args:
            user (str): User for whom the process is created.
            name (str): Name of the process.

        Returns:
            str: Message indicating the process creation.
        """
        return f'Created process for user {user} ({name})'

@dataclass
class OperatingSystem:
    """
    The Facade class for interacting with servers.
    """
    fs: FileServer = field(default_factory=FileServer)
    ps: ProcessServer = field(default_factory=ProcessServer)

    def __post_init__(self) -> None:
        """
        Initialization after object creation.
        """
        print("OS Booted up!")

    def start(self):
        """
        Start the servers.
        """
        [p.boot() for p in [self.fs, self.ps]]
    
    def shutdown(self):
        """
        Shutdown the servers.
        """
        [p.kill() for p in [self.fs, self.ps]]
    
    def restart(self):
        """
        Restart the servers.
        """
        [p.kill(restart=True) for p in [self.fs, self.ps]]

    def create_file(self, user, name, permission):
        """
        Create a file using the FileServer.

        Args:
            user (str): User for whom the file is created.
            name (str): Name of the file.
            permission (str): Permission of the file.

        Returns:
            str: Message indicating the file creation.
        """
        return self.fs.create_file(user, name, permission)

    def create_process(self, user, name):
        """
        Create a process using the ProcessServer.

        Args:
            user (str): User for whom the process is created.
            name (str): Name of the process.

        Returns:
            str: Message indicating the process creation.
        """
        return self.ps.create_process(user, name)
        

def main() -> None:
    os = OperatingSystem()
    os.start()
    os.create_file("Amitabh", "hello-world.txt", "r r-w")
    os.create_process("Amitabh", "calm")
    os.shutdown()
    os.restart()

if __name__ == '__main__':
    main()

OUTPUT = r"""
OS Booted up!
FileServer booted up!
ProcessServer booted up!
FileServer killed!
FileServer restarted!
ProcessServer killed!
ProcessServer restarted!
FileServer killed!
FileServer restarted!
ProcessServer killed!
ProcessServer restarted!
"""
