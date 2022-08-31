'''
 17. Write a Python program to find all prime numbers between given range
     using functions.
     
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''


def prime_num(start, end):

    for num in range(start, end + 1):
       # all prime numbers are greater than 1
       if num > 1:
           for i in range(2, num):
               if (num % i) == 0:
                   break
           else:
               print(num)
               

start=int(input("Range Start From : "))
end=int(input("Range End : "))

print("Prime numbers between", start, "and", end, "are:", )
c=prime_num(start,end)


 


 
          
  

