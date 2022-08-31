# ===============================
# Approch 1:
lst = [20,40,70,50,60,10,80,30]

lst.sort()
print(lst)

print(f"\nFirst Largest Number is :--> {lst[-1]}")
print(f"Second Largest Number is :--> {lst[-2]}\n")


# ===============================
# Approch 2:

# lst = [20,40,70,50,60,10,80,30]

new_l= set(lst)

new_l.remove(max(new_l))    # {70, 40, 10, 50, 20, 60, 30}

print(f"Second Largest Number is :--> {max(new_l)}")



