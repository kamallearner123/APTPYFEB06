def find_non_repeat_chars(s):
    # Write your code here
    pass

if __name__ == '__main__':
    # Test case 1
    s = "hello"
    assert find_non_repeat_chars(s) == "h"

    # Test case 2
    s = "hello world"
    assert find_non_repeat_chars(s) == "w"

    # Test case 3
    s = "hello world, this is a test"
    assert find_non_repeat_chars(s) == "w"

    print("All testcases pass")
    