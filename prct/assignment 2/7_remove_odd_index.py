'''
 7. Write a Python program to remove the characters which have odd index
    values of a given string.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
inpt_str = input("Enter a string: ")

new_str=''

if (len(inpt_str)>0):
    
    for i in range(0, len(inpt_str)):
        if(i%2==1):
            new_str =new_str + inpt_str[i]    
    
    print(new_str)   
        
else:
    print("Empty String")
    
