def is_pallidrome(word):
    reverse_str = ''.join(reversed(word))
    return word == reverse_str

def test_is_pallidrome():
    input_str = "racecar"
    result = is_pallidrome(input_str)
    assert result == True

def test_is_pallidrome1():
    input_str = "kayak"
    result = is_pallidrome(input_str)
    assert result == True
    print("Test Passed! '" + input_str + "' is a palindrome.")