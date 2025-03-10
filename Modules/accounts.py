
VERSION = "1.1.1"


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__address = "White Field"


class Account(Person):
    count = 0
    names = []
    __address = "White Field"
    __balance = 0
    def __init__(self, name, age, userame, passwd, address="White Field"):
        #Account.count += 1
        self.__class__.count += 1 # Accessing+Modifying class variable
        self.__class__.names.append(userame)
        
        print(self.count)
        #self.count = 1 # Creating instance variable 
        
        name = "Harish"
        # Read the data from DB using user name
        self.name = userame
        self.passwd_from_db = "root123"
        self.__balance = 0
        self.validated = -2

        if passwd == self.passwd_from_db:
            print("Validated: SUCCESS")
            self.validated = 0 # creating
        else:
            print("Invalid password")
            self.validated = -1 # creating
            return None
            
    # Instance method
    def withdraw(self, amount):
        if self.__balance<amount:
            print("Not a sufficient balance!!!")
            return
        if self.validated != 0:
            print("Invalid ops")
            return False
        self.__balance -= amount
        self.__class__.update_balance(-amount)
        return True

    # Instance method
    def deposite(self, amount):
        if amount <= 0:
            print("Invalid deposite!!!")
            return
        if self.validated != 0:
            print("Invalid ops")
            return False
        self.__balance += amount
        self.__class__.update_balance(amount)
        return True
        
    @classmethod
    def get_info(cls): # Class method
        for name in cls.names: # Head ache
            print(f"User Name = {name}")
        print(f"Total Banks Balance = {cls.balance}")

    @classmethod
    def update_balance(cls, difference):
        cls.balance += difference
        print(f"Banks Balance: {cls.balance}")

