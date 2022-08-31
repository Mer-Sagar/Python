'''
 19. Write a Python program to print all perfect numbers between given range
     using functions.
     
     [ perfect number is a positive integer that is equal to the sum of its
     positive divisor, excluding the number itself example 6 3+2+1= 6]
         
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''


def is_perfect_num(num):
    
    if num<1:
        return False
            
    sum=0
    for x in range(1,num):
        if num % x==0:              #if divisible by x then store in sum 
            sum =sum + x
            
    return sum==num            
                       

start=int(input("Range Start From : "))
end=int(input("Range End : "))


print("Perfect numbers between %d and %d" %(start, end))

for i in range(start,end+1):
    
    if is_perfect_num(i):       #fuction call in if
        
        print(i, end=' ')
    






 
          
  

