'''
 6. Write a Python program to remove the nth index character from a
    nonempty string.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
inpt_str = input("Enter a string: ")

ind= int(input("Enter Index : "))

new_str=''

if (len(inpt_str)>0):
    
    for i in range(0, len(inpt_str)):
        if(i != ind):
            new_str =new_str + inpt_str[i]    
    
    print(new_str)
   
        
else:
    print("Empty String")
    
