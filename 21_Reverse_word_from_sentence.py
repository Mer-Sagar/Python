# Input :  I am from India
# Output : India from am I 

str = "I am from India"

words = str.split(" ")
# print(words)                 # ['I', 'am', 'from', 'India']


words = words[::-1]
# print(words)                 # ['India', 'from', 'am', 'I']

output_str = ' '.join(words)
print(output_str)
