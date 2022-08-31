'''
 14. Write a Python program to remove duplicate values from Dictionary.
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''

# dict = {'a': 100, 'b':200, 'c':300}

# initializing dictionary
test_dict = { 'first' : 10, 'second' : 15, 'thired' : 20, 'fourth' : 10, 'fifth' : 20}
  
# printing original dictionary
print("The original dictionary is : \n" + str(test_dict))
  
# Remove duplicate values in dictionary
# Using loop
temp = []
res = dict()
for key, val in test_dict.items():        #get key and values as tuple in list
    if val not in temp:
        temp.append(val)
        res[key] = val
  
# printing result 
print("The dictionary after values removal : \n" + str(res))
  


  

