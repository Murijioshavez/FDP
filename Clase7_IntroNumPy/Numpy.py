import numpy as np

my_list = [1, 2, 3, 4, 5]
arr = np.array(my_list)
print(arr)

zeros = np.zeros(5)
print(zeros)

ones = np.ones(5)
print(ones)

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1)
print(arr2)
resultado = arr1 + arr2
print(resultado)

arr = np.array([1, 2, 3])
result = arr + 5
print(result)

arr1 = np.array([1, 2, 3]) #Columnas
arr2 = np.array([[10], [20], [30]]) #filas
result = arr1 + arr2
print(result)

arr = np.array([1, 2, 3, 4, 5])
slice = arr[1:4]
print(slice)

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
result = arr[mask]
print(result)

arr = np.array([1, 2, 3, 4, 5])
indices = np.array([0, 2, 4])
result = arr[indices] 

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
concatenated = np.concatenate((arr1, arr2))

#División
arr = np.array([1, 2, 3, 4, 5, 6])
split = np.split(arr, 3)
print(split)