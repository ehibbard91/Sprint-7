import math

def compute_factorial(number):
    return math.factorial(number)

def test_compute_factorial():
    input_num = 5
    result = compute_factorial(input_num)
    assert result ==120

    print("Test Passed! The factorial of " + str(input_num) + " is " + str(result))