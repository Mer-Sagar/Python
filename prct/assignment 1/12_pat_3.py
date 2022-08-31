'''
Generate the following pattern:
    * * * * *
    * * * *
    * * *
    * *
    *

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

for i in range(5,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()
    
