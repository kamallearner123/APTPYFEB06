from accounts import Account
# import bank # bank.Account
# from bank import *

VERSION = "1.0.0"

a1 = Account(user="Kamal", passwd="root123") # __init__ is called from class
a1.deposite(-100)
a1.withdraw(10)
