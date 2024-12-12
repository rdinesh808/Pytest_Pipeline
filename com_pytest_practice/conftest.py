import pytest

@pytest.fixture(scope="class")
def start():
    print("I am Starting....")
    yield
    end()

def end():
    print("I am completed....")


@pytest.fixture(scope="function")
def bstart():
    print("Before test")
    yield
    aend()

def aend():
    print("After test")