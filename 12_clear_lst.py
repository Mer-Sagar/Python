# =============================
# Approch 1:

lst = [10,20,90,50,80,70,30,60]

lst.clear()
print(lst)


# =============================
# Approch 2:

lst = [10,20,90,50,80,70,30,60]

lst = []
print(lst)



# =============================
# Approch 3:

lst = [10,20,90,50,80,70,30,60]

lst *=0
print(lst)


# =============================
# Approch 4:

lst = [10,20,90,50,80,70,30,60]

del lst[:]
print(lst)
