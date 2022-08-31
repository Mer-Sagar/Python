'''
Generate the following pattern:
    * * * * *
    *       *
    *       *
    *       *
    * * * * *

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")        
    print()
    
