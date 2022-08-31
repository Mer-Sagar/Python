"""
7.  Write a program that will read a text and count all occurrences of a particular word.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""

str1 = input("Enter the string : ")
word1 = input("Enter the word : ")

split_str = str1.split(" ")
count = 0

for i in range(len(split_str)):
    if word1 == split_str[i]:
        count += 1
        flag=1
        break;


print("Count : ", count)