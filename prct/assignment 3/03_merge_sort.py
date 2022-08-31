"""
3.  Given the two 1-D arrays A and B, which are sorted in ascending order. Write a program to merge
    them into a single sorted array C that contains every item from arrays A and B, in ascending order.


Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

from array import *


def sorted_func(arr):
    
     for i in range(0, len(arr)):
         for j in range(i+1, len(arr)):
             
             if arr[i]>=arr[j]:
                 arr[i],arr[j] = arr[j], arr[i]
                 
     return arr

def print_array(a):
    size = len(a)
    for i in range(size):
        print(a[i], end=" ")



a1 = array('i',[])
b1 = array('i',[])
c = array('i',[])

no = int(input("Enter Number of element for both array : "))

for i in range(no):
    ele = int(input("Enter Element of A: "))
    a1.append(ele)
    
for i in range(no):
    ele = int(input("Enter Element of B : "))
    b1.append(ele)
        
a = sorted_func(a1)   
b = sorted_func(b1)

print("Array A : ", end="")
print_array(a)

print("\nArray B : ", end="")
print_array(b)

 
size = len(a1) + len(b1)

i=0
j=0

while i != len(a) and j != len(b):                      
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j +=1
 
while i != len(a):
    c.append(a[i])
    i += 1
   

while j != len(b):
    c.append(b[j])
    j += 1
   

print("\nResult Array C : ", end="")
print_array(c)
    
    
    
    