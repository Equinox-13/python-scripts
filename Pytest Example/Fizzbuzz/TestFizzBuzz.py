import pytest

def fizzbuzz(value):
    if is_Multiple(value, 3):
        if is_Multiple(value, 5):
            return "FizzBuzz"
        return "Fizz"
    if is_Multiple(value, 5):
        return "Buzz"
    return str(value)


def is_Multiple(value, mod):
    return value % mod == 0

# No longer needed as the test case is covered in the subsequent cases
# def test_can_call_fizzbuzz():
#     fizzbuzz(1)

def check_fizzbuzz(value, expectedReturnValue):
    return_value = fizzbuzz(value)
    assert return_value == expectedReturnValue

def test_returns1With1PassedIn():
    # Removed similar code by creating a utility function for testing
    # return_value = fizzbuzz(1)
    # assert return_value == "1"
    check_fizzbuzz(1, "1")

def test_returns2With2PassedIn():
    check_fizzbuzz(2, "2")

def test_returnsFizzWith3PassedIn():
    check_fizzbuzz(3, "Fizz")

def test_returnsBuzzWith5PassedIn():
    check_fizzbuzz(5, "Buzz")

def test_returnsFizzWith6PassedIn():
    check_fizzbuzz(6, "Fizz")

def test_returnsBuzzwith10PassedIn():
    check_fizzbuzz(10, "Buzz")

def test_returnsFizzBuzzWith15PassedIn():
    check_fizzbuzz(15, "FizzBuzz")

def test_returnsFizzBuzzWith15PassedIn():
    check_fizzbuzz(15, "FizzBuzz")
