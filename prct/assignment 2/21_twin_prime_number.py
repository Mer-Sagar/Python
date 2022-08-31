'''
 21. Write a python program to find twin prime numbers up to a range.
     [ex 3,5 5,7 11,13 17,19 41,43 ] all are twin prime their number
     difference is 1
         
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''

def is_prime(num):
    if num<2:
        return False
    
    for i in range(2,num):
        if num % i==0:
            return False
    return True
    


start=int(input("Start Range from : "))
end= int(input("End Range : "))

for i in range(start,end+1):
    
    if(is_prime(i) and is_prime(i+2)):
        print("%d,%d "%(i,i+2))
    






 
          
  

