a=5
b=8

# Approch 1

temp = a
a = b
b = temp

print(f"Value of a ==> {a}\nValue of b ==> {b}")

# Approch 2

a, b = b,a
print(f"Value of a ==> {a}\nValue of b ==> {b}")
