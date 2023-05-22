import pytest
import composite
from composite import *

def test_employee_hierarchy():
    emp = Employee("Amitabh")
    emp1 = Engineer("Shweta")
    emp2 = Architect("Suman")
    emp.reportees.append(emp1)
    emp.reportees.append(emp2)

    emp3 = Employee("Aadya")
    emp3.reportees.append(Engineer("Chota Dhruv"))
    emp3.reportees.append(Architect("Dhruv"))
    emp.reportees.append(emp3)

    expected_output = (
        "Amitabh (Manager)\n"
        " - Shweta (Engineer)\n"
        " - Suman (Architect)\n"
        " - Aadya (Manager)\n"
        " -  - Chota Dhruv (Engineer)\n"
        " -  - Dhruv (Architect)\n"
    )

    assert str(emp) == expected_output

def test_eng_designation():
    eng = Engineer("Amitabh")
    assert eng.designation == "Engineer"

def test_architect_designation():
    eng = Architect("Amitabh")
    assert eng.designation == "Architect"