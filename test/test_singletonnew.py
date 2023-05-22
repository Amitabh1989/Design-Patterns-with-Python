import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _04_Singleton_Design_Pattern import singleton_2
from _04_Singleton_Design_Pattern.singleton_2 import SingletonNew

def test_singleton_behavior():
    person1 = SingletonNew()
    person2 = SingletonNew()
    
    assert person1 != person2  # Both objects should be equal
    assert person1.name == person2.name  # Name should be the same
    
    person1.name = "Amitabh Suman"
    assert person1.name == person2.name  # Name change should reflect in both objects

    assert person1.position == "CEO"  # Position should be the same
    assert person2.position == "CEO"

    assert str(person1) == "Amitabh Suman is a CEO in the company!"
    assert str(person2) == "Amitabh Suman is a CEO in the company!"
