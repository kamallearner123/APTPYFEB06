def find_non_repeat_chars(s):
    p=[]
    for char in s:
        p.append(char)
    for i in p:
        count=p.count(i)
        if count==1:
            print(i)
            return i

if __name__ == '__main__':
    # Test case 1
    s = "hello"
    assert find_non_repeat_chars(s) == "h"

    # Test case 2
    s = "hello world"
    assert find_non_repeat_chars(s) == "h"

    # Test case 3
    s = "hello world, this is a test"
    assert find_non_repeat_chars(s) == ","

    print("All testcases pass")
    
