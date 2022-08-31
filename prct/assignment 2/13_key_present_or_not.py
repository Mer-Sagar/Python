'''
 13. Write a Python program to check if a given key already exists in a
     dictionary.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''

dict = {'a': 100, 'b':200, 'c':300}

inpt_key= input("Enter Key : ")


if inpt_key in dict:
    print("Present, ", end =" ")
    print("value =", dict[inpt_key])
else:
    print("Not present")
  


  

