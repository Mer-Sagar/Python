'''
8. Write a program to insert employee record and read the data from 3rd record.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

import pickle, sys

class Employee:
    def __init__(self):
        pass  

    def setDetails(self):
        self.id = int(input("Enter id : "))
        self.name = input("Enter name : ")

    def showDetails(self):
        print("\n\t\t\t\t\tEmployee Details")
        print("Id : ", self.id)
        print("Name : ", self.name)
        

try:
    noofrec = int(input("Enter the number of records : "))
    with open("pro_6.dat", "wb") as f:
        for i in range(noofrec):
            print()
            s = Employee()
            s.setDetails()
            pickle.dump(s,f)
            if(i==1):
                point = int(f.tell())
    
    
    
    with open("pro_6.dat","rb") as f:  
            for i in range(0, 2):
                obj=pickle.load(f)

            for i in range(2, noofrec):
                obj=pickle.load(f)
                obj.showDetails()
                print()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)

