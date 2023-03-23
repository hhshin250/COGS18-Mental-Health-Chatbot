from my_module.classes_functions import *
import random

def test_User():
    assert self.name
    assert self.age
    assert self.prev_conditions
    assert isinstance(self.name, str)
    assert isinstance(self.age, str)
    assert isinstance(self.prev_conditions, str)    

def test_add_user():
    add_user("Danny", 20, "Yes")
    # Check if user is added to dictionary
    assert users["Danny"].name == "Danny"
    
def test_help_user():
    # Test existing user
    users["Danny"] = User("Danny", 20, "Yes")
    assert help_user("Danny") == "Welcome back Danny!"

    # Test with new user
    assert help_user("Heidi") == "Hello new user Heidi!"
    
# Test suggestion
def test_suggestion():
    assert random.choice(suggestion) in suggestion

# Test affirmation
def test_affirmation():
    assert random.choice(affirmation) in affirmation

def test_describe_depression():
    assert describe_depression() == print(depression_description)

def test_describe_anxiety():
    assert describe_anxiety() == print(anxiety_description)
