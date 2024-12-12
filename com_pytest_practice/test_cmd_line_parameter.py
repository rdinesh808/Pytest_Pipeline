import pytest

@pytest.fixture()
def test_start(name):
    if name=="dinesh":
        print(f"My name is {name}")
    elif name=="shruthy":
        print(f"My name is {name}")
    elif name=="dineshshruthy":
        print(f"My name is {name}")
    else:
        print("Name not matched")

def pytest_addoption(parser):
    parser.addoation("--name")


@pytest.fixture()
def name(request):
    return request.config.getoption("--name")