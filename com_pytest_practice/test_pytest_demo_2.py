import pytest

@pytest.fixture(scope='function', autouse=True)
def setup():
    print("Start")
    yield
    endup()

def endup():
    print("End")

def test_demo1():
    print("My Pytest Demo 1.")
    
def test_demo2():
    print("My Pytest Demo 2.")

def test_demo3():
    print("My Pytest Demo 3.")