# test_hello_steps.py

import pytest
from pytest_bdd import scenario, given, when, then
from utils.helloprinting import Abc
from types import SimpleNamespace

# Load feature file
@scenario("../features/print_hello.feature","printing hello for user")
def test_something():
    pass


@pytest.fixture()
def import_from_utils() -> Abc:
    return Abc()

@pytest.fixture()
def context():
    return SimpleNamespace()



# Step Definitions
@given("i have access to computer")
def access_computer(import_from_utils, context):
    # You can simulate access setup here
    result=import_from_utils.printing_hello()
    context.message=result
    print(f"[Given] Stored in context {context.message}")
    pass

@when("user says hello")
def user_says_hello(context):
    # This would normally be user input logic; for now it's just a placeholder
    print(f"[WHEN] Context message is: {getattr(context, 'message', 'Not set')}")
    context.updated = context.message + " again"

@then("print hello")
def print_hello(context):
    print(f"[THEN] Final message: {context.updated}")
    assert context.updated == "Hello again"
