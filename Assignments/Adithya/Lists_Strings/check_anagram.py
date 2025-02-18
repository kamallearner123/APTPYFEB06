def find_anagram(s1, s2):
    s1=s1.lower()
    s2=s2.lower()
    if (len(s1) ==len(s2)):
        sorted_s1=sorted(s1)
        sorted_s2=sorted(s2)
        if (sorted_s1 == sorted_s2):
            return True
        else:
            return False
    else:
        return False
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
