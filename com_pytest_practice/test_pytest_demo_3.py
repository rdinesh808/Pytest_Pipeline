import pytest


class TestPy:
    def endup(self):
        print("End")

    @pytest.fixture(scope='class', autouse=True)
    def setup(self):
        print("Start")
        yield
        self.endup()

    def test_demo1(self):
        print("My Pytest Demo 1.")

    def test_demo2(self):
        print("My Pytest Demo 2.")

    def test_demo3(self):
        print("My Pytest Demo 3.")
