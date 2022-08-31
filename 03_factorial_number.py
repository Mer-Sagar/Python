# 5! = 1 * 2 * 3 * 4 * 5 = 120

fact = 1
num =5

# ========================
# Approch 1 :

# if num<1:
#     print("\nNot Possible for negetive number....\n")
# elif num == 0:
#     print("\nFactorial of 0 is 1\n")
# else:
#     for i in range(1,num+1):

#         fact = fact * i
#     print(f"\nFactorial of {num} is {fact}\n")


# ========================
# Approch 2 :


# def factorial(num):
#     if (num==0 or num==1):
#         return 1
#     else:
#         return num * factorial(num-1)

# fact = factorial(5)
# print(f"\nFactorial of {num} is {fact}\n")

# ========================
# Approch 3 : Tenary operator

def factorial(num):
    
    return 1 if (num==0 or num==1) else num * factorial(num-1)

fact = factorial(5)
print(f"\nFactorial of {num} is {fact}\n")

