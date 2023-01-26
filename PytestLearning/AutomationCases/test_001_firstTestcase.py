import pytest
# Testcase code written must be inside a method
# Method name must be started with test
actual_result = "Hello"
a = 102
# @pytest.mark.skipif(a > 100, reason="This is not working..")
@pytest.mark.TopPriority
def test_Login_Logout_Testing():
    print("This is first testcase..")
    print("Testcase end.")
    assert actual_result != "Hi", "These 2 values must not be same"

@pytest.mark.Sanity
def test_Logout_invalid_credentials():
    print("This is testcase 3..")
    print("testcase 3 end.")

# Print statement output display on console -s
# Verbose mode display test cases name with status -v