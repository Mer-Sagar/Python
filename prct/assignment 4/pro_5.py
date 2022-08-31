'''
5.  Write a program fetch the binary information from the file and convert it in to the string so 
    that you can perform all the operation of string on that information.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

try:
    with open("pro_5file.dat","rb") as f:
        str = f.read().decode()
        print(str)
        
except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)
