def rotate_list(list1, 2):
    pass

if __name__ == '__main__':
    # Test case 1
    list1 = [1, 2, 3, 4, 5]
    rotate_list(list1, 2)
    assert list1 == [4, 5, 1, 2, 3]

    # Test case 2
    list1 = [1, 2, 3, 4, 5]
    rotate_list(list1, 3)
    assert list1 == [3, 4, 5, 1, 2]

    # Test case 3
    list1 = ["david", "john", "james", "lara"]
    rotate_list(list1, 2)
    assert list1 == ["james", "lara", "david", "john"]

    print("All testcases pass")


