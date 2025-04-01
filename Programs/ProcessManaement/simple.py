
# 1) Import
from multiprocessing import Process
import os

def fun(msg):
    print("Child: Message recieved form parent = ", msg)
    print("Child: My process id = ", os.getpid())
    print("Child: my parent process  id = ", os.getppid())

if __name__=="__main__":
    print("Parent: Pid = ", os.getpid())
    p1 = Process(target=fun, args=('''Message from parent''',))
    p1.start()
    p1.join()
