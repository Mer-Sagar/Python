'''
 1. Write a Python program to calculate the length of a string.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
str = input("Enter a string: ")

# counter variable to count the character in a string
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)  

 # using function : len(str) 
print("Using Function Length of the input string is : ", len(str))