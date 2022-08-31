'''
 5. Write a Python program to add 'ing' at the end of a given string 
    (length should be at least 3). If the given string already ends with 'ing'
    then add 'ly' instead. If the string length of the given string is
    less than 3, leave it unchanged.
    
    Ex Input : test         Expected Output : testing
    If Input : testing      Expected Output: testingly
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
inpt_str = input("Enter a string: ")

if (len(inpt_str)>3):
    
    if (inpt_str[-3:]=="ing"):
        print(inpt_str + "ly")
    else:
        print(inpt_str + "ing")
else:
    print("please enter at least 3 chracter string")
    
