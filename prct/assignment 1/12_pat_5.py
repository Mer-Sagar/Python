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

for i in range(1,6):
    for j in range(1,i+1):        
       print(" ",end=" ")
       
    for k in range(1,7-i):
        print("*",end=" ")
       
    print()
    
