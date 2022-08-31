# =============
# Approch 1:

str = "My Name is Sagar"

count=0

for i in str:
    count = count + 1

print(count)


# =============
# Approch 2:

str = "My Name is Sagar"

count=0

while str[count:]:
    count = count + 1

print(count)



# =============
# Approch 3:

str = "My Name is Sagar"

print(len(str))

# =============
# Approch 4: join and count

str = "Sagar"
ran_str = 'Z'

print((ran_str).join(str))
print((ran_str).join(str).count(ran_str)+1)
