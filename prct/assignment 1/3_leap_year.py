'''
Write a program to tell if a year is a leap year Or Not.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

year = int(input("Enter Year : "))

if (year % 400 == 0) or (year % 100!=0) and (year % 4 ==0):
    print("{0} is Leap Year.".format(year))
else:
    print("{0} is not Leap Year.".format(year))