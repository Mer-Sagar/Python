'''
10. Write a program to display all the line starting with the word entered by user from the file.

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

try:
    fname = input("Enter file name : ")
    word = input("Enter word to be searched : ")
    f = open(fname)
    for line in f:
        if line.startswith(word):
            print(line)
    f.close()

except FileNotFoundError:                         
    print("File not found!!!")

except Exception as e:                           
    print("Exception occurred : ",e)


