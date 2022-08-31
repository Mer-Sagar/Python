'''
 12. Write a Python program to concatenate following dictionaries to create a
     new one.
     d1={1:100, 2:200}
     d2={3:300, 4:400}
     d3={5:500, 6:600}
 
Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22


'''

d1={1:100, 2:200}
d2={3:300, 4:400}
d3={5:500, 6:600}
d4={}

for ele in (d1,d2,d3):
    d4.update(ele)

print(d4)