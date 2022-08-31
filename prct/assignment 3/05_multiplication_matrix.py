"""
5. Write a program that reads in two matrices and multiply them. Display the resultant matrix.


Name  : Mer Sagar        Roll No.: 21
Class : MCA sem-1        Year    : 2021-22
"""
import numpy as np

def matrix_print(mat, r,c):
    for i in range(r):
        for j in range(c):
            print(mat[i][j], end=" ")
        print()

r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of column : "))
    
lst1 = []
lst2 = []

for i in range(0, r*c):
    item = int(input("Enter the element of matrix 1 : "))
    lst1.append(item)

for i in range(0, r*c):
    item = int(input("Enter the element of matrix 2 : "))
    lst2.append(item)

matrix1 = np.array(lst1).reshape(r,c)
matrix2 = np.array(lst2).reshape(r,c)
result = np.zeros([r, c], dtype=int)

for i in range(r):
    for j in range(c):
        for k in range(r):
            result[i][j] += matrix1[i][k] * matrix2[k][j]   
            
    
print("Matrix 1:")
matrix_print(matrix1, r, c)
print("Matrix 2:")
matrix_print(matrix2, r, c)
print("Matrix 1 * matrix 2:")
matrix_print(result, r, c)


    
    

                        
        
        