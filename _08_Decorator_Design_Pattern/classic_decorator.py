from dataclasses import dataclass, field
import random
import string
import time

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        stop = time.time()
        print(f'>>> Total time taken : {int((stop-start)*1000)}ms')
        return ret
    return wrapper

def generate_id(classname):
        return classname.upper() + "".join(random.choices(string.ascii_uppercase, k=12))

@dataclass
class Person:
    name: str
    email: str
    address: str
    age: int
    id: str = field(init=False) #, default_factory=generate_id)
    _search_string: str = field(init=False, repr=False)

    def __post_init__(self) -> None:
        print(f'{type(self).__name__}')
        self.id = generate_id(classname=f'{type(self).__name__}')
        self._search_string = f'{self.name} {self.address}'
        time.sleep(1)

    def __str__(self) -> str:
        print(f'{type(self).__name__}')
        return f'{self.name} lives in {self.address}'

@timeit
def main() -> None:
    person = Person(name="Amitabh", email="amitabh@ainebula.in", address="India", age=31)
    print(person)
    print(repr(person))
    person.address = "Bangalore, India"
    print("After change")
    print(person)
    print(repr(person))

if __name__ == '__main__':
    main()


OUTPUT = r"""
Person
Person
Amitabh lives in India
Person(
    name='Amitabh', email='amitabh@ainebula.in',
    address='India', age=31, id='PERSONGDCGFANNDDDW'
    )
>>> Total time taken : 1009ms
"""
