# =============================
# Approch 1:

lst = [10,20,90,50,80,70,30,60]
lst_c = lst[:]

print(lst_c)


# =============================
# Approch 2:

lst = [10,20,90,50,80,70,30,60]
lst_c2 = []

lst_c2.extend(lst)
print(lst_c2)



# =============================
# Approch 3:

lst = [10,20,90,50,80,70,30,60]

lst_c3 = lst.copy()

print(lst_c3)


# =============================
# Approch 4: List comprehension

lst = [10,20,90,50,80,70,30,60]

lst_c4 = [i for i in lst]
print(lst_c4)
