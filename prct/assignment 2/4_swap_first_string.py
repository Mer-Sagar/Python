'''
4. Write a Python program to get a single string from two given strings,
   separated by a space and swap the first two characters of each string.

    Ex Input : st1=hello st2=world
    Expected Output : st3=wollo herld
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

inpt_str = input("Enter a string: ")

x = inpt_str.split()    #split by " "

st1=x[0]        #type conversion list to string
st2=x[1]        

new1=st1.replace(st1[:2], st2[:2])  #replace(old, new)

new2=st2.replace(st2[:2], st1[:2])

print(new1)
print(new2)


