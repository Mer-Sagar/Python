"""
6.  Write a program to sort given string array in ascending order.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

import numpy as np

size = int(input("Enter the size of array : "))
lst1 = []

for i in range(size):
    item = input("Enter the string : ")
    lst1.append(item)

arr = np.array(lst1)

print("Before sorting : ", end=" ")

for i in range(size):
    print(arr[i], end=" ")

for i in range(size-1):
    min_index = i
    for j in range(i, size):
        if arr[min_index].lower() > arr[j].lower():
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]

print("\nAfter sorting : ", end=" ")

for i in range(size):
    print(arr[i], end=" ")
    