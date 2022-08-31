#  Search element

lst = ["India","Australia","Englend","India","Sri Lanka","Israial","India"]

find = "Bhutan"
flag = 0

for i in lst:

    if i ==find:
        flag = 1
        break

if flag==1:
    print("element found  ")
else:
    print("element not found  ")

