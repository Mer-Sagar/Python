


lst = [12,34,53,86,45,95,76]

print("Before Swaping : -->",lst)

lst[0],lst[-1] = lst[-1],lst[0]

print("After Swaping : -->",lst)


# =================================================
# Output : 
# Before Swaping : --> [12, 34, 53, 86, 45, 95, 76]
# After Swaping : --> [76, 34, 53, 86, 45, 95, 12]

#  Approch 2:

lst = [12,34,53,86,45,95,76]

start,*mid,end = lst

print(start)
print(mid)
print(end)

lst =  [end,*mid,start]

print("After Swaping : -->",lst)

# ====================================
# Output : 
# 12
# [34, 53, 86, 45, 95]
# 76
# After Swaping : --> [76, 34, 53, 86, 45, 95]

#  Approch 3:

lst = [12,34,53,86,45,95,76]

print("Before Swaping : -->",lst)

first = lst.pop(0)
last = lst.pop(-1)

lst.insert(0,last)
lst.insert(-1,first)

print("After Swaping : -->",lst)

# =================================================
# Output : 
# Before Swaping : --> [12, 34, 53, 86, 45, 95, 76]
# After Swaping : --> [76, 34, 53, 86, 45, 95, 12]


