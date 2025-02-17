def find_anagram(s1, s2):
    # Write your code here
    pass

if __name__ == '__main__':
    # Test case 1
    s1 = "listen"
    s2 = "silent"
    assert find_anagram(s1, s2) == True

    # Test case 2
    s1 = "triangle"
    s2 = "integral"
    assert find_anagram(s1, s2) == True

    # Test case 3
    s1 = "hello"
    s2 = "world"
    assert find_anagram(s1, s2) == False

    print("All testcases pass")