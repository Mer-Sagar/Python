"""
1.  Write a program to find maximum element from 1-Dimensional array.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

from array import*

max=0

arr= array('i',[])

no_ele= int(input("\n Enter Number of element : "))

for i in range(no_ele):
    ele = int(input("\n Enter Element : "))
    arr.append(ele)

    if ele>max:
        max=ele
    
print("Max element is : ",max)














# from array import*

# max = 0

# arr=array('i',[])
# no = int(input("Enter Number Of elements : "))

# for i in range(no):
#     s= int(input("Enter element : "))
#     arr.append(s)
    
#     if(s>max):
#         max=s
        
# print("Max number among this elements : ", max)
   
    


