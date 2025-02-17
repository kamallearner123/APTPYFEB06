def func1():
    print("func1() called form module ", __name__)


if __name__ == '__main__': #mentioning :
    print("my module ", __name__)

    # 1) Collect number of nums
    n = int(input())
    inputs = input().split() # Splitting with space
    print(f"inputs = {inputs}")

    nums = []
    for i in inputs:
        nums.append(int(i))
    print(f"nums = {nums}")

    hash_value = hash(tuple(nums))
    print(hash_value)
    
