'''
 3. Write a Python program to get a string from a given string 
    where all occurrences of its first char have been changed to '$', 
    except the first char itself.
    Ex Input : abracadabra Expected Output : abr$c$d$br$
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''
str1 = input("Enter a string: ")

char = str1[0]
str1 = str1.replace(char, '$')

str1 = char + str1[1:]
print(str1)