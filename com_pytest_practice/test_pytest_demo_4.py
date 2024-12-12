import pytest

@pytest.mark.skip(reason="Method not yet implemented")
def test_demo1():
    print("My Pytest Demo 1.")

@pytest.mark.xfail(reson="The failure is know issue.")
def test_demo2():
    print("My Pytest Demo 2.")

name = "dinesh"
@pytest.mark.skipif(name=="dinesh", reason="If the name is dinesh need to skip.")
def test_demo3():
    print("My Pytest Demo 3.")

@pytest.mark.parametrize("n", [1, 2, 3])
def test_demo4(n):
    print("The n is : ", n)

@pytest.mark.smoke
def test_demo5():
    print("This is Smoke testing method 5")

@pytest.mark.smoke
def test_demo6():
    print("This is Smoke testing method 6")

@pytest.mark.smoke
def test_demo7():
    print("This is Smoke testing method 7")

@pytest.mark.regression
def test_demo8():
    print("This is Regression testing method 8")

@pytest.mark.regression
def test_demo9():
    print("This is Regression testing method 9")

@pytest.mark.regression
def test_demo10():
    print("This is Regression testing method 10")
