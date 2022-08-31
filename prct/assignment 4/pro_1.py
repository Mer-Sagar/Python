'''
1. Write a program to create a file and input five person full name in file and read the information
   from file. 

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

from logging import exception


try:
    with open("test1.txt","w") as f:
        for i in range(5):
            a= input("\n Enter Name : ")
            f.write(a+"\n")

    print("\n")
    with open("test1.txt","r") as f2:
        for j in f2:
            print(j.rstrip("\n"))

except FileNotFoundError:
    print("File not found")

except exception as e:
    print("Error : ", e)






























# try:
#     with open("pro_1data.txt", "w") as f:                        
#         for i in range(5):
#             name = input("Enter the name : ")
#             f.write(name + "\n")                              

#     print("Names are: ")
#     with open("Pro_1data.txt", "r") as file:        

#         for fline in file:                                       
#             print(fline.rstrip("\n"))
#             print()

# except FileNotFoundError:                         
#     print("File not found!!!")

# except Exception as e:                           
#     print("Exception occurred : ",e)

