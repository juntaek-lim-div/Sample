import a
import b
import os

RootDIR = os.path.dirname(os.path.abspath(__file__))

#read test.txt
with open(RootDIR + '/test.txt', 'r') as f:
    print(f.read())
for i in range(10):
    a.add(i,i)
    b.sub(i,i)
os.system('pause')