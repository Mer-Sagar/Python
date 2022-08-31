# find() method finds the first occurance of the specified value.

str = "Welcome to python programming"

sub_str = "python"

# print(str.find(sub_str))        # found --> 11, not found-->1

if (str.find(sub_str) == 11):
    print("String found")
else:
    print("String not Found")