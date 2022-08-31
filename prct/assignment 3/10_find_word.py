"""
10.  Write a program that finds a given word in a string.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

str1 = input("Enter the string : ")
word1 = input("Enter the word : ")


split_str_lst = str1.split(" ")
count = 0

flag=0

for i in range(len(split_str_lst)):
    if word1 == split_str_lst[i]:
        flag=1
        break;

if(flag==1):
      print("Yes this word is in the string!")
      
else:
      print("No this word is not found in string!")