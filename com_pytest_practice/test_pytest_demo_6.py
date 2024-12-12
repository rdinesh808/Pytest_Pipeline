import pytest

class TestOrder:
    @pytest.mark.third
    def test_demo1(self):
        print("My Pytest Demo 1. Third")
        assert 1+2 == 3

    @pytest.mark.first
    def test_demo2(self):
        print("My Pytest Demo 2. First")

    @pytest.mark.second
    def test_demo3(self):
        print("My Pytest Demo 3. Second")