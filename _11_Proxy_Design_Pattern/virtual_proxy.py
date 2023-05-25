"""
VIRTUAL DESIGN PATTERN
======================

This design pattern is aimed at better object mamagement.
It controls the access to real object by behaving as suppogate object 
to the real underlying object.

It aims at providing a virtual object to work with classes and functions
that warrent need of a costly / expensive objects (like a database object).

Its synonymous to Laxy evaluation. Let's see first, the example without and
then with the VirtualProxy class.

We will see an example of DataBase
"""

from dataclasses import dataclass, field

@dataclass
class DBEval:
    """
    Class representation of a Database class
    """
    name: str

    def __post_init__(self) -> None:
        print(f'{self.name} database loaded')

    def query_db(self, query):
        """
        Responds to the query asked

        ARGS:
            query (str) : Query to be asked
        """   
        print(f"Sending back the query result for {query}")

def db_query(db, query):
    """
    Interface to get query from the database
    """
    print("Sending query to DB")
    db.query_db(query)
    print("Query succesful!")

OUTPUT_NO_VP = r"""

if __name__ == "__main__":
    db = DBEval("mongoDB")
    db_query(db, "get_name")

mongoDB database loaded
Sending query to DB
Sending back the query result.
Query succesful!
"""

@dataclass
class LazyDBeval:
    """
    Proxy Class representation of a Database class
    """
    name: str
    _db_instance: DBEval = None

    def query_db(self, query):
        """
        Responds to the query asked

        ARGS:
            query (str) : Query to be asked
        """
        if not self._db_instance:
            self._db_instance = DBEval("mongo")
        self._db_instance.query_db(query)


if __name__ == "__main__":
    db = LazyDBeval("mongoDB")
    db_query(db, "get_name")
    db_query(db, "get_address")

OUTPUT_2 = r"""
You can see that the first time the class did not load the object 
as the line db_query(db, "get_name") was commented out.

Next time, when I ran it, it load the object only after that.

Sending query to DB
mongo database loaded
Sending back the query result.
Query succesful!


And a third time, i repeated the command and the object was not reloaded.
It continued to give output using the same object

Sending query to DB
mongo database loaded
Sending back the query result for get_name
Query succesful!
Sending query to DB
Sending back the query result for get_address
Query succesful!
"""
