'''
Generate the following pattern:
    5
    54
    543
    5432
    54321

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
'''

for i in range(5,0,-1):                
    for j in range(5,i-1,-1):        
       print(j,end=" ")  
    print()
   
    
