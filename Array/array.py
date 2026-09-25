import array
a=array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])

import array as ar
a=ar.array('i',[10,20,30])
for i in range(3):
    print(a[i])

from array import*
a=array('i',[10,20,30])
for i in range(3):
    print(a[i])

    
print(a[1::1])
print(a[1:3:])
print(a[::1])
