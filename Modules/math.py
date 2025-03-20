
print(f"Module name {__name__} is getting imported!!!")
def add(a,b):
    return a+b

def main():
    print("Going to test add function")
    assert add(10,20)==30


if __name__ == "__main__":
    main()
