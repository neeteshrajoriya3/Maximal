"""from pytest_bdd import scenario, given, when, then
from steps.project_steps import print_hello
import pytest

# Link the test function to the feature file scenario
@scenario("../features/project.feature", "Print message")
def test_hello():
    pass

@pytest.fixture
@given('I have a function that prints "Hello, World!"')
def hello_function():
    return print_hello  # Return the function itself

@pytest.fixture
@when("I execute the function")
def when_execute(hello_function):
    return hello_function()  # Call the function and return its result

@then('it should print "Hello, World!"')
def then_validate_output(when_execute):
    assert when_execute == "Hello, World!"  # Validate the function output
"""