# input : arr[] = {1, 2, 3}
# Output : 6
# 1 + 2 + 3 = 6

# =============
# Approch 1:

arr=[1,2,3,4,5]

print(sum(arr))

# print(sum(arr,10))
# print(sum(arr,-10))

# =============
# Approch 2:

sum1=0

for i in range(len(arr)):
    sum1= sum1 + arr[i]
    
print("-->",sum1)