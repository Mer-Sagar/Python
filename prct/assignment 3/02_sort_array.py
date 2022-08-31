"""
2. Write a program to sort given array in ascending order.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

from array import *


def sorted_arr(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):

            if arr[i]>=arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr








arr = array('i',[])

size = int(input("Enter Number of Element : "))

for i in range(size):
    ele = int(input("Enter element : "))
    arr.append(ele)


c= sorted_arr(arr)

for i in range(size):
    print(c[i],end=" ")







# from array import *


# def sorted_func(arr):
    
#     for i in range(0, len(arr)):
#         for j in range(i+1, len(arr)):
             
#             if arr[i]>=arr[j]:
#                 arr[i],arr[j] = arr[j], arr[i]
                 
#     return arr
   

# arr = array('i',[])

# no = int(input("Enter Number of element : "))

# for i in range(no):
#     ele = int(input("Enter Element : "))
#     arr.append(ele)
        
    
# c= sorted_func(arr)   

# print("-------------")
# for i in range(no):
#     print(c[i],end=" ")

# --------------------------------------------------------

# arr1 = sorted(arr)   
    
# for i in range(no):
#     print(arr[i],end=" ")    
    