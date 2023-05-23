import pytest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _01_Builder_Design_Pattern import builder
from _01_Builder_Design_Pattern.builder import *


class TestBuilder:

    @pytest.fixture
    def choose_pizza(self):
        choice="margarita"
        print(Pizza(choice).name)
        return Pizza(choice).name

    def setup_method(self):
        print("Setup called")
    
    def teardown_method(self):
        print("Teardown called.")
    
    def test_pizza_init(self, choose_pizza):
        assert choose_pizza == "margarita"
    
    def test_pizza_dough(self):
        pizza = Pizza("margherita")
        pizza.prepare_dough("thin")
        assert pizza.dough == "thin"
    
    def test_pizza_topping(self):
        pizza = Pizza("margarita")
        marg = MargaritaBuilder()
        marg.pizza = pizza
        marg.add_topping()
        print(f"Pizza Topping : {pizza.topping}")
        assert pizza.topping[0] == [PizzaTopping.double_mozzarella, PizzaTopping.oregano]
    
    def test_add_sauce(self):
        pizza = Pizza("creamy bacon")
        crba = CreamyBaconBuilder()
        crba.pizza = pizza
        crba.add_sauce()
        print(f"Pizza sauce is {crba.pizza.sauce}")
        assert crba.pizza.sauce == PizzaSauce.creme