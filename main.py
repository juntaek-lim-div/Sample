import a
import b
import os
import ctypes


if(__name__=="__main__"):
    print("program is running...")
    for i in range(0, 100):
        print("i = " + str(i))
        a.add(i,i)
        b.sub(i,i)
    os.system("pause")