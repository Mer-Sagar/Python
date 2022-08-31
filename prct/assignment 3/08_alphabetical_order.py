"""
8.  Write a program that will read a string and rewrite it in the alphabetical order.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

# def sortString(str):                #done using sorted and join method
#     return ''.join(sorted(str))
      

str = input("Enter the string : ")
# print(sortString(str))

lst1 = list(str)            # convert string into list


for i in range(len(lst1)-1):
    min_index = i
    for j in range(i+1, len(lst1)):
        if lst1[min_index].lower() > lst1[j].lower():
            min_index = j
    lst1[i], lst1[min_index] = lst1[min_index], lst1[i]
    
str1 = "".join(lst1)

print(str1)