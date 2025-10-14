import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([1, 2, 3])
arr3 = np.array([4, 6, 5])

a = 5
#input("Enter a number:" )

# arrr = np.concatenate((arr2, arr3))

# for i in arr:
#     print(arr[-i])


# i=len(arr)-1
# while i <=0 :
#     print(arr[i])

# print(arr[:4])
# print(arr[1:3:4])

# print(arr.dtype)
# print(arr2.dtype)

# print(arr2[1])

# print(arr.shape)

# for i in arr:
#     print(i)

# print(arrr)

# print(np.sort(arrr))   
# print(min(arrr))

for i in arr3:
    if a != i :
       i-=1
       
    else:
        print(arr3[i])
    

    
