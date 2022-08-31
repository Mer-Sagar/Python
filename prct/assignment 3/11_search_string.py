"""
11. Write a program that search an item from array of string.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""
import numpy as np

str1 = input("Enter the string : ")
find_str = input("Enter the item to find : ")
lst1 = str1.split()

str_arr = np.array(lst1)

flag = False

for i in range(len(str_arr)):

    if str_arr[i] == find_str:
        print("Item at index : ", i+1)
        flag = True
        break

if not flag:
    print("Item", find_str, "not found")