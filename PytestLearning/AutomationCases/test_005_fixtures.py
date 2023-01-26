import pytest

@pytest.fixture(scope = "module")
def fixture_code():
    print("This is our fixture code execute before testcase.")
    print("-------------------------------------------------")
    yield
    print("close DB connection after executing the testcase.")
    print("-------------------------------------------------")

@pytest.mark.Smoke
def test_Login_Logout_Testing(fixture_code):
    print("This is Smoke testcase....")
    print("End of the testcase")

@pytest.mark.Sanity
def test_Logout_invalid_values(fixture_code):
    print("This is Sanity testcase..")
    print("end of the testcase")