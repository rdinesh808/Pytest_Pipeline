import pytest

@pytest.mark.dependency()
def test_demo1():
    print("My Pytest Demo 1.")
    assert 1+2 == 3

@pytest.mark.dependency(depends=["test_demo1"])
def test_demo2():
    print("My Pytest Demo 2.")

@pytest.mark.dependency(depends=["test_demo1", "test_demo2"])
def test_demo3():
    print("My Pytest Demo 3.")