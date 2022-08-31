# element occurrance 


# ===============
# Approch 1 : 

lst = ["India","australia","Englend","India","Sri Lanka","Israial","India"]

word = "India"

count = 0


for i in range(len(lst)-1):
    
    if lst[i] == word:
        count= count +1

print(count)

# ===============
# Approch 2 : lst.count(word)

lst = ["India","australia","Englend","India","Sri Lanka","Israial","India"]
word = "India"

print(f"{word} has occured {lst.count(word)} times")

# ===============
# Approch 3 : 

from collections import Counter

lst = ["India","australia","Englend","India","Sri Lanka","Israial","India"]
word = "India"

dic = Counter(lst)   # Counter({'India': 3, 'australia': 1, 'Englend': 1, 'Sri Lanka': 1, 'Israial': 1})

print(f"{word} has occured {dic[word]} times")