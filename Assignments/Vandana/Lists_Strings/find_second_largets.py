def find_second_largest(arr):
    # Write your code here
    pass

if __name__ == '__main__':
    # Test case 1
    arr = [1, 2, 3, 4, 5]
    assert find_second_largest(arr) == 4

    # Test case 2
    arr = [1, 2, 3, 4, 5, 6]
    assert find_second_largest(arr) == 5

    # Test case 3
    arr = [1, 2, 3, 4, 5, 6, 7]
    assert find_second_largest(arr) == 6

    # Test case 4
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    assert find_second_largest(arr) == 7

    # Test case 5
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert find_second_largest(arr) == 8

    # Test case 6
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert find_second_largest(arr) == 9

    print("All testcases pass")