# Array Function
from array import *
a = array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in range(len(a)):
    print(a[i])

a.append(11)
print(a)

a.insert(0, 100)
print(a)

a.pop()
print(a)

a.remove(2)
print(a)

a.reverse()
print(a)

print(a.count(5))

