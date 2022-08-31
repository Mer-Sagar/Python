'''
Generate the following pattern:
                1
               232
              34543
             4567654
            567898765
          
           67890109876
          7890123210987
         890123454321098
        90123456765432109

Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''
'''
num= 1
for i in range(1,10):
    num=i
    for j in range(10,i,-1):
        print(" ",end=" ")
        
    for k in range(1,i+1):
        print(num,end=" ")
        num=num+1;
        
    for l in range(2,i+1):
        print(l,end=" ")
    
    print()
    
    '''
    
    
    
p=int(input("Enter value of p:")) 

for i in range(1,p+1): 

    for op in range(1,p+1-i): 
    print(" ",end="") 
    
    for j in range(i,i+i): 
    print(j%10,end="") 
    for k in range(j-1,i-1,-1): 
    print(k%10,end="") 
   print("\r")
    
    '''


















