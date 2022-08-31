'''
9. In program no 6 display information from file in descending order of percentage.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''
import pickle, sys

class Student:

    def __init__(self):
        pass

    def stud_detail(self):
        self.roll=int(input("\n Enter Roll No : "))
        self.name = input("Enter your name : ")
        self.m1 = int(input("Enter Marks1 : "))
        self.m2 = int(input("Enter Marks2 : "))
        self.m3 = int(input("Enter Marks3 : "))
        self.m4 = int(input("Enter Marks4 : "))
        self.m5 = int(input("Enter Marks5 : "))
        self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        self.per = (self.tot * 100)/500

    def display_rec(self):
        print("\t\t\t\t\tMarksheet")
        print("Roll : ", self.roll)
        print("Name : ", self.name)
        print("m1 : ", self.m1)
        print("m2 : ", self.m2)
        print("m3 : ", self.m3)
        print("m4 : ", self.m4)
        print("m5 : ", self.m5)
        print("Total Marks : ", self.tot)
        print("Percentage : ", self.per)



try:

    no_rec = int(input("Enter Number Of Records : "))

    with open("test2.dat","wb") as f:
        
        for i in range(no_rec):
            s= Student()
            s.stud_detail()
            pickle.dump(s,f)            # (object, file handler)

    with open("test2.dat","rb") as f1:

        for i in range(no_rec):
            obj= pickle.load(f1)
            obj.display_rec()
            print()




except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)




'''
import pickle, sys

class Student:
    def __init__(self):
        pass    

    def setDetails(self):
        self.roll = int(input("Enter Roll No : "))
        self.name = input("Enter your name : ")
        self.m1 = int(input("Enter Marks1 : "))
        self.m2 = int(input("Enter Marks2 : "))
        self.m3 = int(input("Enter Marks3 : "))
        self.m4 = int(input("Enter Marks4 : "))
        self.m5 = int(input("Enter Marks5 : "))
        self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
        self.per = (self.tot * 100)/500


    def display(self):
        print("\t\t\t\t\tMarksheet")
        print("Roll : ", self.roll)
        print("Name : ", self.name)
        print("m1 : ", self.m1)
        print("m2 : ", self.m2)
        print("m3 : ", self.m3)
        print("m4 : ", self.m4)
        print("m5 : ", self.m5)
        print("Total Marks : ", self.tot)
        print("Percentage : ", self.per)

try:

    noofrec = int(input("Enter the number of records : "))
    with open("pro_6.dat", "wb") as f:
        for i in range(noofrec):
            print()
            s = Student()
            s.setDetails()
            pickle.dump(s,f)
    
    with open("pro_6.dat","rb") as f:
        for i in range(noofrec):
                obj=pickle.load(f)
                obj.display()
                print()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)
'''