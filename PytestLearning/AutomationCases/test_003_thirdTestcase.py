import pytest

@pytest.mark.Smoke
def test_Login_Logout_Testing():
    print("This is first testcase..")
    print("Testcase end.")

@pytest.mark.Sanity
def test_Logout_invalid_credentials():
    print("This is testcase 3..")
    print("testcase 3 end.")

