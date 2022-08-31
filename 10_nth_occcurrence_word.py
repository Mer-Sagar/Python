# Nth occurrance remove 
lst = ["India","australia","Englend","India","Sri Lanka","Israial","India"]

word = "India"

count = 0
n=2

for i in range(len(lst)-1):
    
    if lst[i] == word:
        count= count +1

        if(count==n):                   #  remove duplicate :--> if (count>1)
            del lst[i]

print(lst)