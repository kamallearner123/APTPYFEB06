def remove_duplicates(data):
    """
    This function removes duplicates from the list and returns a new list without duplicates.
    """
    # Write your code here
    return list(set(data))

if __name__ == '__main__':
    # Test case 1
    data = [1, 2, 3, 4, 5, 1, 2, 3]
    assert remove_duplicates(data) == [1, 2, 3, 4, 5]

    # Test case 2
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
    assert remove_duplicates(data) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test case 3
    data = ["david", "john", "james", "lara", "david", "john"]
    assert remove_duplicates(data) == ["david", "john", "james", "lara"]

    print("All testcases pass")
    