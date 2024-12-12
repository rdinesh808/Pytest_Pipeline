import pytest

@pytest.mark.usefixtures("start")
@pytest.mark.usefixtures("bstart")
class TestTwo:
    def test_t4(self):
        print("I am Test One Class Test 4 Method.")

    def test_t5(self):
        print("I am Test One Class Test 5 Method.")

    def test_t6(self):
        print("I am Test One Class Test 6 Method.")