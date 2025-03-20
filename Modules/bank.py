from accounts import Account # from local dir
import pandas as pd # from standard python path
# import bank # bank.Account
# from bank import *

VERSION = "1.0.0"

a1 = Account("kamal", 10, "Kamal", "root123") # __init__ is called from class
a1.deposite(-100)
a1.withdraw(10)


