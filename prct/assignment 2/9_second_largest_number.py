'''
 9. Write a Python program to get the second largest number from a list.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''

lst = []
 
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input("Enter value : "))
 
    lst.append(ele) # adding the element
     
print(lst)

lst.sort()  #   lst.sort(reverse=True)  

print("The second largest element of the list is:", lst[-2])  