'''
 10. Write a program to remove all the duplicate elements from list.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''

lst = []
 
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input("Enter value : "))
 
    lst.append(ele) 

print("Orignel List : ",end=(" "))
print(lst)


print("Remove duplicate from List : ",end=(" "))
print(list(set(lst)))

# dup_items = set()
# uniq_items = []
# for x in lst:
#     if x not in dup_items:
#         uniq_items.append(x)
#         dup_items.add(x)

# print(dup_items)
