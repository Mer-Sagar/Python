str = input("Enter String :--> ")

rev_str = str[::-1]
print(rev_str)

if (str == rev_str):
    print("\n Palindrom") 
    
else:
    print("\n Not Palindrom")