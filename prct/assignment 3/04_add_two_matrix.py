"""
4.  Write a program to add two matrices.


Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""
import numpy as np

row=int(input("Enter Row :"))
col=int(input("Enter Column :"))

list1=[]
list2=[]

for i in range(0, row*col):
    ele=int(input("Enter element fo Matrix 1 : "))
    list1.append(ele)

for j in range(0, col*row):
    ele = int(input("Enter element for Matrix 2 : "))
    list2.append(ele)

matrix1 = np.array(list1).reshape(row,col)
matrix2 = np.array(list2).reshape(row,col)

result = np.zeros([row,col], dtype=int)

for i in range(row):
    for j in range(col):
        # for k in range(row):
            
            result[i][j] = matrix1[i][j] + matrix2[i][j]

            # result[i][j] += matrix1[i][k] * matrix2[k][j]   


for i in range(0,row):
    for j in range(0,col):
        print(result[i][j], end=" ")
    print()


# import numpy as np

# row = int(input("Enter Number of Rows : "))
# col = int(input("Enter Number of Columns : "))
# lst1 = []
# lst2 = []

# for i in range(0, row*col):
#     item = int(input("Enter the element of Matrix 1 : "))
#     lst1.append(item)

# for i in range(0, row*col):
#     item = int(input("Enter the element of Matrix 2 : "))
#     lst2.append(item)
    
# matrix1 = np.array(lst1).reshape(row,col)
# matrix2 = np.array(lst2).reshape(row,col)

# result = np.empty([row, col], dtype=int)

# for i in range(0, row):
#     for j in range(0, col):
#         result[i][j] = matrix1[i][j] + matrix2[i][j]

# for i in range(0, row):
#     for j in range(0, col):
#         print(result[i][j], end=" ")
#     print()

                 
        
        