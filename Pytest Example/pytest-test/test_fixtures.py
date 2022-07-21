import pytest

# Runs fixtures for all the unit tests
# @pytest.fixture(autouse=True)

@pytest.fixture()
def setup():
    print("\nSetup")

def test1():
    print("\nExecuting test1")
    assert True

# Used to execute a fixture
@pytest.mark.usefixtures("setup")
def test2():
    print("\nExecuting Test2")
    assert True
