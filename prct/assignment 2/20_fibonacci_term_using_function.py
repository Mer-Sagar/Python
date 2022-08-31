'''
 20. Write a Python program to generate nth Fibonacci term using function.
         
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''
# Python program to display the Fibonacci sequence

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = int(input("Enter Number of Term you wnat to find : "))

lst =[]

# check if the number of terms is valid

if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       c=lst.append(recur_fibo(i))
   
   print(lst)               # serries
   
   print(lst[nterms-1])     # n th term
       
    






 
          
  

