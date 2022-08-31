'''
Write a program that reads the percentage obtained by the students and 
determines and prints the class obtained by the student as per 
the following rules
    Percentage  Class
    0 - 39      Fail
    40 - 59     Second class
    60 - 79     First class
    80 - 100    Distinction.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

per = int(input("Enter Percentage : "))

if (per>=80 and per<=100):
    print("Student pass with Distinction")
elif (per>=60 and per<=79):
    print("Student pass with First class")
elif (per>=40 and per<=59):
    print("Student pass with Second class")
elif (per>=0 and per<=39):
    print("Fail, Batter Luck next Time!!")
else:
    print("Please enter valid percentage")



