'''
 18. Write a Python program to print all Armstrong numbers between given
     range using functions.
     
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22

'''


def armstrong_num(start, end):


    for num in range(start, end + 1):
        
        # order of number
        order = len(str(num))   # number convert to string and 
                                # find lenth of string        
        # initialize sum
        sum = 0
        temp = num
        
        while temp > 0:
           digit = temp % 10
           sum += digit ** order
           temp //= 10
        
        if num == sum:
            print(num)

        

start=int(input("Range Start From : "))
end=int(input("Range End : "))

print("armstrong numbers between", start, "and", end, "are:")
armstrong_num(start,end)


 
          
  

