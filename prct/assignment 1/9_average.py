'''
Write a program to calculate the average of a set of n given numbers.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

n = int(input("Enter Number of Element : "))
avg=0

for i in range(n):
    num = int(input("Enter value : "))
    avg= avg+ num;

print("\n Average of {0} Number is : {1}".format(n,avg/n))
    
    
    





