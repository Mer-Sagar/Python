'''
 2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
 Ex Input : beautiful Expected Output : beul
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
value = input("Enter a string: ")

if len(value) < 2 :
    print("Value is too sort...")
else:
    print(value[0:2]+value[-2:])