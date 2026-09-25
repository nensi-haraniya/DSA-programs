#Dimensions Array
#Dimensions ndim Attribute
from numpy import*

arr1=array([1,2,3,4,5])
print(arr1.ndim)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.ndim)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.ndim)

#Dimensions shape Attribute
arr1=array([1,2,3,4,5])
print(arr1.shape)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.shape)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.shape)

#Dimensions size Attribute
arr1=array([1,2,3,4,5])
print(arr1.size)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.size)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.size)

#Dimensions shape Attribute
arr1=array([1,2,3,4,5])
print(arr1.itemsize)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.itemsize)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.itemsize)

#Dimensions shape Attribute
arr1=array([1,2,3,4,5])
print(arr1.dtype)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.dtype)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.dtype)

#Dimensions shape Attribute
arr1=array([1,2,3,4,5])
print(arr1.nbytes)

arr2=array([[1,2,3],[4,5,6]])
print(arr2.nbytes)

arr3=array([[[1,2,3],[4,5,6]],[[7,8,9],[2,7,5]]])
print(arr3.nbytes)
