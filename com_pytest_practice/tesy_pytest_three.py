import pytest

@pytest.mark.usefixtures("start")
@pytest.mark.usefixtures("bstart")
class TestTwo:
    def test_t7(self):
        print("I am Test One Class Test 7 Method.")

    def test_t8(self):
        print("I am Test One Class Test 8 Method.")

    def test_t9(self):
        print("I am Test One Class Test 9 Method.")