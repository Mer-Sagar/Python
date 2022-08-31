# =============
# Approch 1:

lst=[1,2,3,4,5]

print(sum(lst))

# print(sum(arr,10))
# print(sum(arr,-10))

# =============
# Approch 2:

sum1=0

for i in range(len(lst)):
    sum1= sum1 + lst[i]
    
print("-->",sum1)