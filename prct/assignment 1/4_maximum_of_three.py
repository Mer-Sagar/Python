'''
Write a program to determine the maximum of 3 numbers.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

m = int(input("Enter first number : "))
e = int(input("Enter second number : "))
r = int(input("Enter third number : "))

if (m>e) and (m>r):
    print("\n{0} is Maximum Number among three.".format(m))
elif (e>m) and (e>r):
    print("\n{0} is Maximum Number among three.".format(e))
else:
    print("\n{0} is Maximum Number among three.".format(r))