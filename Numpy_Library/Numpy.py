import numpy as np
arr=np.array((1,2,3,4))
print(arr)
print(type(arr))#type of array
#0dimensial array
print("0 dimensional array")
arr=np.array(12)
print(arr)
#1dimensial array
print("1 dimensional array")
arr=np.array([12,2,3,4,6,9,10])
print(arr.dtype)#array datatype
print(arr[1:5])#it will print element from index 1 to 5
print(arr[4:])#not mentioned the endso it will print values from index 4
print(arr[:4])
print("value of array at indexes:",arr[0]+arr[2])#sum of value at index 0 and 2(12+3=15)
print("value of array at indexes:",arr[0],arr[2])
print(arr)
#2dimensial array
print("2 dimensional array")
arr=np.array([[12,2,3],[1,20,40]])
print("value of array at indexes:",arr[0,2],arr[0,1])
print("value of array at indexes:",arr[0,2]+arr[0,1])#sum of 2 indexes
print(arr)
#2dimensial array
print("3 dimensional array")
arr=np.array([[12,2,30],[1,20,40],[12,34,5]])
print(arr)
#to check dimensions of arrays
a=np.array(12)
b=np.array([12,2,3])
c=np.array([[12,2,3],[1,20,40]])
d=np.array([[12,2,3],[1,20,40],[12,34,5]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)