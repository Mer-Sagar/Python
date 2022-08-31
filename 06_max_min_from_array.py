# Maximum and Minimum

arr = [10,30,20,40,5]

max = arr[0]
min = arr[0]


for i in range(1,len(arr)):

    if max < arr[i] :
        max = arr[i]

    if min > arr[i] :
        min = arr[i]

print(max)
print(min)