import a
import b
import os
import ctypes

RootDIR = os.path.dirname(os.path.abspath(__file__))
print(f"RootDIR: {RootDIR}")
#read test.txt
with open(RootDIR + '/test.txt', 'r') as f:
    print(f.read())
    
#load dll
dll = ctypes.cdll.LoadLibrary(RootDIR + '/opu.dll')
print(dll.CameraModel())
for i in range(10):
    a.add(i,i)
    b.sub(i,i)
os.system('pause')