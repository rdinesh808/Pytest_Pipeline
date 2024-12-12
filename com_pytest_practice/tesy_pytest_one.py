import pytest

@pytest.mark.usefixtures("start")
@pytest.mark.usefixtures("bstart")
class TestOne:
    def test_t1(self):
        print("I am Test One Class Test 1 Method.")

    def test_t2(self):
        print("I am Test One Class Test 2 Method.")

    def test_t3(self):
        print("I am Test One Class Test 3 Method.")